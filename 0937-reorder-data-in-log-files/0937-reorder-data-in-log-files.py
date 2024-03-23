class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def getkey(log):
            _id, msg = log.split(" ",maxsplit = 1)
            return (-1, msg, _id) if msg[0].isalpha() else (0,) #msg may contain alphabets and spaces, so we write msg[0] to form the correct condition
        return sorted(logs,key=getkey)