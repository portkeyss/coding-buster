public class Solution {
    public String reverseWords(String s) {
        char[] str = s.toCharArray();
        
        if( str.length == 0 ) return "";
        
        int i, start, end;
        
        //find the starting char
        for(i = 0; i < str.length; i++) {
            if(str[i] != ' ') break;
        }
        start = i;
        
        //find the ending char
        for(i = str.length-1; i >= 0; i--) {
            if(str[i] != ' ') break;
        }
        end = i;
         
        if( start > end ) return ""; //all the characters are spaces and start==str.length
             // end == -1. Both of them are one step of the bounds
             // meaning start go cross the final bound without finding a non space char
            //  and end go cross the starting bound without finding a non space char
        
        // squeeze out the extra spaces, retaining the start cursor, while shifting
        // end towards the start. It is done via copying all the char to the
        // designated position. Note that it is in place, the cursor in the orginal array
        // always equal or goes after the cursor in the new array
        int k = start;
        for(i = start; i <= end; i++){
            if(str[i] == ' ') {
                str[k++] = str[i];
            }
            while(str[i] == ' '){
            i++;
            }
            if(str[i] != ' ') str[k++] = str[i];         
        }
        
        end = k-1;
                
        //begin first stage naive reverse, reverse all the charactors
        reverseWord(str, start, end); 
            
        //second stage reverse, reversing back each individual word
        int j = start;
        while ( j<= end) {
         k=j; 
         while(k<= end && str[k] != ' ') k++;//Note that the k<=end must be placed before
                                             //str[k] != ' ', to avoid outofbound str[k]
                 reverseWord(str, j,k-1);
                 j = k+1;
        }
  
       return new String(str, start, end-start+1); 
        } 
    
    //Note that it is an in place reverse
     private static void reverseWord(char[] str, int start, int end){ 
         if( start > end ) return;
         int i = start; 
         int j = end; 
         while(i <= j){             
             char temp = str[i]; 
             str[i] = str[j]; 
             str[j] = temp; 
             i++; 
             j--; 
         } 
      }
    
}