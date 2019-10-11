

text_file=open("Write_it.txt","w")

lines=["Lİnes1 \n","Lines2 \n","Lines3 \n "]


text_file.writelines(lines)

text_file.close()




text_file=open("Write_it.txt","r")

print(text_file.read())
text_file.close()