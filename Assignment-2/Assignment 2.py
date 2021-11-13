import array
import csv

def Q1a(): #this function is the solution for question 1, part a
    global array1, tuple1, list1, set1, dictionary1
    with open ('C:/Users/johns/OneDrive/Documents/University/GCIS 123/GCIS-123/Assignment-2/assignment2_file.csv', 'r') as x:
        ro = csv.reader(x) #csv reader object
        c = 0 #counter variable
        for i in ro:
            if c == 0:
                array1 = array.array('B', )
                for j in i:
                    array1.append(int(j))
                c+=1
            elif c == 1:
                tuple1 = ()
                for j in i:
                    tuple1 += (j,) #without the comma, it is not recognized as a tuple
                c+=1
            elif c == 2:
                list1 = i
                c+=1
            elif c == 3:
                set1 = set(i)
                c+=1
            elif c == 4:
                temp = []
                for j in i:
                    temp += [j] 
                #this code creates a temporary list that is later used to create the dictionary, as dictionaries are unordered types
                c+=1
            elif c == 5:
                dictionary1 = {}
                for j in range (len(temp)):
                    dictionary1[temp[j]] = i[j]
                c+=1
    return [array1, tuple1, list1, set1, dictionary1]

def Q1b():
    pass
def Q1c():
    pass
def Q1d():
    pass

def Q2a():
    pass
def Q2b():
    pass
def Q2c():
    pass
def Q2d():
    pass

def Q3a():
    pass

def testQ1a(x):
    #this test checks whether Q1a() returns varibles of the correct type
    assert(type(x[0]) == type(array.array('B')))
    assert(type(x[1]) == type((1,2)))
    assert(type(x[2]) == type([1]))
    assert(type(x[3]) == type({1, 2}))
    assert(type(x[4]) == type({1:2, 2:1}))

    #if the test passes, it runs the following
    print("No Errors\n")

    for i in x:
        print(i, '\n')

def main():
    Q1a()
    testQ1a(Q1a())
    
main()