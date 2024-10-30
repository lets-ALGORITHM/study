import java.util.Scanner;
import java.util.Deque;
import java.util.ArrayDeque;
import java.util.List;
import java.util.Arrays;
import java.util.ArrayList;

public class b2573 {
    private static int[][] map;
    private static int[][] visited;
    private static int[] dx = {1, -1, 0, 0};
    private static int[] dy = {0, 0, 1, -1};
    private static List<int[]> ice = new ArrayList<>(); // 빙산 위치 저장
    private static int n;
    private static int m;
    private static int ans = 0; // 출력할 답(몇 번만에 빙하 나누어졌는지)
    private static int group;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        n = sc.nextInt();
        m = sc.nextInt();

        map = new int[n][m];
        for (int i=0;i<n;i++) {
            for (int j=0;j<m;j++) {
                map[i][j] = sc.nextInt();
                // 해당 좌표에 빙산이 있다면 이를 ice에 추가
                if (map[i][j] != 0) ice.add(new int[]{i, j});
            }
        }
        sc.close();

        // 빙산 다 녹아 없어질 때까지
        while (!ice.isEmpty()) {
            visited = new int[n][m];
            List<int[]> melted = new ArrayList<>(); // 다 녹은 빙산 저장할 리스트
            group = 0; // 빙산 덩어리 개수 저장할 변수

            for (int[] arr : ice) { // 현재 시점에서 존재하는 빙산들 조회
                int x = arr[0];
                int y = arr[1];
                if (visited[x][y] == 0) { // 아직 해당 좌표 방문 전이고
                    if (map[x][y] != 0) { // 해당 좌표에 빙산이 있다면
                        bfs(x, y); // bfs 돌면서 해당 빙산 묶음 녹이기
                        group ++;
                    }
                }
                // 해당 좌표의 빙산이 이미 녹았으면 녹일 후보에 저장
                if (map[x][y] == 0) melted.add(new int[]{x, y});
            }
            if (group > 1) { // 빙산이 2덩이 이상으로 나누어졌으면 답 출력
                System.out.println(ans);
                break;
            }
            // 이미 녹은 빙산들 ice에서 제거
            ice.removeIf(arrA -> melted.stream().anyMatch(arrB -> Arrays.equals(arrA, arrB)));
            ans++;
        }
        // 빙산 다 녹을 때까지 돌고도 나눠지지 않았으면 0 출력
        if (group < 2) System.out.println(0);

    }

    // 좌표가 정상 범위 안에 있는지 체크
    public static boolean check(int nowx, int nowy) {
        return nowx >= 0 && nowx < n && nowy >= 0 && nowy < m;
    }

    // 한 빙산 묶음 돈 후, 인접한 바다 개수만큼 한 번에 녹이기
    public static void bfs(int x, int y) {
        Deque<int[]> q = new ArrayDeque<>(); // (x, y)와 같은 빙산 묶음들 저장
        q.add(new int[]{x, y});
        visited[x][y] = 1;
        List<int[]> toMelt = new ArrayList<>(); // 어느 좌표를 얼만큼 녹일지 저장 (x좌표, y좌표, 얼마나 녹일지)

        while (!q.isEmpty()) {
            int[] temp = q.removeFirst();
            int tx = temp[0];
            int ty = temp[1];
            int sea = 0; // 인접한 바다 개수

            for (int i=0;i<4;i++) {
                int nx = tx + dx[i];
                int ny = ty + dy[i];
                if (check(nx, ny)) { // 정상 좌표 안에 있고
                    if (map[nx][ny] == 0) sea++; // 바다이면 sea++
                    else if (map[nx][ny] != 0 && visited[nx][ny] == 0) { // 빙산이고 아직 방문 전이면
                        q.add(new int[]{nx, ny}); // q에 add
                        visited[nx][ny] = 1; // 방문 처리
                    }
                }
            }
        
            if (sea > 0) toMelt.add(new int[]{tx, ty, sea}); // 인접 바다 개수가 1 이상이면 toMelt에 저장
        }

        for (int[] meltable : toMelt) { // 녹여야 하는 좌표들 돌면서 녹이기
            int mx = meltable[0];
            int my = meltable[1];
            int num = meltable[2];
            map[mx][my] = Math.max(0, map[mx][my] - num);
        }
    }
}