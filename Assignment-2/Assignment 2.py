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
                    try:
                        tuple1 += (int(j),) #without the comma, it is not recognized as a tuple
                    except:
                        tuple1 += (j,)
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

def Q1b(x):
    f = open('C:/Users/johns/OneDrive/Documents/University/GCIS 123/GCIS-123/Assignment-2/assignment2_file.txt', 'w')
    #this code prints the array in reverse order
    for i in range(-1, -(len(x[0]))-1, -1):
        y = x[0][i]
        if i == (-(len(x[0]))):
            print(y)
            f.write(str(y)+'\n')
        else:
            print (y, end = ', ')
            f.write(str(y)+', ')
    print('\n') #inserts extra blank line 

    #this code prints the tuple in reverse order
    for i in range(-1, -(len(x[1]))-1, -1):
        y = str(x[1][i])
        if i == (-(len(x[1]))):
            print(y)
            f.write(y+'\n')
        else:
            print (y, end = ', ')
            f.write(y+', ')
    print('\n') #inserts extra blank line

    #this code prints the list in reverse order
    for i in range(-1, -(len(x[2]))-1, -1):
        y = x[2][i]
        if i == (-(len(x[2]))):
            print(y)
            f.write(y+'\n')
        else:
            print (y, end = ', ')
            f.write(y+', ')
    print('\n') #inserts extra blank line  

    #set was saved backwards, and is unordered
    c = 0
    print(len(x[3]))
    for i in (x[3]):
        if c == (len(x[3])-1):
            f.write(i+'\n')
        else:
            f.write(i+', ')    
            c+=1
    print(x[3])

    #this code prints the dictionary in reverse order
    temp = [] #temporary list 
    for k in x[4]:
        temp += [k+':'+x[4][k]]
    for i in range(-1, -(len(temp)), -1):
        y = temp[i]
        if i == (-(len(x[4])-1)):
            print(y)
            f.write(y+'\n')
        else:
            print (y, end = ', ')
            f.write(y+', ')
    print('\n') #inserts extra blank line
    f.close()

def Q1c():
    with open('C:/Users/johns/OneDrive/Documents/University/GCIS 123/GCIS-123/Assignment-2/assignment2_file.txt', 'r') as f:
        for i in f:
            print (i, end = '')

def Q1d(x): 
    if 'Fujairah' in x[2]: #this function uses membership operator to check 
        print('Found!', "Fujairah")
    else:
        print(None)

    if 'brown' in x[3]: #this function uses membership operator to check 
        print("Found", "brown")
    else:
        print(None)
    
    for i in x[4]: #this function iterates through the dictionary and checks
        if x[4][i] == "Data Science":
            print ("Found", "Data Science")
            break
    else:
        print(None)

def Q2a(A):
    #Insertion Sort
    def insertionSort(l):
        n = len(l)
        for i in range (1, n):
            x = l[i]
            j = i-1
            while ((x < l[j]) and (j >= 0)):
                l[j+1] = l[j]
                j = j-1
            l[j+1] = x
        print(l)
    insertionSort(A[0])

    #Merge Sort
    def mergeSort(A):
        size = len(A)
        temp = [0 for i in range(len(A))]
        if size > 1:
            middle = size // 2
            leftA = A[:middle]
            rightA = A[middle:]
    
            leftA = mergeSort(leftA)
            rightA = mergeSort(rightA)
    
            p = 0
            q = 0
            r = 0
    
            lenLeft = len(leftA)
            lenRight = len(rightA)
            while p < lenLeft and q < lenRight:
                if leftA[p] < rightA[q]:
                    temp[r] = leftA[p]
                    p += 1
                else:
                    temp[r] = rightA[q]
                    q += 1
                
                r += 1
    
            
            while p < lenLeft:
                temp[r] = leftA[p]
                p += 1
                r += 1
    
            while q < lenRight:
                temp[r]=rightA[q]
                q += 1
                r += 1
        else:
            temp = list(A)
        return temp
    print(tuple(A[1]))

    #Quick Sort
    def quickSort (A, low, high):
        if low < high:
            p = partition (A, low, high)
            quickSort (A, low, p-1)
            quickSort (A, p+1, high)
    def partition(A, low, high):
        pivot = A[high]
        i = low
        for j in range (low, high+1):
            if A[j] < pivot:
                swap (A, i, j)
                i = i+1
        swap (A, i, high)
        return i
    def swap(array, a, b):
        array[b], array[a] = array[a], array[b]
    
    quickSort(A[2], 0, len(A[2])-1)
    print(A[2])

def Q2b():
    pass
def Q2c():
    pass
def Q2d():
    pass

def Q3a():
    pass

def testQ1a(x):
    #this test checks whether Q1a() returns variables of the correct type
    assert(type(x[0]) == type(array.array('B')))
    assert(type(x[1]) == type((1,2)))
    assert(type(x[2]) == type([1]))
    assert(type(x[3]) == type({1, 2}))
    assert(type(x[4]) == type({1:2, 2:1}))

    #if the test passes, it runs the following
    print("No Errors\n")

    for i in x:
        print(i, '\n')

def testQ1b():
    with open ('C:/Users/johns/OneDrive/Documents/University/GCIS 123/GCIS-123/Assignment-2/assignment2_file.txt', 'r') as x:
        c = ''
        for i in x:
            c+=i
        assert(len(c) != 0)
        print ("No Errors\n")


def main():
    Q1a()
    testQ1a(Q1a())
    Q1b(Q1a())
    testQ1b()
    Q1c()
    Q1d(Q1a())

    Q2a(Q1a())
    
main()