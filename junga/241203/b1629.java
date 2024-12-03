import java.util.Scanner;

/*
 * [모듈러 연산 - 나머지 정리..]
 * (a * b) % c = (a % c * b % c) % c
 * 요것이 핵심
 * 
 * a를 b번 곱한 걸 c로 나눈 나머지를 구해야 하므로.. 
 * (a^(b//2) * a^(b//2)) % c
 * [b가 짝수면]
 *  = ((a^(b//2) % c) * (a^(b//2) % c)) % c
 *  = ((((a^(b//4) % c) * (a^(b//4) % c)) % c) * (((a^(b//4) % c) * (a^(b//4) % c)) % c)) % c
 *  = ...
 * [b가 홀수면]
 *  = ((((a^(b//2) % c) * (a^(b//2) % c)) % c) * (a % c)) % c
 * 이렇게 //2씩 재귀로 파고들어가 계산해주면 됨
 */

public class b1629 {

    static int a, b, c;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        a = sc.nextInt();
        b = sc.nextInt();
        c = sc.nextInt();

        sc.close();

        if (b == 1) {System.out.println(a % c);} // 제곱할 필요 없으면 그냥 바로 리턴
        else {System.out.println(dc(b));}

    }

    static long dc(int i) {
        if (i == 1) { // 지수가 1이면
            return a % c; // 최대한 깊게 들어온거니까 리턴
        } else {
            long temp = dc(i/2); // i 기준으로 바로 밑 가지 값
            long pow = (temp * temp) % c; // 바로 밑 가지 값 제곱해서 c로 나눈 나머지 구해!
            
            if (i % 2 == 1) { // 지수가 홀수면 a를 c로 나눈 나머지 곱해서 다시 c로 나눈 나머지 구해
                return (pow * (a % c)) % c;
            }
            return pow;
        }
    }
}
