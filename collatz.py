#!/usr/bin/python
# calculate and print the collartz conjecture

"""
using a long list
map the collartz value of n at lst[n]

if n the the first number to be evaluate
the next number should be lst[n], the next one is lst[lst[n]], etc

(0-value means the end, ignore the first element (0-0) of list)

| 0| 1| 2| 3| 4| 5| 6| 7| 8| 9|10|
| 0| 0| 1|10| 2|16| 3|22| 4|28| 5|

"""
# calculate the collartz value
# even: n -> n/2
# odd:  n -> 3n+1
def calc(x):
    
    if (x%2)==0:
        return x/2
    else:
        return 3*x+1

# expand the list one 0-value
def expand_list(lst):
    lst.append(0)

def run(x):

    global count

    # printing the current number 
    #print x,
    #print "->",

    # check if the list is at the end or not
    if (x!=1):
        
        # if the map is not yet reach the current number 
        # expand it 
        while (len(lst)-1<x):
            expand_list(lst)

        # calculate the collazts value of the current number
        # map it to others value in the list
        lst[x] = calc(x)
        
        # run the new number
        run(lst[x])
        count += 1

    # if the list reach the end (4->2->1)
    else:
        pass
        # print("Done")

def main():
    
    global lst

    lst = [0,0]

    n = int(raw_input("N="))
    
    global count 
    i = 1
    #for i in range(1,n+1):
    while True:
        count = 0
        run(i)
        print i,
        print "=",
        print count
        i += 1

if __name__ == "__main__":
    main()  
