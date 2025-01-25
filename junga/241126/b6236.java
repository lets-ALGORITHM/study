import java.util.Arrays;
import java.util.Scanner;

/*
 * [이분 탐색]
 * 1. 이분 탐색으로 적절한 K값을 구할 건데
 * 중요한 건 탐색 범위.
 */

public class b6236 {
    static int n;
    static int m;
    static int[] budget;
    static int ans = Integer.MAX_VALUE;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        m = sc.nextInt();
        budget = new int[n]; // i번째날에 이용할 금액
        int max = Integer.MIN_VALUE;
        for (int i=0;i<n;i++) {
            budget[i] = sc.nextInt();
            max = Math.max(max, budget[i]); // 하루 예산 중 가장 큰 값
        }
        sc.close();

        /*
         * 이분탐색은 최소가 max, 최대는 전체 예산 합친 금액
         * why?
         * 1. m==n인 경우.. 매일매일 인출해야 하므로 최소 인출값은 예산 중 가장 큰 금액
         * 2. m==1인 경우.. 한 번만 인출해야 하므로 전체 예산 합친 금액 인출 필요
         */
        binarySearch(max, Arrays.stream(budget).sum());
        System.out.println(ans);
    }

    static int cnt(int k) { // 해당 K 예산이 문제의 조건을 만족하는지 판단(by 인출 횟수)
        int now = 0;
        int cnt = 0;
        for (int i = 0; i < n; i++) {
            if (k < budget[i]) { // 하루 예산도 충족하지 못하면 실패
                return -1;
            }
            if (now < budget[i]) { // 현재 금액으로 충족 불가능하면 인출
                now = k;
                cnt++;
            }
            now -= budget[i];
        }
        return cnt;
    }

    static void binarySearch(int a, int b) {
        int left = a;
        int right = b;
        while (left <= right) {
            int mid = (left + right) / 2;
            int count = cnt(mid);
            if (count == -1 || count > m) { // k가 조건 충족 못해 실패하는 경우(인출 금액 부족)
                left = mid+1; // k를 더 늘려 다시 탐색
            }
            else { // k가 조건 충족하면
                ans = Math.min(mid, ans); // 답을 더 작은 값으로 업데이트
                right = mid-1; // k를 더 줄여 다시 탐색
            }
        }
    }
}
