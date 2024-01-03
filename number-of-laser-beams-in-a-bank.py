from collections import Counter

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        result = 0
        queue = deque([0])
        while queue:
            level = queue.popleft()
            level_count = Counter(bank[level])
            next_level = level + 1
            for i in range(level + 1, len(bank)):
                if '1' in bank[i]:
                    next_level = i
                    break
            
            if next_level < len(bank):
                next_level_count = Counter(bank[next_level])
                result += (level_count['1'] * next_level_count['1'])
                queue.append(next_level)
        
        return result