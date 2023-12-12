# functions

def writepage(page):
    book = open(filename,"a")
    book.write("\n#- "+page)
    book.close

# take info (title, author)
# title is the book title
# author is the book author
# copy is the text
# file thats going to be copied
title = input("title :") 
author = "Sneak__ on discord"
copy = input("file you want to copy: ")
filename = title+".stendhal"

# created the output file with starting info
book = open(filename,"w")
book.write("title: "+title+"\nauthor: "+author+"\npages:")
book.close()

# reading the copy text
copytext = open(copy,"r")
text = copytext.read()
text = text.replace("\n"," ⌬ ") # using some obscure character to make \n one character
text = text.split(" ")

# read loop variables
pagetext = ""
lettercount = 0
linecount = 0

for i in range(0,len(text)-1): # for every word
    wordlength = len(text[i])
    if lettercount+wordlength >19: # if the current line is 'full' (based of the normal letter width)
        pagetext += "\n" # move to the next line
        linecount += 1
        lettercount = 0
    if linecount == 10: # if the page is 'full' (arbitarily set to 10 lines)
        writepage(pagetext)
        linecount = 0
        pagetext = ""
        lettercount = 0
    if text[i] == "⌬": # if the character is a line break
        pagetext += "\n"
        linecount += 1
        lettercount = 0
    else:
        pagetext += text[i] + " " # else add the word
        lettercount += len(text[i])+1

