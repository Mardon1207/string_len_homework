def main(s):
    """
    Given variable type string s. Return the character in the middle.
    If the length is even, return two characters in the middle.

    Args:
        s: str
    Returns:
        str: answer
    """

    n=len(s)%2
    a=len(s)//2
    if n==0:
        d=s[a-1:a+1]
    else:
        d=s[a]
    return d
s=str(input())
print(main(s))