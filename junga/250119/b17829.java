import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class b17829 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        StringTokenizer st;
        int[][] arr = new int[n][n];

        for (int i=0;i<n;i++) {
            st = new StringTokenizer(br.readLine());
            for (int j=0;j<n;j++) {
                arr[i][j] = Integer.parseInt(st.nextToken());
            }
        }

        for (int i=n;i>1;i/=2) {
            int[][] temp = new int[i/2][i/2];
            for (int j=0;j<i;j+=2) {
                for (int k=0;k<i;k+=2) {
                    // System.out.println(i+" "+j+" "+k);
                    temp[j/2][k/2] = calc(arr[j][k], arr[j][k+1], arr[j+1][k], arr[j+1][k+1]);
                }
            }
            arr = temp;
        }

        System.out.println(arr[0][0]);
    }

    static int calc(int a, int b, int c, int d) {
        int[] nums = {a, b, c, d};
        Arrays.sort(nums);
        return nums[nums.length - 2];
    }
}
