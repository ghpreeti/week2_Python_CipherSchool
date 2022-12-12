def greater(a,b):
    if a>b:
        return a
    else:
        return b


def greatest(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c
print( greatest(10,20,30))
print(greatest(20,40,60))

#function inside function
#greater(a,b)---->a or b
#greater (a,b,or c)----->greatest
#

def new_greatest(a,b,c):
    bigger = greater(a,b)
    return greater(bigger,c)

print(new_greatest(100,2000,4000))


