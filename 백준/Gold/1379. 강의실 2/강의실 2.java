import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.*;

import static java.lang.Integer.parseInt;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = parseInt(br.readLine());
        Map<Integer, Integer> map = new HashMap<>();
        PriorityQueue<Lecture> pq = new PriorityQueue<>(Comparator.comparingInt(l -> l.start));

        StringTokenizer st;
        int num, start, end;
        while (N-- > 0) {
            st = new StringTokenizer(br.readLine());
            num = parseInt(st.nextToken());
            start = parseInt(st.nextToken());
            end = parseInt(st.nextToken());
            map.put(num, -1);

            pq.offer(new Lecture(num, start, end));
        }

        int count = 0;
        PriorityQueue<Lecture> pq2 = new PriorityQueue<>(Comparator.comparingInt(l -> l.end));

        while (!pq.isEmpty()) {
            Lecture l = pq.poll();

            if (pq2.isEmpty()) {
                pq2.offer(l);
                count++;
                map.put(l.idx, count);
                continue;
            }

            if (pq2.peek().end > l.start) {
                count++;
                map.put(l.idx, count);
            } else {
                map.put(l.idx, map.get(pq2.poll().idx));
            }

            pq2.offer(l);
        }

        System.out.println(count);
        List<Map.Entry<Integer, Integer>> collect = new ArrayList<>(map.entrySet());
        collect.sort(Comparator.comparingInt(Map.Entry::getKey));
        for (Map.Entry<Integer, Integer> entry : collect) {
            System.out.println(entry.getValue());
        }
        br.close();
    }


    static class Lecture {
        int idx, start, end;

        public Lecture(int idx, int start, int end) {
            this.idx = idx;
            this.start = start;
            this.end = end;
        }
    }
}