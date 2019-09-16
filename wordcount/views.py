from django.http import HttpResponse
from django.shortcuts import render
import operator


def homepage(request):
    return render(request, "home.html")


def count(request):
    fulltext = request.GET['fulltext']
    print(fulltext)
    wordlist = fulltext.split()

    wordCount = {}
    for word in wordlist:
        if word in wordCount:
            # Increase
            wordCount[word] += 1
        else:
            # add to the dictionary
            wordCount[word] = 1

    SortedWords = sorted(
        wordCount.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, "count.html", {'fulltext': fulltext, 'count': len(wordlist), 'SortedWords': SortedWords})


def about(request):
    return render(request, "about.html")
