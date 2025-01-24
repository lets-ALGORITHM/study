import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.StringTokenizer;

/*
 * a는 내림차순, b는 오름차순 정렬해서
 * a의 한 값 기준으로 b의 몇번째 요소까지 커버 가능한지 인덱스 구해서 더하기
 */

public class b7795 {
    static List<Integer> b;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int tc = Integer.parseInt(br.readLine());

        StringTokenizer st;
        for (int i=0;i<tc;i++) {
            st = new StringTokenizer(br.readLine());
            int n = Integer.parseInt(st.nextToken());
            int m = Integer.parseInt(st.nextToken());
            List<Integer> a = new ArrayList<>();
            b = new ArrayList<>();
            b.add(0);
            st = new StringTokenizer(br.readLine());
            for (int j=0;j<n;j++) {
                a.add(Integer.parseInt(st.nextToken()));
            }
            st = new StringTokenizer(br.readLine());
            for (int j=0;j<m;j++) {
                b.add(Integer.parseInt(st.nextToken()));
            }
            Collections.sort(a, Collections.reverseOrder());
            Collections.sort(b);

            int ans = 0;
            for (int j=0;j<n;j++) {
                int nowa = a.get(j);
                int temp = calc(nowa);
                // System.out.println(nowa+" "+temp);
                if (temp <= 0) {break;}
                ans += temp;
            }

            System.out.println(ans);
        }
    }

    static int calc(int a) {
        int left = 0, right = b.size()-1;
        while (left<=right) {
            int mid = (left+right)/2;
            // System.out.println(left+" "+right+" "+mid);
            int nowb = b.get(mid);
            if (nowb>=a) {right = mid-1;}
            else {left = mid+1;}
        }
        return right;
    }
}
