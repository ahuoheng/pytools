# coding=utf-8

""" 读取图片 """
def get_binfile_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

def get_txtfile_content(filePath):
    with open(filePath, 'r') as fp:
        return fp.read()

txt=get_txtfile_content('testdata/abc.txt')
print(txt)