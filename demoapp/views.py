from django.shortcuts import render
from demoapp.models import Student
from demoapp.models import StudentDetails
from django.http import HttpResponse

def site(Request):
	return render(Request,'site.html')


def sign(Request):
	return render(Request,'signup.html')

def signup(Request):
	user=Request.GET.get('uname')
	password1=Request.GET.get('pass')
	p=StudentDetails(username=user,password=password1)
	p.save()
	return render(Request,'signup.html')

def log(Request):
	return render(Request,'log.html')

def login(Request):
	flag=False
	name=Request.GET.get('name')
	password=Request.GET.get('pass')
	users=StudentDetails.objects.all()
	for i in users:
		if(i.username==name and i.password==password ):
			flag=True
			alldata=StudentDetails.objects.all()
			return render(Request,'insert.html',{'Data':alldata})
	if(flag==False):
		return HttpResponse("Username and password Are not match")



def insert(Request):
	return render(Request,'insert.html')

def insertView(Request):
	name=Request.GET.get('s_name')
	email=Request.GET.get('s_email')
	number=Request.GET.get('s_number')
	s=Student(name=name,email=email,number=number)
	s.save()

	return render(Request,'insert.html')

def display(Request):

	alldata=Student.objects.all()
	return render(Request,'display.html',{'Data':alldata})

def deleteView(Request):
	id1=Request.GET.get('id')
	delete=Student.objects.get(id=id1)
	delete.delete()
	alldata=Student.objects.all()
	return render(Request,'display.html',{'Data':alldata})

def updateView(Request):
	id1=Request.GET.get('id')
	update=Student.objects.get(id=id1)
	#alldata=Student.objects.all()
	return render(Request,'update.html',{'Data':update})

def updateData(Request):
	name1=Request.POST.get('name')
	email1=Request.POST.get('email')
	number1=Request.POST.get('number')

	id2=Request.GET.get('id')
	u1=Student.objects.get(id=id2)

	u1.name = name1
	u1.email = email1
	u1.number = number1
	u1.save()

	alldata=Student.objects.all()
	return render(Request,'display.html',{'Data':alldata})