function solution(numbers) {
  numbers = numbers.map(a=> String(a))
  numbers.sort((a,b)=> a+b < b+a ? 1 : -1)
  return numbers.every(e=>e === "0") ? "0" : numbers.join("") 
}