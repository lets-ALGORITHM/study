import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/*
 * 0분에서 max분 사이에서 이분탐색!
 */

public class b17245 {
    static int[] computers;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        computers = new int[(int) Math.pow(n, 2)];
        double sum = 0;
        int max = 0;
        for (int i=0;i<n;i++) {
            String[] temp = br.readLine().split(" ");
            for (int j=0;j<n;j++) {
                int tempInt = Integer.parseInt(temp[j]);
                computers[i*n+j] = tempInt;
                sum += tempInt;
                max = Math.max(max, tempInt);
            }
        }
        sum /= 2;

        int left = 0;
        int right = max;
        int mid;
        while (left <= right) {
            mid = (left+right)/2;
            if (calc(mid) >= sum) {
                right = mid-1;
            } else {
                left = mid+1;
            }
        }
        System.out.println(left);
    }
    static long calc(int n) {
        long cnt = 0;
        for (int i=0;i<computers.length;i++) {
            cnt += Math.min(computers[i], n);
        }
        return cnt;
    }
}
