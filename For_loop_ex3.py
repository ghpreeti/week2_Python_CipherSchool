# practice for loop 
# ask user name and count each character
# "harshit"
# h:1
# a:2
# r:3
# s:4
# h:5
# i:6
# t:7

name=input("enter your name : ")
temp=""
for i in range(len(name)):
    if name[i] not in temp:
        print(f"{name[i]}:{name.count(name[i])}")
        temp += (name[i])



