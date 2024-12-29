import java.util.ArrayList;
import java.util.List;
import java.util.Arrays;
import java.util.Scanner;

/*
 *  DP..라는 건 알겠는데 어케 해결해나가야 할지 몰라서 못 풂. 미완성 및 오답 코드 ㅜㅜ
 */

public class b25289 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        List<Integer> nums = new ArrayList<>();
        for (int i=0;i<n;i++) {
            nums.add(sc.nextInt());
        }
        sc.close();

        int[] length = new int[n];
        Arrays.fill(length, 1);;

        for (int i=0;i<n;i++) {
            for (int j=i+1;j<n;j++) {
                int x = 1;
                length[j] = Math.max(length[j], x);
                int diff = nums.get(j) - nums.get(i);
                for (int k=nums.get(j);k<=100;k+=diff) {
                    length[nums.indexOf(k)] = Math.max(length[nums.indexOf(k)], x);
                }
            }
        }
    }
}
