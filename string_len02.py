def main(a):
    """
    A string type variable is given. Return True if its length is even. Return False if its length is odd.
    Args:
        a: string
    Returns:
        True or False
    """
    b=len(a)%2
    if b==0:
        s=True
    elif b==1:
        s=False
    return s
a=str(input())
print(main(a))