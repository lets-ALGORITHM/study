import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.IOException;

/*
 * [구현]
 * 1. k번째만큼 next 걸고 해당 원소 삭제하는 메소드 가지는 세미 원형 연결 리스트..? 구현
 */

public class b11866 {
    private static int k;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

        String[] input = br.readLine().split(" ");
        int n = Integer.parseInt(input[0]);
        k = Integer.parseInt(input[1]);
        
        Circle list = new Circle();
        for (int i=1;i<=n;i++) {
            list.add(i);
        }

        bw.write("<");
        list.deleteKthNode(k, bw);
        bw.write(">");
        bw.flush();
        br.close();
        bw.close();
    }

    public static class Circle {
        private Node head;
        private Node tail;
        private Node current; // 현재 위치한 노드 정보

        private class Node {
            int data;
            Node next;

            Node(int data) {
                this.data = data;
            }
        }

        public boolean isEmpty() {
            return head == null;
        }

        public void add(int data) {
            Node newNode = new Node(data);
            if (isEmpty()) {
                head = newNode;
                tail = newNode;
                tail.next = head;
            } else {
                tail.next = newNode;
                tail = newNode;
                tail.next = head;
            }
        }

        // 1번째 노드부터 시작해 k번째 노드들 출력/삭제해가며 조회
        public void deleteKthNode(int k, BufferedWriter bw) throws IOException {
            if (isEmpty() || k <= 0) return;

            current = head;
            Node prev = tail;

            while (head != tail) {
                for (int i=1;i<k;i++) { // k번째 뒤 노드로 이동
                    prev = current;
                    current = current.next;
                }
                bw.write(current.data + ", ");
                // 현재 노드가 head, tail, 그 외인지에 따라 노드 삭제
                if (current == head) {
                    head = head.next;
                    tail.next = head;
                } else if (current == tail) {
                    tail = prev;
                    tail.next = head;
                } else {
                    prev.next = current.next;
                }
                current = current.next;
            }
            bw.write(current.data + "");
        }
    }
}
