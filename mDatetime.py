# coding=utf-8
import datetime
import time


def _getdatetime():
    t = datetime.datetime.now()
    return t
def getdate():
    t = _getdatetime().strftime('%Y-%m-%d')
    return t

def gettime():
    t = _getdatetime().strftime('%H:%M:%S')
    return t

def getdatetime():
    t = _getdatetime().strftime('%Y-%m-%d %H:%M:%S')
    return t


_timestart=time.clock()
_timestop=None

def watchstart():
    _timestart =time.clock()

def watchstop():
    _timestop =time.clock()
    return (_timestop-_timestart)

print(getdatetime())
print(getdate())
print(gettime())


watchstart()
time.sleep(1.1)
print (str( watchstop()))