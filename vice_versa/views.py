from django.shortcuts import render

def home(request):
	return render(request, 'home.html')

def reverse(request):
	user_text = request.GET['usertext']
	count_words = len(user_text.split())
	reversed_txt = user_text[::-1]
	return render(request, 'reverse.html', {'usertext':user_text, 'reversedtxt': reversed_txt, 'countw':count_words})