# power_positive.py

def power(base, exponent):
    result = 1
    for _ in range(exponent):
        result *= base
    return result

if __name__ == "__main__":
    base = int(input("Enter base: "))
    exponent = int(input("Enter exponent: "))
    print("Result =", power(base, exponent))