class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_mapS={}
        hash_mapT={}
        
        i=0
        for letter in s:
            hash_mapS[i]=letter
            i+=1

        j=0
        for letter in t:
            hash_mapT[j]=letter
            j+=1
        
        i=0
        while i<len(s):
            if hash_mapS[i] in hash_mapT.values():
               for j in range(len(t)):
                    try: 
                        if(hash_mapT[j]==hash_mapS[i]):
                            del hash_mapT[j]
                            break
                    except:
                        pass
               del hash_mapS[i]
               i+=1
            else:
                return False
        if len(hash_mapS)==0 and len(hash_mapT)==0:
            return True        
        return False