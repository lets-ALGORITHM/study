import java.io.*;
import java.util.*;

/*
 * [구현]
 * 1. 방에 최대 인원 m명이 꽉 차면 게임 시작
 * 2. 방에 입장하려면 
 * 2.1. 해당 방 최초 입장 플레이어의 레벨 +- 10 내여야 함
 * 2.2. 해당 방의 인원이 꽉 차지 않아야 함
 * 
 * 출력 시에는 생성된 방 순서대로, 방 안에서는 플레이어 닉네임 사전순대로
 * 
 * 1) LinkedHashMap을 요소로 가지는 List를 통해 방들과 방 안의 플레이어들을 관리
 * 2) 2.1과 2.2를 만족하는지 확인 후 방에 추가하거나 새로운 방을 생성해 해당 방에 추가
 * 
 * 다만 플레이어 정보를 LinkedHashMap으로 관리하기보다는,
 * 새로운 Player 클래스를 만들어 관리하는 게 더 빨랐을 듯
 */
public class b20006 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int p = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        // 방과 해당 방 안의 플레이어 정보를 담을 리스트
        List<LinkedHashMap<String, Integer>> rooms = new ArrayList<>();

        // 플레이어마다 돌면서 방에 집어넣기
        for (int i = 0; i < p; i++) {
            st = new StringTokenizer(br.readLine());
            int l = Integer.parseInt(st.nextToken());
            String n = st.nextToken();

            boolean ok = false; // 지금 있는 방에 집어넣었는가?
            // 일단 지금 있는 방들 돌아보기
            for (int j = 0; j < rooms.size(); j++) {
                LinkedHashMap<String, Integer> nowRoom = rooms.get(j);
                if (levelAvailable(l, nowRoom.values().iterator().next())) {
                    if (nowRoom.size() < m) {
                        nowRoom.put(n, l);
                        ok = true;
                        break;
                    }
                }
            }

            if (!ok) { // 지금 있는 방에 못 집어넣었으면 새로운 방 생성해서 넣자
                rooms.add(new LinkedHashMap<>());
                rooms.get(rooms.size() - 1).put(n, l);
            }
        }

        for (int i = 0; i < rooms.size(); i++) {
            LinkedHashMap<String, Integer> nowRoom = rooms.get(i);
            if (nowRoom.size() == m) {
                bw.write("Started!\n");
            } else {
                bw.write("Waiting!\n");
            }
            // 닉네임 기준 정렬
            nowRoom.entrySet().stream()
                .sorted(Map.Entry.comparingByKey())
                .forEach(entry -> {
                    try {
                        bw.write(entry.getValue() + " " + entry.getKey() + "\n");
                    } catch (IOException e) {
                        e.printStackTrace();
                    }
                });
        }

        bw.flush();
        bw.close();
    }

    // 새로운 플레이어가 현재 존재하는 방에 들어갈만큼 레벨 충족하는가?
    static boolean levelAvailable(int player, int room) {
        return player <= room + 10 && player >= room - 10;
    }
}