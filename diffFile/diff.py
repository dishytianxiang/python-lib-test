#!/usr/bin/python
import difflib
import sys
try:
    textfile1 = sys.argv[1]
    textfile2 = sys.argv[2]
except Exception,e:
    print "Error:" + str(e)
    sys.exit()

def readFile(filename):
    try:
        fileHandle = open(filename,'rb')
        text = fileHandle.read().splitlines()
        fileHandle.close()
        return text
    except IOError as error:
        print("Read file Error:" + str(error))
        sys.exit()

text1_lines = readFile(textfile1)
text2_lines = readFile(textfile2)
d = difflib.HtmlDiff()
print d.make_file(text1_lines,text2_lines) #生成html结果：
