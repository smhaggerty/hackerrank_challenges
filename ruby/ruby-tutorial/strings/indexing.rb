# Your code here
def serial_average(str)
  nums = str.split("-")
  avg = (nums[1].to_f + nums[2].to_f) / 2
  "#{nums[0]}-#{avg.round(2)}"
end