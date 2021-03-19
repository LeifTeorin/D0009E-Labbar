
def bounce(n):
    if n==0:
        print(n)
    else:
        print(n)
        bounce(n-1)
        print(n)

def bounce2(n):
    x=n
    while n>0:
        print(n)
        n=n-1
    while n<=x:
        print(n)
        n=n+1

bounce(5)
bounce2(7)
