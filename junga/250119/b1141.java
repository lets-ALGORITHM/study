import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;

public class b1141 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());
        Trie trie = new Trie();

        for (int i=0;i<n;i++) {
            trie.insert(br.readLine());
        }

        System.out.println(trie.countLeafNodes());
    }

    static class TrieNode {
        char value;
        HashMap<Character, TrieNode> children;

        public TrieNode(char value) {
            this.value = value;
            this.children = new HashMap<>();
        }
    }

    static class Trie {
        TrieNode root;

        public Trie() {
            root = new TrieNode('\0');
        }

        public void insert(String word) {
            TrieNode current = root;
            for (char ch : word.toCharArray()) {
                current.children.putIfAbsent(ch, new TrieNode(ch));
                current = current.children.get(ch);
            }
        }

        public int countLeafNodes() {
            return countLeafNodesRecursive(root);
        }

        public int countLeafNodesRecursive(TrieNode node) {
            if (node == null) {
                return 0;
            }

            int cnt = 0;
            if (node.children.isEmpty()) {
                cnt++;
            }

            for (TrieNode child : node.children.values()) {
                cnt += countLeafNodesRecursive(child);
            }

            return cnt;
        }
    }
}
