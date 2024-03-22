public class Solution {
    public int computeArea(int A, int B, int C, int D, int E, int F, int G, int H) {
        int area = (C - A) * (D - B) + (G - E) * (H - F);
        if(G < A || C < E || H < B || D < F) return area;//No overlap
        int overlap = (Math.min(C,G) - Math.max(A,E)) * ( Math.min(D,H) - Math.max(B,F));
        return area - overlap;
    }
}