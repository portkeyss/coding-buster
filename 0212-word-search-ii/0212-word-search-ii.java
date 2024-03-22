public class Solution { 
    public static class TrieNode{ 
        char ch; 
        boolean completeWord;//whether the node itself is the last char of a word 
        TrieNode[] children; 
        public TrieNode(){ 
            ch = '\u0000'; 
            completeWord = false; 
            children = new TrieNode[26]; 
        } 
    } 
    public static class Trie { 
        TrieNode root;
        public Trie() { 
            root = new TrieNode(); 
        } 
        public void addWord(String word) { 
            int len = word.length(); 
            int i = 0; 
            TrieNode t = root; 
            while(i < len) { 
                int idx = word.charAt(i) - 'a'; 
                if(t.children[idx] != null) {t = t.children[idx];i++;}
                else break;
            } 
            while(i < len) { 
                TrieNode p = new TrieNode(); 
                p.ch = word.charAt(i);
                t.children[p.ch - 'a'] = p;
                t = p; i++;
            } 
            t.completeWord = true; 
        } 
    } 
    HashSet<String> wordsFound = new HashSet<String>(); 
    StringBuilder sb = new StringBuilder();
    Trie dict = new Trie(); 
    public List<String> findWords(char[][] board, String[] words) { 
        List<String> result = new LinkedList<String>(); 
        TrieNode root = dict.root;
        for(String word: words) dict.addWord(word); 
        int m = board.length; 
        if(m == 0) return result; 
        int n = board[0].length; 
        for(int i = 0; i < m; i++) { 
            for(int j = 0; j < n; j++) { 
                findWords(board,root,i,j); 
            } 
        } 
        for(String word:wordsFound) result.add(word); 
        return result; 
    } 
    private void findWords(char[][] board, TrieNode dict, int i, int j) { 
        if(board[i][j] == '\u0000' || dict.children[board[i][j] - 'a'] == null ) return;//note that the order in the if( a|| b) is crucial, if board[i][j] is set to '\u0000' it means deadend, and no computation based on alphabetical order does not apply
        sb.append(board[i][j]); dict = dict.children[board[i][j] - 'a'];
        if(dict.completeWord) {wordsFound.add(sb.toString()); }
        char temp = board[i][j]; 
        board[i][j] = '\u0000'; 
        if(i > 0) findWords(board,dict,i - 1,j);
        if(i < board.length - 1) findWords(board,dict,i + 1,j);
        if(j > 0) findWords(board,dict,i,j - 1); 
        if(j < board[0].length - 1) {findWords(board,dict,i,j + 1);}
        sb.setLength(Math.max(0,sb.length() -1));
        board[i][j] = temp;
    }
}