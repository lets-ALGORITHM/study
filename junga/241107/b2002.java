import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException; 
import java.util.List;
import java.util.ArrayList;

public class b2002 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        List<String> in = new ArrayList<>(), out = new ArrayList<>();
        
        for (int i=0;i<n;i++) {
            in.add(br.readLine());
        }
        for (int i=0;i<n;i++) {
            out.add(br.readLine());
        }

        int overtakes = 0;
        for (int i=0;i<n;i++) {
            String temp = out.remove(0);
            if (!temp.equals(in.get(0))) {
                overtakes++;
            }
            in.remove(temp);
        }
        System.out.println(overtakes);
    }
}
