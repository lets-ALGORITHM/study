import java.util.ArrayList;
import java.util.Deque;
import java.util.LinkedList;
import java.util.List;
import java.util.Scanner;

/*
 * 그냥 데크 이용해서 pop, add 반복하면 된당
 */

public class b1158 {

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int k = sc.nextInt();
        sc.close();

        Deque<Integer> q = new LinkedList<>();
        for (int i=1;i<=n;i++) {
            q.add(i);
        }

        List<Integer> answer = new ArrayList<>();

        while (!q.isEmpty()) {
            for (int i=0;i<k;i++) {
                q.add(q.poll());
            }
            answer.add(q.pollLast());
        }

        System.out.println("<" + String.join(", ", answer.stream().map(String::valueOf).toArray(String[]::new)) + ">");
    }
    
}
