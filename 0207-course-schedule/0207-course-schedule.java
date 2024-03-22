public class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        //build adjacency list 
        ArrayList<LinkedList<Integer>> adjacencyList = new ArrayList<LinkedList<Integer>>(); 
        for(int i = 0; i < numCourses; i++) { 
            LinkedList<Integer> list = new LinkedList<Integer>(); 
            adjacencyList.add(list); 
        } 
        for(int i = 0; i < prerequisites.length; i++) { 
            adjacencyList.get(prerequisites[i][1]).add(prerequisites[i][0]); 
        } 
         
        //build a in-degree array 
        int[] inDegree = new int[numCourses]; 
        for(int i = 0; i < numCourses; i++) { 
            for(int j: adjacencyList.get(i)) inDegree[j]++;
        } 
         LinkedList<Integer> zeroInDegreeQueue = new LinkedList<Integer>(); 
        for(int i = 0; i < numCourses; i++) if(inDegree[i] == 0) zeroInDegreeQueue.addLast(i); 
         
        int cnt = 0; 
        while(!zeroInDegreeQueue.isEmpty()) { 
            int j = zeroInDegreeQueue.pollFirst(); 
            for(int k: adjacencyList.get(j)) {inDegree[k]--; if(inDegree[k] == 0) zeroInDegreeQueue.addLast(k);} 
            cnt++; 
        }  
        return cnt == numCourses; 
    } 
}