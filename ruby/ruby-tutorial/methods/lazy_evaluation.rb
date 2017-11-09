# Enter your code here. Read input from STDIN. Print output to STDOUT
require 'prime'
array_size = gets.to_i

palindromic_prime_array = -> (size) do 
    print Prime.each.lazy.select{|prime| prime.to_s == prime.to_s.reverse}.first(size)
end

palindromic_prime_array.(array_size)