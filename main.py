from karatsuba import karatsuba


def main():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))

    print(f"Multiplying {num1} and {num2} using Karatsuba algorithm:")
    result = karatsuba(num1, num2)

    print(f"Result: {result}")

    expected = num1 * num2
    print(f"Expected result: {expected}")
    print(f"Verification: {'Correct' if result == expected else 'Incorrect'}")


if __name__ == "__main__":
    main()
