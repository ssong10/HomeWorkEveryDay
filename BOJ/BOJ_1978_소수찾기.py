N = int(input())
arr = sorted(map(int,input().split()))
def prime(MAX):
    MAX += 1
    primes = [False,False] + [True]*(MAX-2)
    for i in range(2, int(MAX**0.5)+1):
        if primes[i]:
            for j in range(2*i, MAX, i):
                primes[j] = False
    return primes
primes = prime(max(arr))
answer = 0
for i in range(N):
  if primes[arr[i]]:
    answer += 1
print(answer)