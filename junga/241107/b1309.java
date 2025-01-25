import java.util.Scanner;
import java.util.Arrays;

// https://great-park.tistory.com/131
/*
 * [DP]
 * 1. dp[n][0] : n번째 열이 비는 경우의 수
 * 2. dp[n][1] : n번째 열에서 왼쪽 칸에 위치하는 경우의 수
 * 3. dp[n][2] : n번째 열에서 오른쪽 칸에 위치하는 경우의 수
 */


public class b1309 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        sc.close();
        int ans = 0;

        int[][] dp = new int[n+1][3];
        Arrays.fill(dp[1], 1);

        for (int i=2;i<=n;i++) {
            // i번째 열을 비울거면 그 전 열에 사자가 어느 위치에 있든 상관 없음
            dp[i][0] = (dp[i-1][0] + dp[i-1][1] + dp[i-1][2]) % 9901;
            // i번째 열에서 왼쪽 칸에 놓을거면 그 전 열이 비거나 오른쪽 칸에 있어야 함
            dp[i][1] = (dp[i-1][0] + dp[i-1][2]) % 9901;
            // i번쩨 열에서 오른쪽 칸에 놓을거면 그 전 열이 비거나 왼쪽 칸에 있어야 함
            dp[i][2] = (dp[i-1][0] + dp[i-1][1]) % 9901;
        }

        for (int i=0;i<3;i++) {
            ans += dp[n][i];
        }

        System.out.println(ans%9901);
    }
}