result = 0
def solution(numbers, target):
    def back(n,cur_sum):
        global result
        if n == len(numbers):
            if cur_sum == target:
                result += 1
        else:
            back(n+1,cur_sum+numbers[n])
            back(n+1,cur_sum-numbers[n])
    back(0,0)
    return result