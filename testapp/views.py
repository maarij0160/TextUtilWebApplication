
# DEVELOPERS PAGE -----MAARIJ

from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    params = {'name' : 'TEST-BOT', 'place' : 'TEST'}
    return render(request,'index.html',params)

def about(request) :
    params={'name' : 'TEST-BOT', 'place' : 'TEST'}
    return render(request,'aboutus.html',params)

def analyze(request):
    s = request.POST.get('text', 'default')
    rempunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')


    if rempunc == "on" :

        punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        analyzed = ""

        for char in s :
            if char not in punctuations:
                analyzed = analyzed + char

            params ={'purpose' : 'REMOVE PUNCTUATION', 'analyzed_text' : analyzed}

        s=analyzed

    if fullcaps == "on" :
        analyzed = ""
        for char in s:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Changed to Uppercase', 'analyzed_text': analyzed}
        # Analyze the text
        s=analyzed

    if extraspaceremover == "on" :
        analyzed = ""
        for index, char in enumerate(s):
            if not (s[index] == " " and s[index + 1] == " "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        # Analyze the text
        s=analyzed

    if newlineremover == "on" :
        analyzed = ""
        for char in s:
            if char != "\n" and char != "\r" :
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}

    if (rempunc != "on" and fullcaps != "on" and extraspaceremover != "on" and newlineremover != "on") :

        return HttpResponse("ERROR")


    return render(request, 'analyze.html', params)


