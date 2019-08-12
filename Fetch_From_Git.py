import git
import os


# git.Git("C:\\Users\\kunal.hedgire\Downloads\\test-automation-master\\test-automation-master")\
#    .clone("https://github.com/kunal-hedgire/Operations")


name = input("Enter File to Search: ")
path = "C:\\Users\\kunal.hedgire\Downloads\\test-automation-master\\test-automation-master\\Operations\\" + name
path1 = "C:\\Users\\kunal.hedgire\Downloads\\test-automation-master\\test-automation-master\\Operations"


def search_file(name, path1):
    print("hi1")
    for root,dir1,files in os.walk(path1):
        print("HI2")
        if name in files:
            with open(path, 'r')as file:
                 line = file.read().split("\n\n")
                 print(line)
                 break
        else:
            print("File not found")


# name = "DBConnect.py"
# path = "C:\\Users\\kunal.hedgire\Downloads\\test-automation-master\\test-automation-master\\Operations\\DBConnect.py"
# path1 = "C:\\Users\\kunal.hedgire\Downloads\\test-automation-master\\test-automation-master\\Operations"

search_file(name,path1)




