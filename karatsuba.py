def karatsuba(num1: int, num2: int) -> int:
    """
    Performs multiplication using the Karatsuba algorithm, which reduces the number
    of single-digit multiplications required compared to the traditional method.

    The algorithm works by recursively splitting the numbers into smaller parts
    and applying the divide-and-conquer approach to compute the product more efficiently.

    :param num1: The first number to multiply.
    :param num2: The second number to multiply.
    :return: The product of the two numbers.
    """

    # Base case: If either number is a single-digit, perform simple multiplication.
    if num1 < 10 or num2 < 10:
        return num1 * num2

    # Determine the number of digits in the larger of the two numbers.
    m = max(size_base10(num1), size_base10(num2))

    # Compute half of the number of digits (rounded down) to split the number.
    m2 = m // 2

    # Split both numbers into two halves: high and low parts.
    high1, low1 = split_number(num1, m2)
    high2, low2 = split_number(num2, m2)

    # Recursively compute three multiplications to reduce the problem size:
    # z0 = low1 * low2 (product of lower halves)
    # z1 = (low1 + high1) * (low2 + high2) (cross terms multiplication)
    # z2 = high1 * high2 (product of higher halves)
    z0 = karatsuba(low1, low2)
    z1 = karatsuba(low1 + high1, low2 + high2)
    z2 = karatsuba(high1, high2)

    # Using Karatsuba's formula to combine results:
    # (z2 × 10 ^ (m2 × 2)) + ((z1 - z2 - z0) × 10 ^ m2) + z0
    return z2 * 10 ** (2 * m2) + (z1 - z2 - z0) * 10 ** m2 + z0


def split_number(num: int, second_half_size: int) -> tuple[int, int]:
    """
    Splits the given number into two parts:
    - `high`: The leftmost digits (most significant part)
    - `low`: The rightmost digits (the least significant part)

    The split is performed by dividing the number by 10^second_half_size.

    :param num: The number to split.
    :param second_half_size: The size of the second half (low part).
    :return: A tuple containing the high and low parts of the number.
    """
    high, low = divmod(num, 10 ** second_half_size)
    return high, low


def size_base10(num: int) -> int:
    """
    Calculates the number of digits in the given number.

    :param num: The number to count the digits of.
    :return: The number of digits in the given number.
    """
    return len(str(num))
