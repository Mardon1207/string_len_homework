def main(s):
    """
    A string of length three is given. Check that it is a palindrome.
    Return True if the palindrome is False otherwise

    Args:
        s: str
    Returns:
        bool: answer
    """
    if s[0]==s[2]:
        a=True
    else:
        a=False
    return a
s=str(input())
print(main(s))