class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack = []
        result = [0] * n
        for log in logs:
            func_id, tag, timestamp = log.split(':')
            timestamp = int(timestamp)
            func_id = int(func_id)
            if tag == 'start':
                stack.append([func_id, timestamp])
                prev_time = 0
            else:
                curr_id, curr_timestamp = stack.pop()
                time = timestamp - curr_timestamp + 1
                result[curr_id] += time - prev_time
                if stack:
                    top_id, top_timestamp = stack[-1]
                    result[top_id] -= time
        return result