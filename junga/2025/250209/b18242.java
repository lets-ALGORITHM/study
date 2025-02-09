import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class b18242 {
    static boolean[][] arr;
    static int x, y, z, n, m;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        arr = new boolean[n][m];
        x = 0;
        y = 0;
        z = 0;
        for (int i=0;i<n;i++) {
            String temp = br.readLine();
            for (int j=0;j<m;j++) {
                arr[i][j] = (temp.charAt(j) =='#')?true:false;
            }
        }

        findStart();
        // System.out.println(x+" "+y+" "+z);
        String ans = "";
        for (int i=y;i<y+z;i++) {
            if (!arr[x][i]) {ans = "UP";}
        }
        for (int i=x;i<x+z;i++) {
            if (!arr[i][y]) {ans = "LEFT";}
        }
        for (int i=y;i<y+z;i++) {
            if (!arr[x+z-1][i]) {ans = "DOWN";}
        }
        for (int i=x;i<x+z;i++) {
            if (!arr[i][y+z-1]) {ans = "RIGHT";}
        }
        System.out.println(ans);

    }

    static void findStart() {
        for (int i=0;i<n;i++) {
            for (int j=0;j<m;j++) {
                if (arr[i][j]) {
                    x = i;
                    y = j;
                    findLength(i, j);
                    return;
                }
            }
        }
    }
    static void findLength(int x, int y) {
        for (int i=y;i<m;i++) {
            if (!arr[x][i]) {
                if (i+1<m && !arr[x][i+1] || i == m-1) {
                    z = i-y;
                    return;
                }
            }
        }
        z = m-y;
        return;
    }
}
