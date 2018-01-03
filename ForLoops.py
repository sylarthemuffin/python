import random

def print_areas(rooms):
    print "All rooms are square."
    for width in rooms:
        print "Area of room is:",
        print (width**2)
    print "a very square house."
    return width
    
    
def Print_eggs(egg_dozens):
    for dozen in egg_dozens:
        print dozen,
        print "dozen contains",
        print dozen*12,
        print "eggs."
    print "there are 12 eggs per dozen."
    return "That's " + str(len(egg_dozens))+" dozens."
    

def print_bananas(bananas):
    for dozen in bananas:
        print dozen,
        print "baker's dozens contain",
        print dozen*13,
        print "bananas."
    print "there are 13 bananas per baker's dozen."
    return "That's " + str(len(bananas))+" baker's dozens."
    
    
def count_slices(pizzas):
    for pie in pizzas:
        print pie,
        print "pizzas means you have",
        print pie*8,
        print "slices."
    return "That's " + str(len(pizzas))+ " orders of pizza and lots of happy people."
    
def print_bananas(nanas):
    for nana in nanas:
            print nana,
            print "large nanas typically weigh",
            print nana*.401,
            print "pounds."
        
def earned_run_average (earned_runs):
    print "This is the ERA"
    for ERA in earned_runs:
        print "ERA is",
        print 1.285*ERA
    return "Each pitcher pitched 7 innings"
    
    
def rect_area_calc(dimensions):
    print "This function is intended to take the areas of any amount of rectangles and give the individual areas and the total area. The answer will be given in square feet."
    print "There are",
    print str(len(dimensions)/2),
    print "rectangles that are made here."
    for dim in dimensions[::2]:
        print "the area of one of the rectangles is",
        print dim*(dim+1),
        print " square feet."
    print "The total area of the rectangles is ",
    a=[]
    for x in dimensions[::2]:
        p=x*(x+1)
        a.append(p)
    b=sum(a)
    print b,
    print "square feet."
        
        