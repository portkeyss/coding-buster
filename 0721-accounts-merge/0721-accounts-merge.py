class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:        
        idxToSet = {} #idx map to emails      
        for i,account in enumerate(accounts):
            curEmails = set(account[1:])
            newSet = curEmails.copy()
            delkeys = set() #previous keys for set that is to be merged into the newSet
            for j, jsEmails in idxToSet.items():
                if jsEmails & curEmails: #check if two sets have common elements
                    delkeys.add(j)
                    newSet.update(jsEmails)
            for key in delkeys:
                idxToSet.pop(key, None)

            idxToSet[i] = newSet

        res = []
        for idx, emls in idxToSet.items():
            acct = []
            acct.append(accounts[idx][0])
            acct.extend(sorted(emls))
            res.append(acct)
        return res                