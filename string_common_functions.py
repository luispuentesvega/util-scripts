
#Len
str='Hello, My name is Luis'
print(len(str))
##Output:22

#upper
str='Hello, My name is Luis'
print(str.upper())
##Output: HELLO, MY NAME IS LUIS

#lower
str='Hello, My name is Luis'
print(str.lower())
##Output: hello, my name is luis

#count words on a string
str='Hello, My name is Luis'
print(str.count("l"))
##Output: 2

#.find
str='Hello, My name is Luis'
print(str.find("My"))
##Output: 7 -> Starts at 7 positions

#replace
str='Hello, My name is Luis'
print(str.replace("Hello", "Hi"))
##Output: Hi, My name is Luis