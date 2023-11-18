class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def sort_letter_log(log):
            log_list = log.split()
            return log_list[1:], log_list[0]


        letter_logs = []
        digit_logs = []
        for log in logs:
            log_list = log.split()
            content = log_list[1]
            if content.isdigit():
                digit_logs.append(log)
            else:
                letter_logs.append(log)
        
        letter_logs.sort(key=sort_letter_log)
        letter_logs.extend(digit_logs)
        return letter_logs
        
# leetcode solution
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:

        def get_key(log):
            _id, rest = log.split(" ", maxsplit=1)
            return (0, rest, _id) if rest[0].isalpha() else (1, )

        return sorted(logs, key=get_key)