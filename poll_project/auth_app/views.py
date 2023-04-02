from django.shortcuts import render

def ulogin(request):
	return render(request,"ulogin.html")

def usignup(request):
	return render(request,"usignup.html")

def uwelcome(request):
	return render(request,"uwelcome.html")
