
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'home.html')

def count(request):
    fulltext = request.GET['fulltext']
    #print(fulltext)
    wordlist = fulltext.split()
    worddict = {}
    for i in wordlist:
        if i in worddict:
            worddict[i]  = worddict[i]+1
        else:
            worddict[i] = 1
    return render(request,'count.html',{'fulltext':fulltext,'count':len(wordlist),'worddict':worddict})
