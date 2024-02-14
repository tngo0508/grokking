class Solution:
    def intToRoman(self, num: int) -> str:
        hash_map = {
            1: 'I',
            5: 'V',
            10: 'X',
            50: 'L',
            100: 'C',
            500: 'D',
            1000: 'M',
            4: 'IV',
            9: 'IX',
            40: 'XL',
            90: 'XC',
            400: 'CD',
            900: 'CM'
        }
        values = sorted(hash_map.keys())
        res = []
        while num > 0:
            i = 0
            k = values[0]
            while i < len(values) and num >= values[i]:
                k = values[i]
                i += 1

            num -= k            
            res.append(hash_map[k])

        return ''.join(res)   