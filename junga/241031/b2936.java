import java.util.Scanner;

public class b2936 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int x = sc.nextInt();
        int y = sc.nextInt();
        sc.close();
        double ax;
        double ay;

        if (x==0 && y==0) {
            ax = 125;
            ay = 125;
        } else if (x==250 && y==0) {
            ax = 0;
            ay = 125;
        } else if (x==0 && y==250) {
            ax = 125;
            ay = 0;
        } else {
            if (x==0) {
                ax = 31250.0 / Math.max(250 - y, y);
                ay = (y < 125) ? 250 - ax : 0;
            } else if (y==0) {
                ay = 31250.0 / Math.max(250 - x, x);
                ax = (x < 125) ? 250 - ay : 0;
            } else {
                if (x<125) {
                    ay = 0;
                    ax = 250 - 31250.0/y;
                } else {
                    ax = 0;
                    ay = 250 - 31250.0/x;
                }
            }
        }

        System.out.printf("%.2f %.2f", ax, ay);
    }
}
