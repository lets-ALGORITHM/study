import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/*
 * 그냥 현재 위치+본인 사거리 이용해서 끝까지 다 갈 수 있나 그리디로 체크
 */

public class b15889 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] locations = new int[n];

        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i=0;i<n;i++) {
            locations[i] = Integer.parseInt(st.nextToken());
        }        
        
        if (n==1) {
            System.out.println("권병장님, 중대장님이 찾으십니다");
        } else {
            int[] ranges = new int[n-1];
            st = new StringTokenizer(br.readLine());
            for (int i=0;i<n-1;i++) {
                ranges[i] = Integer.parseInt(st.nextToken());
            }

            int reachable = 0;
            for (int i=0;i<n-1;i++) {
                if (locations[i] <= reachable) {
                    reachable = Math.max(reachable, locations[i]+ranges[i]);
                }
            }

            if (reachable >= locations[n-1]) {
                System.out.println("권병장님, 중대장님이 찾으십니다");
            } else {
                System.out.println("엄마 나 전역 늦어질 것 같아");
            }
        }
    }
}
