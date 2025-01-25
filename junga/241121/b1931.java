import java.util.Arrays;
import java.util.Comparator;
import java.util.Scanner;

/*
 * 최대한 많은 회의 해야 함 
 * 1. 종료시간 빠른 순 정렬
 * 2. 종료시간 같으면 시작시간 빠른 순 정렬
 * 해서 종료시간 빠른것 선택 후 => 시작시간이 해당 회의의 종료시간보다 크거나 같은 바로 다음 회의 선택
 */

public class b1931 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        int[][] meetings = new int[n][2];
        for (int i=0;i<n;i++) {
            meetings[i][0] = sc.nextInt(); // 회의 시작시간
            meetings[i][1] = sc.nextInt(); // 회의 종료시간
        }
        sc.close();;

        Arrays.sort(meetings, new Comparator<int[]>() {
            @Override
            public int compare(int[] m1, int[] m2) {
                if (m1[1] == m2[1]) { // 종료시간 같으면
                    return m1[0] - m2[0]; // 시작시간 빠른순 정렬
                }
                return m1[1] - m2[1]; // 종료시간 빠른순 정렬
            }
        });

        int ans = 0;
        int endTime = 0;

        for (int[] meeting : meetings) {
            if (endTime <= meeting[0]) {
                endTime = meeting[1];
                ans ++;
            }
        }

        System.out.println(ans);
    }
}
