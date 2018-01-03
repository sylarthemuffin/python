
def sum_area(rooms):
    area=[]
    for room in rooms:
        x=room*room
        area.append(x)
    y=sum(area)
    return y
    
    
def number_of_eggs(egg_dozens):
    eggs=[]
    for dozen in egg_dozens:
        x=dozen*12
        eggs.append(x)
    y=sum(eggs)
    return y
        
def points(word):
    for letter in word:
        print ord(letter)-96
    
def totalpoints(word):
    tot=[]
    for letter in word:
        tot.append(ord(letter)-96)
    print str(sum(tot))
    
    
def multiply(word):
    tot=[]
    for letter in word:
        tot.append(ord(letter)-96)
    x=1
    for i in tot:
        x=(i)*x
    print x