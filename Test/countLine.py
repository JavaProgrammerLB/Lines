def main():
    count = countCodeLine(u'codeLines2.py')
    print(count)

#统计文件的行数
def countCodeLine(s):
    try:
        #打开文件
        fh = open(s,'rb')
        l = fh.readlines()
        print('fh.readlines()的返回类型为：{}'.format(type(l)))
        lines = len(l)
        #关闭文件
        fh.close()
        return lines
    except PermissionError as e:
        print('{}文件打不开'.format(s))
        #return lines
    # except ValueError:
    #     print('{}文件在io的时候出错'.format(s))
        #return lines

if __name__ == '__main__':
    main()
