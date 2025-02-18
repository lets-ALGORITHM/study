import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

/*
 * 주차장 자리 남아있으면 집어넣고...
 * 꽉 찼으면 큐에 넣고..
 * 자리 다시 나면 큐에 있던 거 빼서 집어넣고... 그렇게 계산
 * 
 * prices[i] = i번째 주차장의 단위가격
 * weights[i] = i번째 자동차의 무게
 * q[i] = i번째로 대기 중인 자동차의 번호
 * occupied = 몇대의 차가 주차되어 있는지
 * parked[i] = i번째 자리에 주차된 자동차의 번호. 비어있으면 0
 */

public class b5464 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int n = Integer.parseInt(st.nextToken());
        int[] prices = new int[n];
        int m = Integer.parseInt(st.nextToken());
        int[] weights = new int[m+1];
        Queue<Integer> q = new LinkedList<>();
        int ans = 0;
        int occupied = 0;
        int[] parked = new int[n];

        for (int i=0;i<n;i++) {
            prices[i] = Integer.parseInt(br.readLine());
        }
        for (int i=0;i<m;i++) {
            weights[i+1] = Integer.parseInt(br.readLine());
        }

        for (int i=0;i<2*m;i++) {
            int temp = Integer.parseInt(br.readLine());
            if (temp < 0) {
                for (int j=0;j<n;j++) {
                    if (parked[j] == temp*-1){
                        if (q.size()>0) {
                            parked[j] = q.poll();
                            ans += prices[j] * weights[parked[j]];
                        } else {
                            parked[j] = 0;
                            occupied--;
                        }
                        break;
                    }
                }
            }
            else {
                if (occupied == n) {
                    q.add(temp);
                } else {
                    for (int j=0;j<n;j++) {
                        if (parked[j] == 0){
                            parked[j] = temp;
                            ans += prices[j] * weights[temp];
                            occupied++;
                            break;
                        }
                    }
                }
            }
            // for (int j=0;j<n;j++) {
            //     System.out.print(parked[j]);
            // }
            // System.out.println();
        }

        System.out.println(ans);
    }
}
