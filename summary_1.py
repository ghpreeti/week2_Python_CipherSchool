#if statement
name="harshit"
if name == "harshit":
    print("u r harshit")
elif name == "mohit" or name=="Mohit" :
    print("u r mohit")   
else:
    print("u r not harshit")    

#while
i=0
while i<10:
    print(i)
    i+=1

#for loop
for i in range(1,11,2):
    print(i)

#break keyword
for i in range(1,11):
    if i==5:
        break
    print(i)

#continue keyword
for i in range(1,11):
    if i==5:
        continue
    print(i)

for i in "harshit":
    print(i)






