import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/*
 * DP인 것만 파악하면 + 정수타입만 잘 설정하면 쉬운 문제!
 * 1. 1, 2, 3만으로 숫자 n을 만들기
 * 2. 순서가 달라지면 다른 경우로 취급
 * 
 * 1 -> 1
 * 2 -> 2, 1+1
 * 3 -> 3, 2+1, 1+2, 1+1+1
 * 4 -> 3+1, 2+1+1, 1+2+1, 1+1+1+1, 2+2, 1+1+2, 1+3
 *      (3을 만드는 경우의 수들에서 +1)   (2를 만드는 경우의 수들에서 +2) (1을 만드는 경우의 수들에서 +3)
 * ==> dp 점화식은 dp[x] = dp[x-1] + dp[x-2] + dp[x-3]
 */

public class b15988 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int tc = Integer.parseInt(br.readLine());

        long[] dp = new long[1000001]; // 스택오버플로우를 방지하기 위해 int가 아닌 long 배열 사용
        dp[1] = 1;
        dp[2] = 2;
        dp[3] = 4;
        for (int i=4;i<1000001;i++) {
            dp[i] = (dp[i-3] + dp[i-2] + dp[i-1])%1000000009;
            }

        for (int i=0;i<tc;i++) {
            int n = Integer.parseInt(br.readLine());
            System.out.println(dp[n]);
        }
    }
}