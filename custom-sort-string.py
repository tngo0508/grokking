# My solution
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        res = []
        in_order = defaultdict(int)
        out_order = []
        for c in s:
            if c in order:
                in_order[c] += 1
            else:
                out_order.append(c)
        
        for c in order:
            if c in in_order:
                res.append(c * in_order[c])
        
        res.extend(out_order)
        return ''.join(res)