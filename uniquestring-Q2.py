#To retrun unique element out of the two string
import traceback
def testconcat(ele1,ele2):
    try:
        ele1=set(ele1+ele2)
        return ele1
    except Exception,e:
        print e
        print traceback.format_exc()
        


if __name__=="__main__":
    #On the fly entry
    ele1=raw_input('Enter 1st dtring: ')
    ele2=raw_input('Enter 2nd string: ')
    ele3=list(testconcat(ele1, ele2))
    
    print 'The required output is %s'%"".join(ele3)