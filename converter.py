# take info (title, book to copy)
# title is the book title
# author is the book author
# copy is the text
# file thats going to be copied
title = input("title :") 
author = "Sneak__ on discord"
copy = input("file you want to copy: ")
textcontent = ""
partnum = 1 # the current page being saved/writen
pagecount = 0 # the number of pages currently written

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
    if lettercount+wordlength+1 >19 and text[i] != "⌬": # if the current line is 'full' (based of the normal letter width)
        pagetext += "\n" # move to the next line
        linecount += 1
        lettercount = 0

    if linecount == 10: # if the page is 'full' (arbitarily set to 10 lines) -> save the page to textcontent
        textcontent +="\n#- "+pagetext
        pagecount+=1
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

    if pagecount == 100 or i == len(text)-2: # when a book is full OR its the end of the source text, write the file for it and go to the start the next book
        book = open(title+str(partnum)+".stendhal","w")
        book.write("title: "+title+"\nauthor: "+author+"\npages:")
        book.write(textcontent)
        book.close()
        pagecount=0
        partnum+=1
        textcontent=""
        pagetext=""

print("text has been converted to stendhal books")