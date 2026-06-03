from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict= defaultdict(list)

        for s in strs:
            key = tuple(sorted(s))
            my_dict[key].append(s)
        return list(my_dict.values())





        