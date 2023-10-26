def fraction_to_decimal(numerator, denominator):
    result, remainder_map = "", {}
    if numerator == 0:
        return '0'

    if (numerator < 0) ^ (denominator < 0):
        result += '-'

        numerator = abs(numerator)
        denominator = abs(denominator)

    quotient = numerator / denominator
    remainder = (numerator % denominator) * 10
    result += str(int(quotient))

    if remainder == 0:
        return result
    else:
        result += "."
        while remainder != 0:
            if remainder in remainder_map.keys():
                beginning = remainder_map.get(remainder)
                left = result[0: beginning]
                right = result[beginning: len(result)]
                result = left + "(" + right + ")"
                return result

            remainder_map[remainder] = len(result)
            quotient = remainder / denominator
            result += str(int(quotient))
            remainder = (remainder % denominator) * 10
        return result


def main():
    inputs = [(0, 4), (4, 2), (5, 333), (2, 3), (47, 18),
              (93, 7), (-5, 333), (47, -18), (-4, -2)]

    for i in range(len(inputs)):

        print(i + 1,  ".\tInput: fraction_to_decimal", inputs[i], sep="")
        result = fraction_to_decimal(inputs[i][0], inputs[i][1])
        print("\tOutput: ", result, sep="")
        print("-"*100)


if __name__ == '__main__':
    main()
