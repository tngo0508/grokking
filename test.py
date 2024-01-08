def construct_message(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    words = {}
    for line in lines:
        number, word = line.split()
        words[int(number)] = word.strip()

    pyramid = []
    current_line = []
    total_words = 0

    for number, word in sorted(words.items()):
        current_line.append(word)
        total_words += 1

        if total_words == number:
            pyramid.append(current_line.copy())
            current_line.clear()
            total_words = 0

    message = ' '.join(word for line in pyramid for word in line)
    return message

# Example usage:
file_path = 'c:\\Users\\tngo0\\Downloads\\coding_qual_input.txt'
result = construct_message(file_path)
print(result)
