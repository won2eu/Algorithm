import sys
input = sys.stdin.readline

a,b,c = map(int, input().split())

def zegop(a,b,c):
    if(b==1):
        return a%c
    
    val = zegop(a,b//2,c)
    val = val * val % c

    if(b%2==0):
        return val
    else:
        return val * a % c

print(zegop(a,b,c))