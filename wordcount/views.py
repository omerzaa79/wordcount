# from django.http import HttpResponse
from django.shortcuts import render
import operator


def home(request):
	return render(request, 'home.html')


def about(request):
	return render(request, 'about.html')


def count(request):
	fulltext = request.GET['fulltext'] # gets the input by user in textarea on homepage
	wordlist = fulltext.split() # makes a list words on spaces
	worddictionary = {} # defining a empty dictionary for words counting
	for word in wordlist:
		if word in worddictionary:
			worddictionary[word] += 1 # { 'the': 2, 'am':5 } etc
		else:
			worddictionary[word] = 1
	#  and .items() makes it [('the', 2),('am',5)]
	sortedworddictionary = sorted(worddictionary.items(), key=operator.itemgetter(1), reverse=True)
	# sortedworddictionary = sorted(worddictionary.items(), key=lambda word: word[1], reverse=True)
	context = {
		'fulltext': fulltext,
		'count': len(wordlist),
		'sortedworddictionary': sortedworddictionary
	}
	return render(request, 'count.html', context)