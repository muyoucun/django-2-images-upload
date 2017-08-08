# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from PIL import Image
from myproject.myapp.models import Document
from myproject.myapp.forms import DocumentForm
from myproject.myapp.imgtest import imgtest
import os
'''
def list(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)

        if form.is_valid():
            newdoc = Document(docfile=request.FILES['docfile'])
            #data=imgtest(newdoc)

            newdoc.save()

            # Redirect to the document list after POST
            #return HttpResponseRedirect(reverse('list'))
            return HttpResponseRedirect(reverse('list'))
    else:
        form = DocumentForm()  # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    return render(
        request,
        'list.html',
        {'documents': documents, 'form': form}
    )

'''
'''
def list(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)

        if form.is_valid():
            hImg=form.cleaned_data['docfile']
            u=Document()
            u.docfile=hImg
            u.save()

            #width,height=imgtest('D:/87/media/'+str(u.docfile))
            path=imgtest('D:/87/media/'+str(u.docfile))
            
            #return render(request,'list.html',{'form':form,'name':u.docfile,'width':width,'height':height})
            return render(request, 'list.html', {'form': form, 'name': u.docfile,'path':path })
            #return HttpResponseRedirect(reverse('list'))
    else:
        form = DocumentForm()  # A empty, unbound form
    return render(
        request,
        'list.html',
        {'form': form}
    )
    # Load documents for the list page
    #documents = Document.objects.all()
    # Render list page with the documents and the form
'''


def list(request):
    imglist=[]
    namelist=[]
    if request.method=='POST':
        form=DocumentForm(request.POST,request.FILES)

        if 'file' in request.FILES:
            image=request.FILES['file']
            imglist.append(image)
        if 'file1' in request.FILES:
            image=request.FILES['file1']
            imglist.append(image)
        for image in imglist:
            u=Document()
            u.docfile=image
            namelist.append(u.docfile)
            u.save()

        path1='D:/87/media/'+str(namelist[0])
        path2='D:/87/media/'+str(namelist[1])
        path=imgtest(path1,path2)


        return render(request, 'list.html', {'form': form, 'path':path})

        #return HttpResponseRedirect(reverse('list'))
    else:
        form = DocumentForm()
    return render(
        request,
        'list.html',
        {'form': form}
    )