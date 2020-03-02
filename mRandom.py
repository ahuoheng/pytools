# coding=utf-8
import random

def getInt(n,m):
    i = random.randint(n,m)
    return i

def getStrIntFill(n,m,w):
    i = getInt(n,m)
    return str(i).zfill(w)

def getIntRange(n,m,k):
    random.randrange(n,m,k)

def getRanstr(length):
    H = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
    salt = ''
    for i in range(length):
        salt += random.choice(H)

    return salt

salt = getRanstr(6)
print(salt)
print(getInt(1,10))
print(getStrIntFill(1,10,6))

