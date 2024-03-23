class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        res = []
        
        matched = True
        
        sourceIt = iter(source)
        line = next(sourceIt, None)
        st = ""
        
        while line is not None: #note that to differeniate btw empty string and no string, we have to state here explicitly
            #find the indices of the first occuring special symbols
            i1 = line.find('//')
            i2 = line.find('/*')
            i3 = line.find('*/')
            
            # highest priority in a line, must be taken first
            if not matched: # a previous line contains /* that was not matched
                if i3 < 0: # */ does not exist in current "partial" line                
                    line = next(sourceIt, None)                    
                else:
                    line = line[i3+2:] 
                    matched = True
                    
            elif i1 >= 0 and (i1 < i2 or i2 < 0) and (i1 < i3 or i3 < 0): #  // is the first special symbol
                st += line[:i1]
                if st != "":
                    res.append(st)
                st = ""
                line = next(sourceIt, None)
                
                      
            elif i2 >= 0 and (i2 < i1 or i1 < 0) and (i2 < i3 or i3 < 0): #  /* is the first special symbol
                matched = False
                st += line[:i2]
                line = line[i2+2:]
                
            elif i3 >= 0 and (i3 < i1 or i1 < 0) and (i3 < i2 or i2 < 0): #  */ is the first special symbol
                st += line[:i3+1]
                line = line[i3+1:]
                
            else: # no special symbols are found in the line
                st += line
                if st != "":
                    res.append(st)
                st = ""
                line = next(sourceIt, None)
                   
        return res
                
                