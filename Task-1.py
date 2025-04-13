try:
    file1 = open('sample.txt', 'r')
    reading_file = file1.readlines()
    list1 = reading_file
    print('Reading file content:')
    count=1
    for i in list1:
        print('Line',count,':',i)
        count+=1
    file1.close()
except FileNotFoundError:
    print("Error: The file 'sample.txt' was not found")

