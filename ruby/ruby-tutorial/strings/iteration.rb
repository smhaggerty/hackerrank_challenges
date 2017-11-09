# Your code here
def count_multibyte_char(str)
  count = 0
  str.each_char {|i| count += 1 if i.bytesize > 1}
  count
end