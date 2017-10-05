#!/usr/bin/python

f = open("macro.txt", "r+")
data = f.read()

#no of bytes to be read
str1 = f.read(25)
print(str1+" hello ")


#f.write( "Python is a great language.\nYeah its great!!\n")
f.close()
#print(data)



#after spliting it stores in the [list] 
words = data.split(" ")
#print("The words in the text are:", words)

#print(words)
num_words = len(words) #find the length(numbers) of list 
print("\n The number of words is ", num_words)

lines=data.split("\n")
#print("\n \n The words in the text are:", lines)
num_words = len(lines)
print("\n\nThe number of lines are :", num_words)

for l in lines:
	if not l:
		lines.remove(l)  #removing a data from the list



