N,M = map(int, input().split())
arr = [0]*(M)
isused = [False]*(N+1)

def func(K): #재귀함수
    if K == M:  #탈출조건을 K가 M일때
        print(*arr) #모든 배열 요소를 출력

        return #함수 탈출
    
    for i in range(1,N+1): #1부터 N까지 수에서
        if(not isused[i]): #isused[i] 그 수가 사용되지 않았다면
           arr[K] = i #배열에 그 수를 넣고
           isused[i] = True #사용했다고 적어준 다음
           func(K+1) #그 다음번째 자리수에서 다시 재귀호출
           isused[i] = False #방문기록 초기화

func(0)
