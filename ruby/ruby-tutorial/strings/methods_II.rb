# Enter your code here
def mask_article(string, words)
  words.each {|word|
      string.gsub!(word, strike(word))    
  }
  string
end
  
def strike(text)
  "<strike>#{text}</strike>"
end