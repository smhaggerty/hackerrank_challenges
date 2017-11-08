def skip_animals(animals, skip)
    # Your code here
    new_array = Array.new
    animals.drop(skip).each_with_index {|animal, index|
        new_array.push "#{index + skip}:#{animal}"
        }
    new_array
end