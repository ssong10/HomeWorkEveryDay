// https://programmers.co.kr/learn/courses/30/lessons/42883

function solution(number, k) {
  number = Array.from(number)
  let answer = ''
  let idx = 0
  for (let i=0;i<number.length-k;i++) {
      let tmp = '0'
      for (let j=idx;j<i+k+1;j++) {
          if (tmp === '9') {
              break
          }
          if (tmp < number[j]){
              tmp = number[j]
              idx = j+1
          }   
      }
      answer += tmp
  }
  return answer;
}