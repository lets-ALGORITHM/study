import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/*
 * 기울기가 음수인 이차함수 그래프를 한 단위로 해서
 * (꼭짓점 기준으로 터뜨릴 수 있는 애들을 한 단위로 묶음)
 * 그래프 시작점인지 : start
 * 값이 증가하고 있는 중인지 : up
 * 
 * 를 이용해서..
 * 한 세트의 이차함수에서 가장 높은 꼭짓점이면 프린트하는 식으로 진행
 * 
 * 
 * 하려고 했는데 63퍼에서 틀렸습니다만 계속 나옴.. 왜 틀렸는지 도저히 모르겠고,, 온갖 반례를 넣어봐도 모르겠고..
 * 챗지피티한테 물어봐도 멍청한짓만 하고... 헬프..
 */
public class b2232 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        boolean up = true;
        boolean start = true;
        int prev = Integer.parseInt(br.readLine());

        // 길이가 하나면 그냥 그거 출력
        if (n == 1) {System.out.println(1);}
        for (int i=2;i<n+1;i++) {
            int x = Integer.parseInt(br.readLine());
            // 시작점이거나 올라가는 중이고 + 전의 값보다 줄어들었으면? 전의 값이 꼭짓점이므로 출력!
            if ((start || up) && prev > x) {
                System.out.println(i-1);
                up = false;
                start = false;
            } else { // 꼭짓점 아니라면
                if (prev < x) { // 올라가는 중이에여
                    up = true;
                }
                else if (prev > x) { // 내려가는 중이에여 + 내려가는 중이니 시작점 아니에여
                    up = false;
                    start = false;
                }
                else if (prev == x) { // 직전 값과 값이 같아여
                    start = true; // 직전 값 > 현재 값이어야 터뜨릴 수 있으므로 한 세트 아님! 고로 시작점
                    if (up) { // 올라가는 중이었으면 전전 지뢰는 직전 지뢰가 터져야만 터지므로 직전 지뢰 터뜨려!
                        System.out.println(i-1);
                        up = false;
                    }
                }
            }
            if (i == n && (up || start)) { // 마지막 지뢰가 혼자 터져야 하는 경우이면 터뜨려!
                System.out.println(n);
            }
            prev = x;
        }
    }
}
