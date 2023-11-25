def two_single_numbers(arr):
    bitwise_sum = 0

    for i in arr:
        bitwise_sum ^= i

    bitwise_mask = bitwise_sum & (-bitwise_sum)
    results = 0

    for i in arr:
        if bitwise_mask & i:
            results = results ^ i

    return [results, bitwise_sum ^ results]


# Driver code
def main():
    inputs_arr = [[1, 2, 2, 3],
             [4, 4, 3, 2, 3, 5],
             [1, 1, 7, 4, 5, 5, 8, 8],
             [1, 0], [9, 8, 8, 7, 6, 6, 4, 4]]

    for i in range(len(inputs_arr)):
        print(i + 1, ". \t Input list: ", inputs_arr[i], sep="")
        print("\t Two Singles numbers in a list: ",
              two_single_numbers(inputs_arr[i]), sep="")
        print("-" * 100)


if __name__ == '__main__':
    main()