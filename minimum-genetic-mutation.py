# My solution - BFS - accepted
class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        queue = deque()
        queue.append([startGene, 0])
        visited = set()
        N = len(startGene)
        while queue:
            node, mutations = queue.popleft()
            for i in range(N):
                gene_str_list = list(node)
                for c in ['A', 'C', 'G', 'T']:
                    if c != gene_str_list[i]:
                        gene_str_list[i] = c
                        new_gene = ''.join(gene_str_list)
                        if new_gene == endGene and new_gene in bank:
                            return mutations + 1
                        
                        if new_gene not in visited:
                            if new_gene in bank:
                                visited.add(new_gene)
                                queue.append([new_gene, mutations + 1])
        
        return -1