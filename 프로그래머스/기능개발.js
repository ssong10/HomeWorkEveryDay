function solution(progresses, speeds) {
  var answer = [];
  let tmp = [];
  for (let i=0;i<progresses.length;i++) {
      let num = parseInt((99 - progresses[i]+speeds[i]) / speeds[i])
      tmp.push(num)
  }
  let day = 0;
  tmp.forEach(t => {
      if (t > day) {
          answer.push(1)
          day = t
      } else {
          answer[answer.length-1] += 1
      }
  })
  return answer;
}