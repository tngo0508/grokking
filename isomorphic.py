def is_isomorphic(string1, string2):
    m1 = {}
    m2 = {}
    for c1, c2 in zip(string1, string2):
        if c1 in m1 and m1[c1] != c2:
            return False
        if c2 in m2 and m2[c2] != c1:
            return False
                
        m1[c1] = c2
        m2[c2] = c1

    print(m1)
    print(m2)
    return True

# solution
def is_isomorphic(string1, string2):

    map_str1_str2 = {}
    map_str2_str1 = {}

    for i in range(len(string1)):
        char1 = string1[i]
        char2 = string2[i]

        if char1 in map_str1_str2 and map_str1_str2[char1] != char2:
            return False

        if char2 in map_str2_str1 and map_str2_str1[char2] != char1:
            return False

        map_str1_str2[char1] = char2
        map_str2_str1[char2] = char1

    return True

# Driver code
def main():
    A = ["egg", "foo", "paper", "badc", "aaeaa"]
    B = ["all", "bar", "title", "baba", "uuxyy"]
    x = 1
    for i in range(len(A)):
        print(x, ".\tString 1 = ", A[i], sep="")
        print("\tString 2 = ", B[i], sep="")
        print("\n\tIsomorphic String ?", is_isomorphic(A[i], B[i]))
        print(100 * '-')
        x = x+1


if __name__ == '__main__':
    main()
