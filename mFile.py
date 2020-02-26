# coding=utf-8

""" 读取图片 """
def get_binfile_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()