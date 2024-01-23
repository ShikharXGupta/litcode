class Solution:
    def maxLength(self, arr: List[str]) -> int:
        n = len(arr)
        res = [""]
        output = 0
        for word in arr:
            for r in res:
                new_r = r+word
                if len(new_r) != len(set(new_r)): continue
                res.append(new_r)
                output = max(output, len(new_r))
        return output