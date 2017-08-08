
from PIL import Image
from PIL import ImageFilter
import os
import time


'''
def imgtest(url):
    img=Image.open(url)
    tmp=url.split('/')

    result=img.filter(ImageFilter.CONTOUR)
    PATH = 'd:/87/myproject/myapp/static/img/'+ tmp[7]
    result.save(PATH)
    path = '/'+PATH.split('/', 4)[4]
    return path
'''

def imgtest(path1,path2):
    ISOTIMEFORMAT = '%Y%m%d%H%M%S'
    img1=Image.open(path1)
    img2=Image.open(path2)
    img3=Image.blend(img1,img2,0.5)


    PATH='d:/87/myproject/myapp/static/img/'+str(time.strftime(ISOTIMEFORMAT))+'.jpg'
    img3.save(PATH)
    path='/'+PATH.split('/',4)[4]
    return path
