import java.util.Arrays;
import java.util.Scanner;

public class b12785 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int w = sc.nextInt();
        int h = sc.nextInt();
        int x = sc.nextInt();
        int y = sc.nextInt();
        sc.close();

        int num = 1000007;

        int[][] map = new int[w+1][h+1];
        map[1][1] = 1;
        for (int i=1;i<x+1;i++) {
            for (int j=1;j<y+1;j++) {
                map[i][j] = Math.max(map[i][j], (map[i-1][j] + map[i][j-1])%num);
            }
        }

        for (int i=x;i<w+1;i++) {
            for (int j=y;j<h+1;j++) {
                map[i][j] = Math.max(map[i][j], (map[i-1][j] + map[i][j-1])%num);
            }
        }

        // System.out.println(Arrays.deepToString(map));

        System.out.println(map[w][h]);
    }
}
