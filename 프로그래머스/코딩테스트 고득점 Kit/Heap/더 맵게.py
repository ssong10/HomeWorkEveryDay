import heapq
def solution(scoville, K):
    heapq.heapify(scoville) # 힙으로만들어준다.
    for i in range(len(scoville)-1):
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        if a < K:
            heapq.heappush(scoville, a+2*b)
        if scoville[0] >= K:
            return i+1
    return -1