#!/bin/ruby

arr = Array.new(6)
for arr_i in (0..6-1)
    arr_t = gets.strip
    arr[arr_i] = arr_t.split(' ').map(&:to_i)
end

arr = arr.flatten

def sum_hourglass(index):
        values = get_hourglass_values_from_array(index)
        return values.flatten.inject(:+)
end

def get_hourglass_values_from_array(index):
        top_row = array[index..index + 2] 
        middle = array[index + 7]
        bottom_row = array[index + 12..index + 14]
        return top_row, middle, bottom_row
end
