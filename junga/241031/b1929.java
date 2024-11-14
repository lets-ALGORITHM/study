import java.util.Scanner;
import java.io.BufferedWriter;
import java.io.OutputStreamWriter;
import java.io.IOException;

public class b1929 {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int m = sc.nextInt();
        int n = sc.nextInt();
        sc.close();

        int[] arr = new int[1000001];
        for (int i=2;i<=n;i++) { // 제곱근까지만 탐색해도 됨
            arr[i] = i;
        }

        for (int i=2;i<=n;i++) {
            if (arr[i] == 0) continue;
            
            for (int j=i*2;j<=n;j+=i) {
                arr[j] = 0;
            }
        }

        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        for (int i=m;i<=n;i++) {
            if (arr[i] != 0) bw.write(arr[i] + "\n"); 
        }
        bw.flush();
    }
}
