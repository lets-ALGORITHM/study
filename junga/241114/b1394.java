import java.util.Scanner;
import java.util.Arrays;

/*
 * https://jgeun97.tistory.com/136
 * 규칙 : 대입해봐야 하는 횟수 = 정답[:-2]까지 대입해봐야 하는 횟수 * 암호 길이 + 암호로 사용 가능한 문자 중 정답[-1]의 인덱스+1
 */
public class b1394 {
    static Code[] codes;
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        String[] chars = sc.nextLine().split("");
        codes = new Code[chars.length];
        for (int i=0;i<chars.length;i++) codes[i] = new Code(chars[i], i+1);
        Arrays.sort(codes); // 추후 이분탐색 하기 위해 정렬

        String ansCode = sc.nextLine();
        sc.close();

        int ans = 0;

        // 한글자짜리, 두글자짜리, ... 순차적으로 계산하기 위해 ansCode 길이만큼만 for문 순회
        // ex. cat을 찾아야 함 => c 찾는 데 걸리는 횟수 먼저 찾고 -> ca 찾고 -> cat 찾기
        for (int i=0;i<ansCode.length();i++) {
            ans = (ans*codes.length + findIdx(ansCode.substring(i, i+1))) % 900528;
        }
        System.out.println(ans % 900528);
    }

    static class Code implements Comparable<Code> {
        String str;
        int idx;

        Code(String str, int idx){
            this.str = str; this.idx = idx;
        }

        // this.str이 사전순으로 더 앞에 있으면 음수, 같으면 0, 뒤에 있으면 양수
        // 이분탐색 시 사용
        @Override
        public int compareTo(Code c) {
            if (!this.str.equals(c.str)) return this.str.compareTo(c.str);
            return this.idx - c.idx;
        }

        @Override
        public boolean equals(Object obj) {
            Code code = (Code)obj;
            if (this.str.equals(code.str)) return true;
            return false;
        }
    }

    // 인덱스 찾을 때 for문으로 돌면서 찾으면 시간초과 날 수 있음 => 이분탐색
    static int findIdx(String str){
        int L = 0, R = codes.length-1, pos = R;
        while (L<=R) {
            int mid = (L+R)/2;
            if (str.compareTo(codes[mid].str) < 0) {
                R = R-1;
                pos = R;
            } else {
                L = L+1;
            }
        }
        return codes[pos].idx;
    }
}