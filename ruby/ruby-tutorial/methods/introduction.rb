# Your code here
def prime?(num)
  prime = true
  return false if (num == 0 or num==1)
  for i in 2..Math.sqrt(num).to_i
    if num % i == 0
      prime = false
    end
  end
  return prime
end