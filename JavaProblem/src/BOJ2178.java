import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class BOJ2178 {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        Integer N = Integer.parseInt(st.nextToken());
        Integer M = Integer.parseInt(st.nextToken());
        int[][] board = new int[N][M];

        for (int i = 0; i < N; i++) {
            int token[] = Arrays.stream(br.readLine().split("")).mapToInt(Integer::parseInt).toArray();
            board[i] = token;
        }

        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (board[i][j] == 0) {
                    board[i][j] = -1;
                } else {
                    board[i][j] = 0;
                }
            }
        }

        // 시작 값.
        board[0][0] = 1;
        int[] dx = { 0, 0, 1, -1 };
        int[] dy = { 1, -1, 0, 0 };

        Queue<Pos> queue = new LinkedList<>();
        queue.offer(new Pos(0, 0, 1));

        while (!queue.isEmpty()) {
            Pos cur = queue.poll();

            int curVal = cur.val;
            for (int i = 0; i < 4; i++) {
                int dr = cur.r + dx[i];
                int dc = cur.c + dy[i];

                if (dr < 0 || dr >= N || dc < 0 || dc >= M) {
                    continue;
                }

                if (board[dr][dc] == 0) {
                    int newVal = curVal + 1;
                    board[dr][dc] = newVal;
                    queue.offer(new Pos(dr, dc, newVal));
                }

            }
        }
        System.out.println(board[N - 1][M - 1]);

    }

    static class Pos {

        int r;
        int c;
        int val;

        Pos(int r, int c, int val) {
            this.r = r;
            this.c = c;
            this.val = val;
        }
    }
}
