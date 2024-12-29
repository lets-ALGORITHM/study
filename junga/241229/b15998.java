import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

/*
 * ??? 왜 틀렸는지도.. 모르겠고.. 정답코드가 진짜 정답인지도 모르겠고..
 * 1. 최대공약수 구함
 * 2. 출금할 일 없는 경우 1 출력
 * 3. 구한 최대공약수가 남은 금액보다 많은 경우 모순 존재하므로 -1 출력
 */
public class b15998 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        boolean is1Available = true;
        boolean noWithdrawal = true;
        int n = sc.nextInt();
        int[][] logs = new int[n][2];
        int money = 0;
        List<Integer> candidates = new ArrayList<>();
        for (int i=0;i<n;i++) {
            logs[i][0] = sc.nextInt();
            logs[i][1] = sc.nextInt();
            if (logs[i][1] > 0) {
                is1Available = false;
            }
            if (logs[i][0] < 0) {
                noWithdrawal = false;
                if (-logs[i][0] > money) {
                    int charged = -logs[i][0] + logs[i][1] - money;
                    candidates.add(charged);
                }
            }
            money = logs[i][1];
        }
        sc.close();

        long ans;
        if (candidates.size() > 0) {
            ans = gcd(candidates);
        } else {
            ans = 1;
        }

        boolean isAvailable = true;
        for (int i=0;i<n;i++) {
            if (ans <= logs[i][1]) {
                isAvailable = false;
                break;
            }
        }
    
        if (noWithdrawal) {
            System.out.println(1);
        } else if (ans == 1) {
            if (!is1Available) {
                System.out.println(-1);
            }
        } else {
            if (ans > 9 * Math.pow(10, 18) || !isAvailable) {
                System.out.println(-1);
            } else {
                System.out.println(ans);
            }
        }

    }

    public static long gcd(List<Integer> candidates) {
        long result = candidates.get(0);
        for (int i = 1; i < candidates.size(); i++) {
            result = gcd(result, candidates.get(i));
        }
        return result;
    }
    
    public static long gcd(long a, long b) {
        if (b == 0) return a;
        return gcd(b, a % b);
    }
}
