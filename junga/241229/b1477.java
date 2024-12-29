import java.util.Arrays;
import java.util.Scanner;

public class u1477 {
    static int[] areas;

    public static void main(String[] args) {
        /*
         * (이분탐색인건 감 잡았는데 어케 범위 설정 및 탐색해야할지를 못 구해서 결국 내 힘으로 풀기 실패)
         * [이분탐색]
         * 1. 범위 : 1 ~ L-1
         * 2. 탐색 방법 : 주어진 휴게소들 돌면서, sum(연속한 두 휴게소 사이에서 mid만큼의 간격으로 몇 개의 휴게소를 더 증축 가능한가?)를 기준으로
         *              총합이 m보다 작거나 같다면(sum <= m; 간격이 충분해!) 좌측 범위에서 다시 탐색, 많다면(sum > m; 간격이 너무 좁아!) 우측 범위에서 다시 탐색
         * 3. 마지막 left가 정답이 됨!
         * 3.1. 왜? left가 조건을 만족하는 값(sum이 m을 충족하는..) 중 최소값이므로
         * 3.2. left가 휴게소가 없는 간격 중 가장 큰 간격이라는 거지, 중간에 left보다 작은 간격으로 m개를 만족할 만큼 추가로 세울 수 있어서 (sum <= m)일 때의 left가 답이 되는 것
         */

        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int m = sc.nextInt();
        int l = sc.nextInt();

        areas = new int[n+2]; // 현재 휴게소
        areas[0] = 0;
        areas[n+1] = l;
        for (int i=0;i<n;i++) {
            areas[i] = sc.nextInt();
        }
        Arrays.sort(areas); // 이분탐색 전 휴게소 정렬

        int left = 1;
        int right = l-1;

        while (left <= right) {
            int mid = (left + right) / 2;
            int sum = count(mid);

            if (sum > m) {
                left = mid + 1;
            } else {
                right = mid - 1;
            }
        }

        System.out.println(left);

    }

    // mid일 때 휴게소 증축 몇 개 할 수 있는가?
    private static int count(int k) {
        int cnt = 0;
        for (int i=1;i<areas.length;i++) {
            cnt += (areas[i] - areas[i-1] - 1) / k;
        }
        return cnt;
    }
}
