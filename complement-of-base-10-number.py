class Solution:
    def bitwiseComplement(self, num: int) -> int:
        temp = 1
        result = 0
        for _ in range(num.bit_length() - 1):
            temp |= temp << 1
        return num ^ temp
    

# SOLUTION
from math import log2, floor


def find_bitwise_complement(num):
    if num == 0:
        return 1

    bit_count = floor(log2(num)) + 1
    all_bits_set = pow(2, bit_count) - 1
    return num ^ all_bits_set


# driver code
def main():

    decimal_values = [42, 233, 100, 999999, 54]

    for i in range(len(decimal_values)):
        print(i + 1, ".\t Input: ", decimal_values[i], sep="")
        print(f'\t Bitwise complement of {decimal_values[i]} is: ', find_bitwise_complement(decimal_values[i]), sep="")
        print("-" * 100)


if __name__ == '__main__':
    main()
