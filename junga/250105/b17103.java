import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class b17103 {
    static boolean[] numbers = new boolean[1000001];

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        setUp();

        int tc = Integer.parseInt(br.readLine());
        for (int i=0;i<tc;i++) {
            solve(Integer.parseInt(br.readLine()));
        }
        br.close();
    }

    static void setUp() {
        // 초기 값 설정 (에라토스테네스의 체 적용)
        // 0과 1은 소수가 아니므로 false
        for (int i = 0; i < 2; i++) {
            numbers[i] = false;
        }
        // 나머지는 일단 true로 초기화
        for (int i = 2; i < 1000001; i++) {
            numbers[i] = true;
        }

        // 에라토스테네스의 체로 소수 판별
        for (int i = 2; i * i < 1000001; i++) { // i * i가 배열 길이를 넘지 않을 때까지
            if (numbers[i]) { // 소수인 경우
                for (int j = i * i; j < 1000001; j += i) {
                    numbers[j] = false; // i의 배수는 소수가 아님
                }
            }
        }

    }

    static void solve(int n) {
        int ans = 0;
        for (int i=2;i<=n/2;i++) {
            if (numbers[n-i] && numbers[i]) {
                ans++;
            }
        }
        System.out.println(ans);
    }
}
