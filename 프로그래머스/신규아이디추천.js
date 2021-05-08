function solution(new_id) {
  let id = Array.from(new_id)
  let tmp = []
  id.forEach((char,prev) => {
      if ('a' <= char && char <= 'z') {
          tmp.push(char)
      } else if ('A' <= char && char <= 'Z') {
          tmp.push(char.toLowerCase())
      } else if ('0123456789-_.'.indexOf(char) !== -1) {
          tmp.push(char)
      }
  })
  let new_tmp = []
  let prev = ''
  for (let i=0;i<tmp.length;i++){
      if (tmp[i] === '.' && tmp[i] === prev) {
          continue
      } else {
          new_tmp.push(tmp[i])
      }
      prev = tmp[i]
  }
  if (new_tmp[0] === '.') {
      new_tmp.shift()
  }
  if (new_tmp[new_tmp.length-1] === '.') {
      new_tmp.pop()
  }
  if (!new_tmp.length) {
      new_tmp = ['a']
  }
  new_tmp =  new_tmp.splice(0,15)
  if (new_tmp[new_tmp.length-1] === '.') {
      new_tmp.pop()
  }
  while (new_tmp.length < 3){
      new_tmp.push(new_tmp[new_tmp.length-1])
  }
  return new_tmp.join('');
}