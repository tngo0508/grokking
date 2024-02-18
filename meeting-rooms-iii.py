# Brute force - accepted
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        rooms = [[] for _ in range(n)]

        for i, meeting in enumerate(meetings):
            start, end = meeting
            available_room = [float('inf'), []]
            for room in rooms:
                if not room:
                    available_room[0] = end
                    available_room[1] = room
                    break
                elif room and start >= room[-1]:
                    available_room[0] = room[-1]
                    available_room[1] = room
                    break
                elif room and available_room[0] > room[-1]:
                    available_room[0] = room[-1]
                    available_room[1] = room
                
            
            prev_end, curr = available_room
            if not room:
                curr.append(end)
            else:
                delays = prev_end - start if prev_end - start > 0 else 0
                curr.append(end + delays)

        rooms = list(map(len, rooms))
        res = [0, 0]
        for i, num_of_meetings in enumerate(rooms):
            if res[0] < num_of_meetings:
                res[0] = num_of_meetings
                res[1] = i
        
        return res[1]