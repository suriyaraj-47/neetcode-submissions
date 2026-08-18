class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        map={}
        for words in strs:
            count=[0]*26
            for char in words:

                count[ord(char)-ord('a')]+=1

            key=tuple(count)

            if key not in map:
                map[key]=[]
            map[key].append(words)
        return (list(map.values()))


        