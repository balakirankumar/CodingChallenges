import sys

def getPrimeFactors(n):
    divisor=2
    factors=list()
    while divisor <= n :
        if n%divisor == 0 :
            factors.append(divisor)
            n=n/divisor
        else:
            divisor+=1
    return factors

print(getPrimeFactors(int(sys.argv[1])))