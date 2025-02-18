import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/*
 * 원형이중연결리스트로 해보려다가.. 의외로 구현이 번거롭고 씅질나서 스스로 못 풂 ㅠ
 * 굳이 연결리스트 사용하지 않고 데크로 매번 새로 앞으로 보내고 뒤로 보내면서 풀어도 됨
 * 왜냐면 시간제한이 2초나 되기 때문! + 길어봤자 1000개임
 */
public class b2346 {
    
    static class CircularLinkedList {
        private Node head = null;
        private int size = 0;

        private static class Node {
            int index; // 풍선 번호 저장
            int value; // 종이에 적힌 숫자 저장
            Node prev;
            Node next;
            
            Node(int index, int value) {
                this.index = index;
                this.value = value;
            }
        }

        // 원형 연결 리스트에 요소 추가
        public void add(int index, int value) {
            Node newNode = new Node(index, value);
            if (size == 0) {
                head = newNode;
                head.next = head;
                head.prev = head;
            } else {
                newNode.prev = head.prev;
                newNode.next = head;
                head.prev.next = newNode;
                head.prev = newNode;
            }
            size++;
        }

        // 현재 위치에서 pop (현재 head를 터뜨림)
        public int popCurrent() {
            if (size == 0) throw new IllegalStateException("List is empty");

            int poppedIndex = head.index; // 터뜨리는 풍선의 번호 저장
            Node nextNode = head.next; // 다음 노드 미리 저장
            
            remove(head); // 현재 head 삭제

            // 리스트가 비어있지 않다면 head를 갱신
            if (size > 0) {
                head = nextNode;
            }

            return poppedIndex;
        }

        // n칸 이동 후 현재 위치 pop
        public int popMove(int move) {
            if (size == 0) throw new IllegalStateException("List is empty");

            if (move > 0) {
                for (int i = 0; i < move; i++) {
                    head = head.next;
                }
            } else {
                for (int i = 0; i < -move; i++) {
                    head = head.prev;
                }
            }

            return popCurrent();
        }

        // 노드 삭제
        private void remove(Node target) {
            if (size == 1) {
                head = null;
            } else {
                target.prev.next = target.next;
                target.next.prev = target.prev;
            }
            size--;
        }

        public boolean isEmpty() {
            return size == 0;
        }

        // 현재 head의 값 반환
        public int getCurrentValue() {
            if (size == 0) throw new IllegalStateException("List is empty");
            return head.value;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        StringTokenizer st = new StringTokenizer(br.readLine());

        CircularLinkedList balloons = new CircularLinkedList();
        
        for (int i = 1; i <= n; i++) {
            int value = Integer.parseInt(st.nextToken());
            balloons.add(i, value);
        }

        StringBuilder result = new StringBuilder();
        result.append(balloons.popCurrent()); // 첫 번째 풍선 제거
        
        while (!balloons.isEmpty()) {
            int move = balloons.getCurrentValue(); // 현재 풍선의 종이 값 가져오기
            result.append(" ").append(balloons.popMove(move));
        }

        System.out.println(result);
    }
}
