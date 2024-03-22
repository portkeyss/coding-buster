public class WordDictionary {
    public static class TrieNode {
        char ch;
        boolean isDictionaryWord;//an indication of whether this TrieNode itself is an end for a dictionary word, besides being a prefix
        LinkedList<TrieNode> children;
        public TrieNode (char ch){
            this.ch = ch;
            isDictionaryWord = false;
            children = new LinkedList<TrieNode>();
        }
    }
    TrieNode root = new TrieNode('\u0000');
    // Adds a word into the data structure.
    public void addWord(String word) {
        TrieNode t = root;
        int idx = 0, len = word.length();
        while(idx < len) {
            boolean flag = false;
            for(TrieNode child: t.children) {
                if(word.charAt(idx) == child.ch) {idx++;t = child; flag = true;break;}
            }
            if(!flag) {
                while(idx < len) {
                    TrieNode p = new TrieNode(word.charAt(idx));
                    t.children.add(p);
                    t = p;idx++;
                }
                break;
            }
        }
        t.isDictionaryWord = true;
    }

    // Returns if the word is in the data structure. A word could
    // contain the dot character '.' to represent any one letter.
    public boolean search(String word) {
        return search(word, root);
    }
    
    private boolean search(String word, TrieNode rootOfSubTrie) {
        if(word.length() == 0) return rootOfSubTrie.isDictionaryWord;
        if(word.charAt(0) == '.') {
            for(TrieNode child: rootOfSubTrie.children) {
                if(search(word.substring(1), child)) return true;
            }
            return false;
        }else {
            TrieNode t = rootOfSubTrie; int i = 0;
            while(i < word.length() && word.charAt(i) != '.') {
                char c = word.charAt(i);
                boolean flag = false;
                for(TrieNode child: t.children) {
                    if(c == child.ch) {t = child; i++; flag = true; break;}
                }
                if(!flag) return false;
            }
            return search(word.substring(i), t);
        }
    }
}

// Your WordDictionary object will be instantiated and called as such:
// WordDictionary wordDictionary = new WordDictionary();
// wordDictionary.addWord("word");
// wordDictionary.search("pattern");