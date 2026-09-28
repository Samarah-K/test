# If you wish you can import any modules from the standard library
# Do not use modules that are not in the standard library
import sys


def processArray(array):
    '''Modify this function to process `array` as indicated
    in the question. At the end, return the appropriate 
    value.

    Please create appropriate classes, and use appropriate
    data structures as necessary.

    Do not print anything in this function.

    Submit this entire program (not just this function)
    as your answer
    '''
    i,wi=0,0
    while i<len(array):
        if array[i]%2!=0:
            j=i
            while j<len(array) and array[j]%2!=0:
                j+=1
            array[wi]=array[j-1]
            wi+=1
            i=j
        else:
            array[wi]=array[i]
            wi+=1
            i+=1
    return wi   # change this appropriately, if necessary

def run():
    array = []
    for line in sys.stdin:
        try:
            intval = int(line)
        except ValueError:
            # If line is not exactly one integer, ignore it
            pass
        if intval == 0:
            break
        array.append(intval)
    newlen = processArray(array)
    for i in range(newlen):
        print(array[i])

if __name__ == '__main__':
    run()
