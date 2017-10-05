#! /usr/bin/python
import sys

#if __name__ == "__main__":

def count_words(data):
   words = data.split(" ")
   num_words = len(words)
   return num_words

def count_lines(data):
	lines=data.split("\n")
	for l in lines:
		if not l:
			lines.remove(l)

	return len(lines)


#exit(1)

filename =input("please enter a filename : ")

f = open("macro.txt", "r")
data = f.read()
f.close()

num_words = count_words(data)
num_lines = count_lines(data)
 
print("The number of words: ", num_words)
print("The number of lines: ", num_lines)






