function find(tmp,nodes,visit) { 
  let flag = true
  while (flag) {
      flag = false
      let new_tmp = []
      tmp.forEach(t => {
          let [a,b] = t
          let check = nodes[b][1].every(v => visit[v])
          if (check) {
              flag = true
              visit[b] = true
              nodes[b][0].forEach(v => {
                  if (!visit[v]) {
                      new_tmp.push([b,v])
                  }
              })
          } else {
              new_tmp.push([a,b])
          }
      })
      tmp = new_tmp
  }
  if (tmp.length) {
      return false
  } else {
      return true
  }
}

function solution(n, path, order) {
  var answer = true;
  let visit = Array(n).fill(false)
  let nodes = Array.from(Array(n),()=>[[],[]])
  path.forEach(p => {
      let [a,b] = p
      nodes[a][0].push(b)
      nodes[b][0].push(a)
  })
  order.forEach(o => {
      let [a,b] = o
      nodes[b][1].push(a)
  })
  if (nodes[0][1].length){
      return false
  }
  visit[0] = true
  let tmp = []
  nodes[0][0].forEach(i=> {
      tmp.push([0,i])
  })
  return find(tmp,nodes,visit);
}