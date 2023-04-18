def main(s1,s2):
    """
    Given two strings, s1 and s2. Find their total length.
    Args:
        s1: string
        s2: string
    Returns:
        total length of strings
    """
    a=len(s1)+len(s2)
    return a
s1=str(input())
s2=str(input())
print(main(s1,s2))