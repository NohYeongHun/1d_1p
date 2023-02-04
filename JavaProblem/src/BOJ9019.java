import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class BOJ9019 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int T = sc.nextInt();

        for (int i = 1; i <= T; i++) {
            int A = sc.nextInt(), B = sc.nextInt();
            boolean[] visited = new boolean[10000];
            visited[A] = true;

            Queue<Calc> queue = new LinkedList<>();
            queue.add(new Calc(A, ""));

            while (!queue.isEmpty()) {
                Calc cur = queue.poll();

                if (cur.num == B) {
                    System.out.println(cur.cmd);
                    break;
                }

                if (!visited[cur.D()]) {
                    queue.add(new Calc(cur.D(), cur.cmd + "D"));
                    visited[cur.D()] = true;
                }
                if (!visited[cur.S()]) {
                    queue.add(new Calc(cur.S(), cur.cmd + "S"));
                    visited[cur.S()] = true;
                }
                if (!visited[cur.L()]) {
                    queue.add(new Calc(cur.L(), cur.cmd + "L"));
                    visited[cur.L()] = true;
                }
                if (!visited[cur.R()]) {
                    queue.add(new Calc(cur.R(), cur.cmd + "R"));
                    visited[cur.R()] = true;
                }
            }
        }

        sc.close();
    }

    static class Calc {
        int num;
        String cmd;

        Calc(int num, String cmd) {
            this.num = num;
            this.cmd = cmd;
        }

        int D() {
            return (num * 2) % 10000;
        }

        int S() {
            return num == 0 ? 9999 : num - 1;
        }

        int L() {
            return num % 1000 * 10 + num / 1000;
        }

        int R() {
            return num % 10 * 1000 + num / 10;
        }
    }
}
