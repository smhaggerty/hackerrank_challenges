def select_arr(arr)
    # select and return all odd numbers from the Array variable `arr`
     arr.select {|i| i if i.odd?}
  end
  
  def reject_arr(arr)
    # reject all elements which are divisible by 3
    arr.select {|i| i unless i % 3 == 0}
  end
  
  def delete_arr(arr)
    # delete all negative elements
    arr.select {|i| i unless i.negative?}
  end
  
  def keep_arr(arr)
    # keep all non negative elements ( >= 0)
    arr.select {|i| i unless i.negative?}
  end