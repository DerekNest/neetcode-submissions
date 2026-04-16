class Solution {
    public int networkDelayTime(int[][] times, int n, int k) {
        // 1. Build the adjacency list
        // Map: Source Node -> List of {Target Node, Time}
        Map<Integer, List<int[]>> adj = new HashMap<>();
        for (int[] time : times) {
            adj.computeIfAbsent(time[0], x -> new ArrayList<>()).add(new int[]{time[1], time[2]});
        }

        // 2. Min-Heap stores {currentTime, currentNode}
        // Sorted by time (the first element in the array)
        PriorityQueue<int[]> pq = new PriorityQueue<>(Comparator.comparingInt(a -> a[0]));
        pq.add(new int[]{0, k});

        // 3. Distance map/array to keep track of shortest path to each node
        int[] dist = new int[n + 1];
        Arrays.fill(dist, Integer.MAX_VALUE);
        dist[k] = 0;

        while (!pq.isEmpty()) {
            int[] current = pq.poll();
            int d = current[0];
            int u = current[1];

            // Optimization: if we already found a shorter path to u, skip
            if (d > dist[u]) continue;

            if (!adj.containsKey(u)) continue;

            for (int[] edge : adj.get(u)) {
                int v = edge[0];
                int weight = edge[1];
                
                // If traveling to v via u is faster than the current known distance to v
                if (dist[u] + weight < dist[v]) {
                    dist[v] = dist[u] + weight;
                    pq.add(new int[]{dist[v], v});
                }
            }
        }

        // 4. Find the maximum time in our distance array
        int maxDelay = 0;
        for (int i = 1; i <= n; i++) {
            if (dist[i] == Integer.MAX_VALUE) return -1; // Node unreachable
            maxDelay = Math.max(maxDelay, dist[i]);
        }

        return maxDelay;
    }
}