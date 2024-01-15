class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        players = defaultdict(list)
        for match in matches:
            w, l = match
            if w not in players:
                players[w].append(0)
                players[w].append(0)

            if l not in players:
                players[l].append(0)
                players[l].append(0)

        for match in matches:
            w, l = match
            players[w][0] += 1
            players[l][1] += 1

        player_id = players.keys()
        no_lost = []
        lost_one = []
        for p in sorted(player_id):
            if players[p][1] == 0:
                no_lost.append(p)
            if players[p][1] == 1:
                lost_one.append(p)
            
        return [no_lost, lost_one]
