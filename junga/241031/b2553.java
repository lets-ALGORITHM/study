import java.util.Scanner;

public class b2553 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        sc.close();

        long num = 1;
        for (int i=1;i<=n;i++) {
            num *= i;
            while (num%10 == 0) {
                num /= 10;
            }
            num %= 1000000;
        }

        System.out.println(num%10);

    }
}
