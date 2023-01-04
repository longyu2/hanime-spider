# 本py模块将with open 封装，简化使用

# 两个参数，1是文件名，二是读取类型，以二进制还是文本读取，默认编码utf8
def read(filename,filetype):
    try:
        with  open(filename, filetype, encoding='utf8') as fp:
            return fp.read()
    except:
        print("error!")
        return False

# 三个参数，1是文件名，二是读取类型，以二进制还是文本读取，默认编码utf8
def write(filename,filetype,content):

        try:
            with  open(filename, filetype,encoding='utf8') as fp:
                fp.write(content)

        except:
            print("error!")
            return False
        else:
            return True