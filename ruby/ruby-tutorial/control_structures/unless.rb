def scoring(array)
    # update_score of every user in the array unless the user is admin
    array.each {|i| i.update_score unless i.is_admin?}
end
  
  