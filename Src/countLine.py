def main():
    count = countCodeLine('codeLines.py')
    print(count)

#统计文件的行数
def countCodeLine(s):
    try:
        #打开文件
        fh = open(s)
        print(type(fh))
        #统计文件行数
        lines = len(fh.readlines())
        #关闭文件
        fh.close()
        print(lines)
        return lines
    except PermissionError as e:
        print('{}文件打不开'.format(s))
        #return lines
    except ValueError:
        print('{}文件在io的时候出错'.format(s))
        #return lines

if __name__ == '__main__':
    main()
