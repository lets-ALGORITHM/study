import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/*
 * [DP]
 * 
 * 1. 풀이 방법 : 
 * VIP 고정석들을 기준으로, 
 * VIP 고정석 사이에 위치한 좌석들을 배치할 수 있는 경우의 수를 모두 곱하면 됨
 * 예제로 들면 4, 7번째 좌석만 고정이므로 1~3, 5~6, 8~9번째 묶음들을 배치할 수 있는 경우의 수끼리 곱하기
 * 
 * 2. 경우의 수는 어떻게 구하나? (== dp 배열은 어떤 규칙으로 채우나?) :
 * cases[n] = cases[n-1] + cases[n-2]
 * why? 
 * cases[n-1] = n번째 친구가 n번째 좌석에 앉는 경우 == n-1개의 좌석을 배치하는 경우
 * cases[n-2] = n번째 친구가 자신에게 배정된 좌석이 아닌 n-1번째 좌석에 앉는 경우 == n-2개의 좌석을 배치하는 경우
 */

public class b2302 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int m = Integer.parseInt(br.readLine());

        int[] cases = new int[n+1];
        cases[0] = 1;
        cases[1] = 1;
        if (n>1) {
            cases[2] = 2;
            for (int i=3;i<n+1;i++) {
                cases[i] = cases[i-2]+cases[i-1];
            }
        }
        
        int ans = 1;
        int idx = 0;
        for (int i=0;i<m;i++) {
            int x = Integer.parseInt(br.readLine());
            ans *= cases[x-idx-1];
            idx = x;
        }
        ans *= cases[n-idx];

        System.out.println(ans);
    }
}
