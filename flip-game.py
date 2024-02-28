# My solution
class Solution:
    def generatePossibleNextMoves(self, currentState: str) -> List[str]:
        N = len(currentState)
        res = []
        
        for i in range(N):
            curr = list(currentState)
            if curr[i] == '+':
                if i + 1 < N and curr[i] == '+' and curr[i+1] == '+':
                    curr[i] = '-'
                    curr[i+1] = '-'
                    res.append(''.join(curr))
                
        return res
    
# Editorial Soluion
class Solution:
    def generatePossibleNextMoves(self, currentState: str) -> List[str]:
        # List to store all possible next states after making one move.
        next_possible_states = []

        # Iterate through the 'currentState' string characters from left to right.
        for index in range(len(currentState) - 1):
            # If two adjacent characters of the 'currentState' string are '+', 
            # replace them with '-' and store the new state string.
            if currentState[index] == '+' and currentState[index + 1] == '+':
                next_state = currentState[:index] + "--" + currentState[index + 2:]
                next_possible_states.append(next_state)

        # Return 'next_possible_states' list.
        return next_possible_states