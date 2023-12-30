# I have created this file
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,'index.html')

def analyze(request):
    # Getting the text
    djtext = request.GET.get('text', 'default')
    # checkbox value for removing Punctuations
    rmvPunc = request.GET.get('healthyBoy','default')
    # Checkbox value for converting to uppercase
    Upp = request.GET.get('FullCaps','default')
    # Checkbox for removing New Lines
    Nlr = request.GET.get('NLR','default')
    # checkbox for removing Extra Space
    Exr = request.GET.get('EXR','default')
    # checkbox for counting characters
    cc = request.GET.get('CC','default')
    # checkbox for counting @
    cnt = request.GET.get('@count','default')

    # checking which checkbox is on
    if rmvPunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed

    if(Upp == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Changed To Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed

    if(Nlr == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {'purpose': 'After removing lines', 'analyzed_text': analyzed}
        djtext = analyzed

    if (Exr == "on"):
        analyzed = ""
        for idx, char in enumerate(djtext):
            if djtext[idx] == " " and djtext[idx+1] == " ":
                pass
            else:
                analyzed = analyzed + char
        params = {'purpose': 'After Removing Extra Space', 'analyzed_text': analyzed}
        djtext = analyzed

    if (cc == "on"):
        cnt = 0
        for char in djtext:
            if char not in range(0,10):
                cnt = cnt + 1

        analyzed = f"The No. of Character in the given text are {cnt}"
        params = {'purpose': 'Count of Character is', 'analyzed_text': analyzed}

    if (cnt == "on"):
        cntt = 0
        for char in djtext:
            if char == "@":
                cntt = cntt + 1

        analyzed = f"The No. of '@' Character in the given text are {cntt}"
        params = {'purpose': 'Count of Character is', 'analyzed_text': analyzed}

    if(rmvPunc != "on" and Nlr != "on" and Exr != "on" and cc != "on" and Upp != "on" and cnt != "on"):
        return HttpResponse("Please select a Valid operation...")

    return render(request, 'analyze.html', params)
