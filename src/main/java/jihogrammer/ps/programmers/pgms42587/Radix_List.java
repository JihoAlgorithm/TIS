package jihogrammer.ps.programmers.pgms42587;

import java.util.ArrayList;
import java.util.List;

public class Radix_List {

    public static void main(String[] args) {

        System.out.println(new Radix_List().solution(new int[] {2, 1, 3, 2}, 2));
        System.out.println(new Radix_List().solution(new int[] {1, 1, 9, 1, 1, 1}, 0));

    }

    public int solution(int[] priorities, int location) {

        int answer = 1;
        List<List<Integer>> buckets = new ArrayList<>();
        List<Integer> preBucket = null;

        for (int i = 0; i < 9; i++) buckets.add(new ArrayList<>());

        for (int i = 0; i < priorities.length; i++)
            buckets.get(9 - priorities[i]).add(i);

        int index = -1;
        for (List<Integer> bucket : buckets) {
            index++;
            if (bucket.isEmpty()) continue;
            if (bucket.contains(location))
                return bucket.indexOf(location) + 1;
            preBucket = buckets.remove(index);
            break;
        }

        answer += preBucket.size();

        for (List<Integer> bucket : buckets) {
            if (bucket.isEmpty()) continue;

            int size = bucket.size();
            int key = preBucket.get(preBucket.size() - 1);
            int pivot = upperBound(key, bucket, 0, size);
            preBucket = bucket.subList(pivot, size);
            preBucket.addAll(bucket.subList(0, pivot));

            if (preBucket.contains(location)) {
                answer += preBucket.indexOf(location);
                break;
            }

            answer += preBucket.size();

        }

        return answer;

    }

    private int upperBound(int key, List<Integer> list, int l, int r) {
        int m;
        while (l < r)
            if (list.get(m = l + r >> 1) > key) r = m;
            else l = m + 1;
        return r;
    }

}
