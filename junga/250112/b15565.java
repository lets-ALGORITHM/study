import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

/*
 * 원래는 투포인터로 풀어보려다가.. 투포인ㄴ터로 길이가 10의 6승을 시간 낸에 다 돌 수가 있나?
 * 고민하다가 인터넷을 서치해봐씀다 결국 내손으로는 마무리는 못 했삼..
 * 
 * 아이디어
 * 1. 검사 대상 : 1이냐 아니냐만 판별하면 됨
 * 2. 그래서 1인 대상들의 인덱스를 리스트에 저장해두고, i번째와 i+k-1번째 간의 거리를 구하면 정답!
 * ex. 예제
 * indexs = [0, 4, 6, 9]
 * k가 3이므로 집합 크기 후보들은 (6-0+1=7, 9-4+1=6)
 * 따라서 6이 정답!
 */

public class b15565 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());
        List<Integer> indexs =  new ArrayList<>();

        st = new StringTokenizer(br.readLine());
        for (int i=0;i<n;i++) {
            int x = Integer.parseInt(st.nextToken());
            if (x == 1) {
                indexs.add(i);
            }
        }
        
        int ans = Integer.MAX_VALUE;

        for (int i=0;i<indexs.size()-k+1;i++) {
            ans = Math.min(ans, indexs.get(i+k-1)- indexs.get(i) + 1);
        }

        System.out.println(ans);
    }
}