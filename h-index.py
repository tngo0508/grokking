class Solution:
    def hIndex(self, citations: List[int]) -> int:
        res = 0
        citations.sort()
        N = len(citations)
        papers = 0
        for i in reversed(range(N)):
            if citations[i] > papers:
                papers += 1
            if papers <= citations[i]:
                res = max(res, papers)
        return res