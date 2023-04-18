def main(num1, num2):
    """
    Given two non-negative integers, num1 and num2 represented as string.
    Return the sum of num1 and num2 as a string.

    Args:
        num1: str
        num2: str
    Returns:
        str: answer
    """
    a=str(int(num1)+int(num2))
    return a
num1=str(input())
num2=str(input())
print(main(num1,num2))