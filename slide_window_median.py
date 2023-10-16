from heapq import heappop, heappush, heapify


def median_sliding_window(nums, k):
    # To store the medians
    medians = []

    # To keep track of the numbers that need to be removed from the heaps
    outgoing_num = {}

    # Max heap
    small_list = []

    # Min heap
    large_list = []

    # Initialize the max heap by multiplying each element by -1
    for i in range(0, k):
        heappush(small_list, -1 * nums[i])

    # Transfer the top 50% of the numbers from max heap to min heap
    # while restoring the sign of each number
    for i in range(0, k//2):
        element = heappop(small_list)
        heappush(large_list, -1 * element)

    # Variable to keep the heaps balanced
    balance = 0

    i = k
    while True:
        # If the window size is odd
        if (k & 1) == 1:
            medians.append(float(small_list[0] * -1))
        else:
            medians.append((float(small_list[0] * -1) + float(large_list[0])) * 0.5)

        # Break the loop if all elements have been processed
        if i >= len(nums):
            break

        # Outgoing number
        out_num = nums[i - k]

        # Incoming number
        in_num = nums[i]
        i += 1

        # If the outgoing number is from max heap
        if out_num <= (small_list[0] * -1):
            balance -= 1
        else:
            balance += 1

        # Add/Update the outgoing number in the hash map
        if out_num in outgoing_num:
            outgoing_num[out_num] = outgoing_num[out_num] + 1
        else:
            outgoing_num[out_num] = 1

        # If the incoming number is less than the top of the max heap, add it in that heap
        # Otherwise, add it in the min heap
        if small_list and in_num <= (small_list[0] * -1):
            balance += 1
            heappush(small_list, in_num * -1)
        else:
            balance -= 1
            heappush(large_list, in_num)

        # Re-balance the heaps
        if balance < 0:
            heappush(small_list, (-1 * large_list[0]))
            heappop(large_list)
        elif balance > 0:
            heappush(large_list, (-1 * small_list[0]))
            heappop(small_list)

        # Since the heaps have been balanced, we reset the balance variable to 0. 
        # This ensures that the two heaps contain the correct elements for the calculations to be performed on the elements in the next window.
        balance = 0

        # Remove invalid numbers present in the hash map from top of max heap
        while (small_list[0] * -1) in outgoing_num and (outgoing_num[(small_list[0] * -1)] > 0):
            outgoing_num[small_list[0] * -1] = outgoing_num[small_list[0] * -1] - 1
            heappop(small_list)

        # Remove invalid numbers present in the hash map from top of min heap
        while large_list and large_list[0] in outgoing_num and (outgoing_num[large_list[0]] > 0):
            outgoing_num[large_list[0]] = outgoing_num[large_list[0]] - 1
            heappop(large_list)

    return medians


def main():
    input = (
            ([3, 1, 2, -1, 0, 5, 8],4), 
            ([1, 2], 1), 
            ([4, 7, 2, 21], 2), 
            ([22, 23, 24, 56, 76, 43, 121, 1, 2, 0, 0, 2, 3, 5], 5), 
            ([1, 1, 1, 1, 1], 2))
    x = 1
    for i in input:
        print(x, ".\tInput array: ", i[0],  ", k = ", i[1], sep = "")
        print("\tMedians: ", median_sliding_window(i[0], i[1]), sep = "")
        print(100*"-", "\n", sep = "")
        x += 1


if __name__ == "__main__":
    main()