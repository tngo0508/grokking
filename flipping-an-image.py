class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        n = (len(image) + 1) // 2
        for row in image:
            for i in range(n):
                row[i], row[~i] = row[~i] ^ 1, row[i] ^ 1
                print(i, ~i)
        return image
    
# solution
def flip_and_invert_image(image):
    row_count = len(image)
    mid = (row_count + 1) // 2
    
    for row in image:
        for i in range(mid):
            temp = row[i] ^ 1
            row[i] = row[len(row) - 1 - i] ^ 1
            row[len(row) - 1 - i] = temp
    
    return image


# Driver code
def main():
    inputs = [
                [[1, 1, 0],
                 [1, 0, 1],
                 [0, 0, 0]],

                [[1, 1, 0, 0],
                 [1, 0, 0, 1],
                 [0, 1, 1, 1],
                 [1, 0, 1, 0]],

                [[1, 1, 0, 0, 1],
                 [1, 0, 0, 1, 0],
                 [0, 1, 1, 1, 1],
                 [0, 0, 1, 1, 0],
                 [1, 0, 1, 0, 0]],

                [[0, 0, 1],
                 [1, 0, 1],
                 [0, 1, 0]],

                [[1, 1, 1],
                 [0, 0, 0],
                 [1, 1, 1]]
    ]

    for i in range(len(inputs)):
        print(i + 1, ".\t Original image: ", inputs[i], sep="")
        print("\t Flipped and inverted image: ", ": ",
              flip_and_invert_image(inputs[i]), sep="")
        print("-" * 100)


if __name__ == "__main__":
    main()
