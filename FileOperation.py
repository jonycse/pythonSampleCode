import sys

def readFile(filename):
    try:
        file = open(filename,'r')
        content = file.read()
        file.close()
        return content
    except IOError:
        print "IOError:",IOError.args[0]
    except :
        print "Unexpected error:",sys.exc_info()[0]
        raise


print readFile('testfile.tsxt')
#print readFile('testfile')
#print readFile('testfile')