def extra_character_index(str1, str2):
    if len(str1) < len(str2):
        str1, str2 = str2, str1
    result = 0
    for ch in str1:
        result ^= ord(ch)
    for ch in str2:
        result ^= ord(ch)
    return str1.index(chr(result))

# SOLUTION
def extra_character_index(str1, str2):

    result = 0
    str1_length = len(str1)
    str2_length = len(str2)

    for i in range(str1_length):
        result = result ^ (ord)(str1[i])

    for j in range(str2_length):
        result = result ^ (ord)(str2[j])

    if len(str1) > len(str2):
        index = str1.index((chr)(result))
        return index
    else:
        index = str2.index((chr)(result))
        return index

def main():
    # given string
    string1_list = ["wxyz", "cbda", "jlkmn", "courae", "hello"]
    string2_list = ["zwxgy", "abc", "klmn", "couearg", "helo"]
    for i in range(len(string1_list)):

        print(i+1, ".\tString 1 = ",
              string1_list[i], "\n\t", "String 2 = ", string2_list[i], sep="")
        print("\n\tExtra character is at index ", extra_character_index(string1_list[i], string2_list[i]), sep = "")
        print("-"*100)


if __name__ == '__main__':
    main()
