def encode(strings):
    encode = '<tag>'.join(strings)
    return encode
    

def decode(string):
    return string.split('<tag>')


# solution
def encode(strings):
    encoded_string = ""

    for x in strings:
        # Add appended 4 byte string length to string in encoded string
        encoded_string += length_to_bytes(x) + x

    return encoded_string


def decode(string):
    # Initialize a pointer
    i = 0
    decoded_string = []

    while i < len(string):
        # Get length in integer from 4 byte string
        length = bytes_to_length(string[i : i + 4])
        i += 4
        # Add string of the computed length
        decoded_string.append(string[i : i + length])
        # Move the pointer
        i += length

    return decoded_string


def length_to_bytes(x):
    # Express the string length as a string of bytes
    # If there are 4 characters in the string, the function will return '0004'
    length = len(x) # Compute the length of string
    bytes = []

    for i in range(4):
        # Apply right shift operator
        bytes.append(chr(length >> (i * 8)))

    bytes.reverse()
    # Convert the array to the string
    bytes_string = "".join(bytes)

    return bytes_string


def bytes_to_length(bytes_string):
    # Convert a 4-byte string to an integer
    # If bytes_string is '0040', the function will return 40
    result = 0

    for c in bytes_string:
        result = result * 256 + ord(c)
        
    return result


# Driver code
def main():
    input = [
                ["I", "love", "educative"], 
                ["6^Hello_5", "5_World^6"], 
                ["I", "love", "programming"], 
                ["a", "b", "c", "d"], 
                ["*_*EDUCATIVE*_*"]
            ]

    for i in range(len(input)):
        encoded = encode(input[i])
        print(i + 1, ".\t Input = ", input[i], sep="")
        print("\t Encoded string = ", print_encoded(encoded), sep="")
        print("\t Output = ", decode(encoded), sep="")
        print("-" * 100)


# For printing (Bytes to Integer)
def print_encoded(string):
    final = ""
    i = 0

    while i < len(string):
        for z in string[i : i + 4]:
            final += str(ord(z))
        length = bytes_to_length(string[i : i + 4])
        i += 4
        final += string[i : i + length]
        i += length
    return final


if __name__ == "__main__":
    main()