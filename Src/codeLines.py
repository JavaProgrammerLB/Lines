import os
import re

def main():
    fileList = os.listdir()
    currentDir = os.getcwd()
    print('{}目录下共有{}个文件'.format(currentDir,len(fileList)))
    countFileType(fileList)

#统计各种类型文件的数目
def countFileType(lis):
    #print('debug0')
    d = dict()
    d2 = dict()
    for num in range(len(lis)):
        #print('debug1')
        filename = lis[num]
        try:
            #print("dubug2")
            fileType = getFileType(filename)
            numCodeLines =  countCodeLine(filename)
            if fileType in d:
                if d[fileType] == None:
                    pass
                else:
                    d[fileType] += 1
                if d2[fileType] == None:
                    pass
                else:
                    d2[fileType] += numCodeLines
            else:
                d[fileType] = 1
                d2[fileType] = numCodeLines
        except ValueError as e:
            print('{}文件出了问题'.format(filename))
            continue
    else:
        dList = list(d.keys())
        d2List = list(d2.keys())
        for i in range(len(dList)):
            val = d[dList[i]]
            val2 = d2[d2List[i]]
            print('其中{}文件的个数为：{}，行数为{}'.format(dList[i],val,val2))

#根据文件名判断文件的类型
def getFileType(s):
    if(type(s) == str):
        for i in range(len(s)):
            if(s[i] == '.'):
                return s[i:]
        else:
            return 'unkown'
    else:
        print('{}文件在获取文件类型的时候出错'.format(s))
        raise ValueError('fileName类型为{}错误，应该为str'.format(type(str)))

#统计文件的行数
def countCodeLine(s):
    try:
        #打开文件
        fh = open(s,'rb')
        #统计文件行数
        lines = len(fh.readlines())
        #关闭文件
        fh.close()
        return lines
    except PermissionError as e:
        print('{}文件打不开'.format(s))
        #return lines
    except ValueError:
        print('{}文件在io的时候出错'.format(s))
        #return lines

if __name__ == '__main__':
    main()
