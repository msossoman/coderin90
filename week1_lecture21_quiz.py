#Here are items 1-4 of 5 for the week 1 lecture 21 quiz. 
#The 5th item (counting words in text doc) will be in a separate Github repo. I'll send you a link once I've completed it.

#Bullet 1: Read about how to append to a file and the difference between appending and writing
#Answer 1: Appending file adds text to the existing file, and writing file replaces text in the existing file.

#Bullet 2: Create a new python file 
#Answer 2: This is the file I created.

#Bullet 3: Write a program that reads any text file and outputs the contents of that file
#Answer 3:
myfile = open('myText.txt', 'r')
lines = myfile.readlines()
print lines
myfile.close

#Bullet 4: Reading and writing binary files
#Answer 4: open('filename', 'rb') would read a binary file and open('filename', 'wb') would write to a binary file

