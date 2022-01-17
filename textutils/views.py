from string import punctuation
from django.http import HttpResponse
from django.shortcuts import render
import string 
import re

#Created by -SARTHAK BINDAL
def index(request):
    return render(request, 'index.html')

def analyse(request):

    #Getting text
    djtext = request.POST.get('text','default')

    #Check which function is to be performed
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps','off')
    newlinerem = request.POST.get('newlinerem','off')
    extraspacerem = request.POST.get('extraspacerem','off')
    charcount  = request.POST.get('charcount','off')

    #Remove Punctutation Marks
    if removepunc == "on" and len(djtext)!=0:
        analysed=""
        for char in djtext:
            if char not in string.punctuation:
                analysed+=char
        params = {'purpose':'Removed Punctuations', 'analysed_text': analysed}
        djtext = analysed
        # return render(request,'analyse.html',params)

    #Transform string/text to uppercase
    if fullcaps == "on" and len(djtext)!=0:
        analysed = djtext.upper()
        params = {'purpose': 'UPPERCASE', 'analysed_text':  analysed}
        djtext = analysed


    #Remove Newline from text
    if newlinerem == "on" and len(djtext)!=0:
        analysed = ""
        for char in djtext:
            if char != "\n" and  char!='\r':
                analysed+=char
        params = {'purpose': 'Removed New Line', 'analysed_text':  analysed}
        djtext = analysed

    
    #Remove Extra Space from text
    if extraspacerem == "on" and len(djtext)!=0:
        analysed=''
        for index,char in enumerate(djtext):
            if not(djtext[index]==' ' and djtext[index+1]==' '):
                analysed+=char
        params = {'purpose': 'Removed Extra Space', 'analysed_text':  analysed}
        djtext = analysed

       
    
    #Exception Handling
    else:
        return HttpResponse("<center><h2>Error!</h2></center>")

    return render(request, 'analyse.html', params)

