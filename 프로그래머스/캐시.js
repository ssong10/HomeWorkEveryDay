function solution(cacheSize, cities) {
  var answer = cities.length * 5;
  const cache = []
  if (cacheSize === 0){
      return answer
  }
  cities.forEach(cityname => {
      const city = cityname.toLowerCase()
      const i = cache.indexOf(city)
      if (i > -1){
          cache.splice(i,1)
          answer -= 4
      } else if (cache.length === cacheSize) {
          cache.shift()
      }
      cache.push(city)
  })
  return answer;
}