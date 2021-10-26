import array
def swap(array, a, b):
    array[b], array[a] = array[a], array[b]

def main():
    x = array.array('l', [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    print(x)
    swap(x, 2, 5)
    print(x)

main()

#Merge Sort
def mSplit(A):
    e = array.array('l', []) #even indices
    o = array.array('l', []) #odd indices
    C = True #even condition
    for i in A:
        if C:
            e += i
        else:
            o += i
        C = not(C) #condition inverter
    return e, o

def mMerge(A):
    pass

def mMain(A):
    if len(A) in (1, 0):
        return A
    else:
        s = mSplit(A)
        return mMerge(s)

#Quick Sort
def sort (A, low, high):
    if low < high:
        p = partition (A, low, high)
        sort (A, low, p-1)
        sort (A, p+1, high)
def partition(A, low, high):
    pivot = A[high]
    i = low
    for j in range (low, high+1):
        if A[j] < pivot:
            swap (A, i, j)
            i = i+1
    swap (A, i, high)
    return i