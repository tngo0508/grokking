class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        number_map = {
            '1': '',
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
            '0': '',
        }
        def backtrack(number_map, digits, result, index, curr):
            if index == len(digits):
                if curr:
                    result.append(curr[:])
                return

            digit = digits[index]
            for c in number_map[digit]:
                backtrack(number_map, digits, result, index + 1, curr + c)

        result = []
        backtrack(number_map, digits, result, 0, "")
        return result