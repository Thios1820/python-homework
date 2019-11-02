from os.path import isfile  # importing package

if  isfile('housing.data'):  # condition on the file
    my_file = open('housing.data')  # opening file

    for line in my_file.readlines():  # loop the lines to read
        print(line.split())  # pour diviser une chaine de characters en liste

my_file.close()  # always close the file
