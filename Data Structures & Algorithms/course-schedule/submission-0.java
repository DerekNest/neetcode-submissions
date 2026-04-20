class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        int[] inDeg = new int[numCourses];
        List<List<Integer>> adj = new ArrayList<>();
        for (int i=0; i <numCourses; i++) {
            adj.add(new ArrayList<>());
        }
        for (int[] p : prerequisites) {
            adj.get(p[1]).add(p[0]);
            inDeg[p[0]]++;
        }
        Queue<Integer> q = new LinkedList<>();
        for (int i=0; i<numCourses;i++) if (inDeg[i] ==0) q.add(i);
        int[] order = new int[numCourses];
        int idx=0;
        while(!q.isEmpty()) {
            int u = q.poll();
            order[idx++] = u;
            for(int v:adj.get(u)) if (--inDeg[v]==0) q.add(v);

        } return idx == numCourses;
    }
}
