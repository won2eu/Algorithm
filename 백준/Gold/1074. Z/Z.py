N,r,c = map(int, input().split())

def Z(N,r,c):
    if N == 0:
        return 0;
    half = 2 ** (N-1)
    
    if r<half and c<half :
        return Z(N-1, r, c)
    if r<half and c>=half:
        return half*half + Z(N-1, r, c-half)
    if r>=half and c<half:
        return 2*half*half + Z(N-1, r-half, c)
    if r>=half and c>=half:
        return 3*half*half + Z(N-1, r-half, c-half)
    
print(Z(N,r,c))