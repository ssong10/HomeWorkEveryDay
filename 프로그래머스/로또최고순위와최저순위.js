function solution(lottos, win_nums) {
  const result = [7,7]
  const nums = new Set()
  let blank = 0
  lottos.forEach(num => {
      if (num){
          nums.add(num)
      } else {
          blank += 1
      }
  })
  Array.from(nums).forEach((num) => {
      let correct = win_nums.some(win_num => win_num === num)
      result[1] -= correct ? 1 : 0
  })
  result[1] = result[1] === 7 ? 6 : result[1]
  result[0] = result[1] - blank
  result[0] = result[0] ? result[0] : 1
  return result;
}