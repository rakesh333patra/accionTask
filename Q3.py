"""a. Write a function that accepts an integer and returns True if the input is between
4 and 10, inclusive; otherwise, return False
b. Write a function to test if a list contains any items. Return 'EMPTY' if it does not
contain any items and 'NOT EMPTY' if it does.
c. Write a function that accepts a file name and a string and writes the string to the
file with the given file name.
d. Write a function that accepts a list and doubles each value in the list. When no
input parameter is provided, return an empty list."""
import traceback
def Intergerfun(val):
    try:
        if val>=4 and val<=10:
            return True
        else:
            return False
        
    except Exception,e:
        print e
        
def testlist(val):
    try:
        if len(val)>0:
            return 'NOT EMPTY'
        else:
            return 'EMPTY'
    except Exception,e:
        print e
        
def fileOperation(filename,name):
    try:
        f=open(filename,'r')
        f.write(name)
        f.close()
    except Exception,e:
        print e
        
def listDouble(val):
    print val
    try:
        if len(val)==0:
            return val
        else:
            return [i*2 for i in val]
    except Exception,e:
        print e
        
        
if __name__=="__main__":
    """Pass the respective value to the funcation and comment out which you dont need"""
    #To test if the number lie in define range
    Intergerfun(val)
    #To test list is empty
    testlist(val)
    #To test fie operation
    fileOperation(filename, name)
    #To test list double
    listDouble(val)
    
        