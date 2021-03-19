
def tvarsumma(n):
    if n%10==n:
        return n
    else:
        summa = n%10 +tvarsumma(n//10)
        return summa

def tvarsumma2(n):
    summa = 0
    while n > 0:
        summa = summa + n%10
        n=n//10
    return summa


print(680%10)

