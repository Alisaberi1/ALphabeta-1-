

# to calculate the number of space between Alphabet
characters=["a","b","c","d","e" ,"f" , "g", "h" ,"i","j" ,"k","l","m","n", "o" ,"p", "q" ,"r", "s","t" ,"u", "v","w","x","y","z"]
x=str(input())
y=str(input())
while characters.index(y)>characters.index(x):
  print(characters.index(y)-characters.index(x))
  break
