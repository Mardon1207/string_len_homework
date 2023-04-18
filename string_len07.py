def main(s1,s2,s3):
    """
    Given three strings, s1, s2 and s3. return their odd lengths, example "[s1, s2]". If there is no odd length, return "[]".
    Args:
        s1: string
        s2: string
        s3: string
    Returns:
        string
    """
    a=len(s1)
    b=len(s2)
    c=len(s3)
    s=""
    if a%2==1:
        s=s+s1+" "
    if b%2==1:
        s=s+s2+" "
    if c%2==1:
        s=s+s3
    return "["+s+"]"
s1=str(input())
s2=str(input())
s3=str(input())
print(main(s1,s2,s3))

