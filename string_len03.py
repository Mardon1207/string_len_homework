def main(a,b):
    """
    String type variables a and b are given. Return True if the length is equal. If not equal, return False.
    Args:
        a: string
        b: string
    Returns:
        True or False
    """
    c=len(a)
    d=len(b)
    if c==d:
        s=True
    else:
        s=False
    return s
a=str(input())
b=str(input())
print(main(a,b))
