# coding=utf-8
import os
""" 读取图片 """
def get_binfile_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

def get_txtfile_content(filePath):
    with open(filePath, 'r',encoding="utf-8") as fp:
        return fp.read()

def GetDirFileList(path):
    Filelist = list()
    for root,dirs,files in os.walk(path):
             for file in files:
                   Filelist.append(root + os.sep + file)
    return Filelist

txt=get_txtfile_content('testdata/abc.txt')
print(txt)
print(GetDirFileList('.'))