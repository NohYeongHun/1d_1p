import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.HashMap;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.Map;
import java.util.Queue;
import java.util.Set;
import java.util.StringTokenizer;

public class BOJ1389 {

    static Integer MIN = Integer.MAX_VALUE;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        Integer N = Integer.parseInt(st.nextToken());
        Integer M = Integer.parseInt(st.nextToken());

        // 어떤 리스트에 어떤게 연결되어 있는지
        Map<Integer, Set<Integer>> map = new HashMap<>();
        int[][] distance = new int[101][5001];
        boolean[][] visited = new boolean[101][50001];
        for (int i = 1; i <= 100; i++) {
            map.put(i, new HashSet<>());
            distance[i][i] = 1;
            visited[i][i] = true;
        }

        for (int i = 1; i <= M; i++) {
            st = new StringTokenizer(br.readLine());
            Integer A = Integer.parseInt(st.nextToken());
            Integer B = Integer.parseInt(st.nextToken());
            map.get(A).add(B);
            map.get(B).add(A);
        }

        for (int cur = 1; cur <= N; cur++) {
            Queue<Integer> q = new LinkedList<>();

            for (int val : map.get(cur)) {
                q.add(val);
                visited[cur][val] = true;
                distance[cur][val] = 2;
            }

            while (!q.isEmpty()) {
                int node = q.poll();

                for (int nextNode : map.get(node)) {
                    int prevCost = distance[cur][node];

                    if (visited[cur][nextNode]) {
                        continue;
                    }

                    if (distance[cur][nextNode] != 0) {
                        distance[cur][nextNode] = Math.min(prevCost + 1, distance[cur][nextNode]);
                    } else {
                        distance[cur][nextNode] = prevCost + 1;
                    }
                    visited[cur][nextNode] = true;
                    q.add(nextNode);
                }
            }
        }

        Integer answer = -1;
        // 이동할 다음노드, 비용
        for (int node = 1; node <= N; node++) {
            Integer val = 0;
            for (int nextNode = 1; nextNode <= N; nextNode++) {
                val += distance[node][nextNode];
            }
            val -= N;

            if (val < MIN) {
                answer = node;
                MIN = val;
            }

        }
        System.out.println(answer);
    }

}
