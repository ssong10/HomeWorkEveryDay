function solution(gems) {
  let kind = new Set(gems).size
  let answer = [1,10**10]
  let start=-1;
  let end=-1;
  const gemObj = {}
  let count = 0
  while (start <= end) {
      if (count < kind && end !== gems.length-1) {
          end += 1
          if (gems[end] in gemObj) {
              gemObj[gems[end]] += 1
          } else {
              count += 1
              gemObj[gems[end]] = 1
          }
      } else {
          start += 1
          if (count === kind && answer[1]-answer[0] > end-start) {
              answer = [start+1,end+1]
          }
          gemObj[gems[start]] -= 1
          if (gemObj[gems[start]] === 0) {
              delete gemObj[gems[start]]
              count -= 1
          }
      }
  }
  return answer
}