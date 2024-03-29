# My solution
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        row, col = 0, 0
        hash_map = defaultdict(list)
        direction = -1
        for c in s:
            hash_map[row].append(c)
            if row == numRows - 1 or row == 0:
                direction *= -1
            row += direction


        res = []
        for i in range(len(hash_map)):
            res.extend(hash_map[i])

        return ''.join(res)
    
# Editorial Solution
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        answer = []
        n = len(s)
        chars_in_section = 2 * (numRows - 1)

        for curr_row in range(numRows):
            index = curr_row
            while index < n:
                answer.append(s[index])

                # If curr_row is not the first or last row,
                # then we have to add one more character of current section.
                if curr_row != 0 and curr_row != numRows - 1:
                    chars_in_between = chars_in_section - 2 * curr_row
                    second_index = index + chars_in_between

                    if second_index < n:
                        answer.append(s[second_index])
                # Jump to same row's first character of next section.
                index += chars_in_section

        return "".join(answer)