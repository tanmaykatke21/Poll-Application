from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login,logout,authenticate

def ulogin(request):
	if request.user.is_authenticated:
		return redirect("uwelcome")
	else:
		if request.method == "POST":
			un = request.POST.get("un")
			pw = request.POST.get("pw")
			usr = authenticate(username=un,password=pw)
			if usr is None:
				return render(request,"ulogin.html",{"msg":"invalid username/password"})
			else:
				login(request,usr)
				return redirect("uwelcome")
		else:	
			return render(request,"ulogin.html")

def usignup(request):
	if request.user.is_authenticated:
		return redirect("uwelcome")
	else:
		if request.method == "POST":
			un = request.POST.get("un")
			pw1 = request.POST.get("pw1")
			pw2 = request.POST.get("pw2")
			if pw1 == pw2:
				try:
					usr = User.objects.get(username=un)
					return render(request,"usignup.html",{"msg":"user already exists"})
				except User.DoesNotExist:
					usr = User.objects.create_user(username=un,password=pw1)
					usr.save()
					return redirect("ulogin")
			else:
				return render(request,"usignup.html",{"msg":"password did not match"})
		else:
			return render(request,"usignup.html")

def uwelcome(request):
	if request.user.is_authenticated:
		return render(request,"uwelcome.html")
	else:
		return redirect("ulogin")

def ulogout(request):
	logout(request)
	return redirect("ulogin")

def ucp(request):
	if request.user.is_authenticated:
		if request.method == "POST":
			pw1 = request.POST.get("npw1")
			pw2 = request.POST.get("npw2")
			pw = User.objects.get(password=request.user.password)
			if (pw1==pw2):
				try:
					usr = User.objects.get(username=request.user.username)
					usr.set_password(pw1)
					usr.save()
					return redirect("ulogin")
				except User.DoesNotExist:
					return render(request,"ucp.html",{"msg":"User does not exists"})
			else:
				return render(request,"ucp.html",{"msg":"password did not match"})
		else:
			return render(request,"ucp.html")
	else:
		return redirect("ulogin")			
