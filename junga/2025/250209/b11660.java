import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/**
 * 1. 표의 크기 size와 명령의 개수 cmd가 입력된다.
 * 2. 표 값을 입력받으면서 구간합 배열을 구한다.
 * 2-1. 현재 위치의 구간합 값은 (왼쪽 구간합 값 + 윗쪽 구간합 값 - 중복된 값 + 현재 입력 값)이다.
 * 3. 구간합 성질을 이용해 (마지막 구간합 값 - 시작위치 왼쪽의 구간합 값 - 시작위치 윗쪽의 구간합 값 + 중복되어 빼진 값)을 결과로 출력한다.
 */
public class b11660 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        
        StringTokenizer st = new StringTokenizer(br.readLine());
        int size = Integer.parseInt(st.nextToken());
        int cmd = Integer.parseInt(st.nextToken());

        int[][] subTotal = new int[size+1][size+1];
        for(int row=1; row<=size; row++) {
            st = new StringTokenizer(br.readLine());
            for(int col=1; col<=size; col++) {
            	// 2-1. 현재 위치의 구간합 값은 (왼쪽 구간합 값 + 윗쪽 구간합 값 - 중복된 값 + 현재 입력 값)이다.
                subTotal[row][col] = subTotal[row][col-1] + subTotal[row-1][col] - subTotal[row-1][col-1] + Integer.parseInt(st.nextToken());
            }
        }

        while(cmd-- > 0) {
            st = new StringTokenizer(br.readLine());
            int startRow = Integer.parseInt(st.nextToken());
            int startCol = Integer.parseInt(st.nextToken());
            int endRow = Integer.parseInt(st.nextToken());
            int endCol = Integer.parseInt(st.nextToken());
            int sum = subTotal[endRow][endCol] - subTotal[startRow-1][endCol] - subTotal[endRow][startCol-1] + subTotal[startRow-1][startCol-1];

            sb.append(sum).append('\n');
        }
        System.out.print(sb);
    }
}