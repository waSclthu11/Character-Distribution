"""
distribution.py
Author: waSclthu11
Credit: Assignment description

Assignment:

Write and submit a Python program (distribution.py) that computes and displays 
the distribution of characters in a given sample of text.

Output of your program should look like this:

Please enter a string of text (the bigger the better): The rain in Spain stays mainly in the plain.
The distribution of characters in "The rain in Spain stays mainly in the plain." is:
iiiiii
nnnnnn
aaaaa
sss
ttt
ee
hh
ll
pp
yy
m
r

Notice about this example:

* The text: 'The rain ... plain' is provided by the user as input to your program.
* Uppercase characters are converted to lowercase
* Spaces and punctuation marks are ignored completely.
* Characters that are more common appear first in the list.
* Where the same number of characters occur, the lines are ordered alphabetically. 
  For example, in the printout above, the letters e, h, l, p and y both occur twice 
  in the text and they are listed in the output in alphabetical order.
* Letters that do not occur in the text are not listed in the output at all.
"""
def compare(a, b):
    """
    compare - generic comparison function for testing two elements.
    """
    return b > a


def bsort(seq, cmp):
    """
    bsort - simple sorting algorithm that uses any comparison function
    seq - a list to be sorted
    cmp - a function for comparing two elements of seq
    """
    sorted = False  # assume the seq is not sorted to start with
    while not sorted:
        sorted = True   # assume it's already sorted correctly
        for index, value in enumerate(seq): # for every element in seq
            if index > 0:                   # past the first..
                if not cmp(seq[index-1], value):  # if this element is out of order
                    sorted = False          # then the list is not sorted yet
                    seq[index-1], seq[index] = seq[index], seq[index-1] # and swap it

import string
abc = string.ascii_lowercase
text = input(str("Please enter a string of text (the bigger the better): "))
print('The distribution of characters in "{}" is: '.format(text))
text=str.lower(text)
abc=([abc[w:w+1] for w in range(0, 26, 1)])#Splits alphabet into list
x=0
letters=[]
while(x<=25): #Loop goes through all letters in alphabet and counts the number of each letter in entered text
    y=text.count(abc[x]) 
    letters.append(y)
    x=x+1


x=0
alph=[]
while(x<=25):
    for z in range(0,letters[x]):
        if letters[x]>0: 
            alph.append(abc[x])
    if letters[x]>0:
        alph.append(" ")
    x=x+1
alph= ''.join(alph)

alph= alph.split(" ")
alph.pop(-1)

y=len(alph)


x=0
while(x==0):
    x=1
    for i in range(0,y):
        if i > 0:
            if len(alph[i-1]) > len(alph[i]):
                x=0
                alph[i-1], alph[i] = alph[i], alph[i-1]
alphf=[]

for x in range(1,(len(alph)+1)):
    print(alph[-x])



