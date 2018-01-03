def areas(widths):
    areas=[]
    for width in widths:
        areas.append(width**2)
    return areas

def to_inches(tree_heights):
    inches=[]
    for height in tree_heights:
        inches.append(height*12)
    return inches
    
def word_lengths(word_list):
    lengths=[]
    for word in word_list:
        lengths.append(len(word))
    return lengths
    
def cube(numbers):
    products=[]
    for i in numbers:
        x=i**(3)
        products.append(x)
    return products
def longest_word(phrase):
    record=0
    for word in phrase:
        if len(word)>record:
            record=len(word)
    return record

def biggest_int(integers):
    record=0
    for int in integers:
        if int>record:
            record=int
    return record