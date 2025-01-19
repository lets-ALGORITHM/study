import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

/*
 * [메인 아이디어]
 * 1. 맞물릴 수 있는 최소 길이를 구해야 함
 * 1.1. 맞물린다 == (이와 이)만 아니면 다 맞물리는 경우라고 판단
 * 2. 가능한 최소 길이는 (두 기어 중 더 긴 부분의 길이 ~ 두 기어 길이의 합) 중에서 존재
 * 2.1. 왜냐하면 아무리 맞춰봐도 맞물리는 경우가 없어 그냥 병렬적으로 둬야 하는 경우거나, 아니면 예시1처럼 긴 부분 안에 짧은 부분이 쏙 들어갈 수 있으므로
 * 3. 그리고 맞물리게 하는 방법은 
 * 3.1. 짧은 부분이 왼쪽 + 긴 부분이 오른쪽
 * 3.2. 긴 부분 안에 짧은 부분이 포함
 * 3.3. 긴 부분이 왼쪽 + 짧은 부분이 오른쪽
 *      이렇게 총 세 가지 경우로 배치할 수 있으므로,
 *      긴 부분의 앞뒤에 짧은 부분의 길이만큼 0이라는 무의미한 요소를 추가한 뒤에
 *      해당 전체 리스트의 시작부분부터 끝부분까지 짧은 부분이 맞물릴 수 있는지 확인해가며 최소 길이를 갱신할 것
 *      == 긴 기어를 고정시켜두고, 짧은 기어를 긴 부분의 왼쪽에서 오른쪽으로 한 칸씩 움직이면서 맞춰가며 확인
 */

public class b1195 {
    static List<Integer> a = new ArrayList<>();
    static List<Integer> b = new ArrayList<>();
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(String.join(" ", br.readLine().split("")), " ");

        while (st.hasMoreTokens()) {
            a.add(Integer.parseInt(st.nextToken()));
        }
        st = new StringTokenizer(String.join(" ", br.readLine().split("")), " ");
        while (st.hasMoreTokens()) {
            b.add(Integer.parseInt(st.nextToken()));
        }

        // a가 무조건 짧은 기어가 되도록 바꿔줌
        if (a.size() > b.size()) {
            List<Integer> temp = new ArrayList<>();
            temp = a;
            a = b;
            b = temp;
        }
        // 긴 기어 앞뒤에 짧은 기어 길이만큼 0 추가
        for (int i=0;i<a.size();i++) {
            b.add(0, 0);
            b.add(0);
        }

        // 아무리 해도 맞물리지 않는 경우의 길이 == 답이 될 수 있는 최장 길이
        int ans = b.size() - a.size();

        // i : 짧은 기어의 시작 지점 인덱스
        for (int i=0;i<b.size()-a.size();i++) {
            if (isAvailable(i)) { // 맞물려지면
                int temp;
                // i가 어디인지에 따라 답(길이)이 달라짐
                if (i < b.size()-2*a.size()) { // i가 긴 기어의 실질적 시작지점 전인 경우
                    temp = b.size()-a.size()-i;
                }
                else { // 실질적 시작지점 후인 경우
                    temp = i;
                }
                // 답이 긴 기어의 길이 이상이어야 하고, 갱신하려면 이전 답보다 더 작아야 함
                ans = Math.min(ans, Math.max(temp, b.size()-2*a.size()));
            }
        }

        System.out.println(ans);
    }

    // 현재 위치에서 맞물려지는지 확인하는 함수
    static boolean isAvailable(int i) {
        for (int j=i;j<a.size()+i;j++) {
            if (b.get(j)+a.get(j-i) == 4) {
                return false;
            }
        }
        return true;
    }
}
