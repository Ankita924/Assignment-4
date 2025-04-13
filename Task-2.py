line1=str(input('Enter text to write to the file: '))
file1=open('output.txt','w')
writing_file=file1.write(line1+'\n')
print("Data successfully written to output.txt")
file1.close()

line2=str(input('Enter additional text to append: '))
file1=open('output.txt','a')
appending_file=file1.write(line2)
print("Data successfully appended")
file1.close()

file1=open('output.txt','r')
reading_file=file1.readlines()
for i in reading_file:
    print(i)