text_file=open("deneme.txt","w")

text_file.write("1,1 \n")

text_file.write("2,2 \n")

text_file.write("3,3 \n")


text_file.close()


#open the text file


text_file=open("deneme.txt","r")

print(text_file.read())

text_file.close()