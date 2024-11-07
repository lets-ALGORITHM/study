import java.util.Scanner;

public class b1393 {
    static int xs;
    static int ys;
    public static int gcd(int p, int q) {
       if (q == 0) return p;
       return gcd(q, p%q);
    }

    public static double dist(int x, int y) {
        return Math.sqrt((xs-x)*(xs-x) + (ys-y)*(ys-y));
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        xs = sc.nextInt();
        ys = sc.nextInt();
        int xe = sc.nextInt();
        int ye = sc.nextInt();
        int dx = sc.nextInt();
        int dy = sc.nextInt();
        sc.close();

        int gcd = gcd(dx, dy);
        int xx = dx/gcd, yy = dy/gcd;

        double minDist = Double.POSITIVE_INFINITY;
        int i = 0;
        int bestX = xe, bestY = ye;
        
        while (true) {
            int tx = xe + xx*i;
            int ty = ye + yy*i;
            double d = dist(tx, ty);
            if (d > minDist) {
                break;
            }
            minDist = d;
            bestX = tx;
            bestY = ty;
            i += 1;
        }
        System.out.printf("%d %d", bestX, bestY);
    }
}
