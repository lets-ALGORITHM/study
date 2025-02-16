import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;

/*
 * BFS인데 상하좌우가 아니라 주변 6군데를 탐색!
 */

public class b14397 {
    static int n, m;
    static boolean[][] visited;
    static Queue<int[]> q;
    static int[] dx = {-1, -1, 0, 0, 1, 1};
    static int[] dy_o = {0, 1, -1, 1, 0, 1};
    static int[] dy_e = {-1, 0, -1, 1, -1, 0};
    static String[][] map;
    static int ans;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String[] temp = br.readLine().split(" ");
        n = Integer.parseInt(temp[0]);
        m = Integer.parseInt(temp[1]);
        ans = 0;

        map = new String[n][m];
        for (int i=0;i<n;i++) {
            temp = br.readLine().split("");
            for (int j=0;j<m;j++) {
                map[i][j] = temp[j];
            }
        }

        visited = new boolean[n][m];
        
        for (int i=0;i<n;i++) {
            for (int j=0;j<m;j++) {
                if (map[i][j].equals("#") && !visited[i][j]) {
                    dfs(i, j);
                }
            }
        }

        System.out.println(ans);
    }

    static boolean isValidIndex(int x, int y) {
        if (x >= 0 && x < n && y >= 0 && y < m) {
            return true;
        }
        return false;
    }

    static void dfs(int x, int y) {
        Queue<int[]> q = new LinkedList<>();
        int[] now = {x, y};
        q.add(now);
        visited[now[0]][now[1]] = true;
        while (!q.isEmpty()) {
            int[] temp = q.poll();
            // System.out.println(temp[0]+" "+temp[1]);

            for (int i=0;i<6;i++) {
                int nx = temp[0]+dx[i];
                int ny;
                if (temp[0]%2 == 0) {
                    ny = temp[1]+dy_e[i];
                } else {ny = temp[1]+dy_o[i];}
                if (isValidIndex(nx, ny)) {
                    if (map[nx][ny].equals("#") && !visited[nx][ny]) {
                        int[] temp2 = {nx, ny};
                        // System.out.println("to add :"+nx+" "+ny);
                        visited[nx][ny] = true;
                        q.add(temp2);
                    } else if (map[nx][ny].equals(".")) {
                        // System.out.println(temp[0]+" "+temp[1]+" "+nx+" "+ny);
                        ans++;
                    }
                    
                }
            }
        }
    }
}
