class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned_set = set(banned)
        words = paragraph.lower()
        words = re.sub(r"[!?',;.]", " ", words)
        words = words.split()
        counter = Counter(words)
        result = ""
        max_freq = 0
        for word, count in counter.items():
            if word not in banned:
                if max_freq < count:
                    result = word
                    max_freq = count
        
        return result
