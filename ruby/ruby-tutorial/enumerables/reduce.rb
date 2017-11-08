def sum_terms(n)
    # your code here
    (1..n).reduce(0) {|sum, num| sum += (num * num + 1)}
end