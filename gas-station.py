# Brute Force - TLE
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) - sum(cost) < 0:
            return -1
        diff = []
        stations = len(gas)
        for i in range(stations):
            diff.append(gas[i] - cost[i])
        
        for i in range(stations):
            curr = i
            d = 0
            while d >= 0:
                d += diff[curr]
                curr = (curr + 1) % stations
                if curr == i:
                    return i
                
# Editorial Solution
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_gain = 0
        curr_gain = 0
        answer = 0
        
        for i in range(len(gas)):
            # gain[i] = gas[i] - cost[i]
            total_gain += gas[i] - cost[i]
            curr_gain += gas[i] - cost[i]

            # If we meet a "valley", start over from the next station
            # with 0 initial gas.
            if curr_gain < 0:
                curr_gain = 0
                answer = i + 1
        
        return answer if total_gain >= 0 else -1