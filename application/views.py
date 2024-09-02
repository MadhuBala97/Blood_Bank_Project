from django.shortcuts import render,redirect
from application.models import Newuser,Blood,Camp,Bloodrequest,Bloodbank
def home(request):
	return render(request,"template/index.html")
def about(request):
	return render(request,"template/about.html")
def doctors(request):
	return render(request,"template/doctors.html")
def blog(request):
	return render(request,"template/blog.html")
def contact(request):
	return render(request,"template/contact.html")
def login(request):
	return render(request,"template/login.html")
def registercode(request):
	if request.method=="POST":
		a=request.POST['t1']
		b=request.POST['t2']
		c=request.POST['t3']
		d=request.POST['t4']
		e=request.POST['t5']
		f=request.POST['t6']
		g=request.POST['t7']
		data2=Newuser.objects.filter(email=b).count()
		if data2==0:
			data=Newuser(name=a,age=b, gender=c, email=d, password=e, address=f, confirm=g)
			data.save()
			request.session['email'] = d
			return redirect("/user/")
		else:
			user = "This Email Is All Ready Register"
			return render(request,"template/msg.html",{"msg":user})	
	else:
		redirect('/index/')
def logincode(request):
	if request.method=="POST":
		email= request.POST['t1']
		pwd= request.POST['t2']
		if email == "admin@gmail.com" and pwd=="admin":
			request.session['admin'] = email
			return redirect("/admin1/")
		else:
			user = Newuser.objects.filter(email=email, password=pwd).count()
			if(user==0):	
				user = "Not match"
				return render(request,"template/msg.html",{"msg":user})
			else:
				request.session['email'] = email
				return redirect("/user/")
def admin1(request):
	if request.session.has_key('admin'):
		email = request.session['admin']
		return render(request,"template/admin.html", {"usernames" : email})
	else:
		return redirect('/login/')
def addblood(request):
	if request.session.has_key('admin'):
		return render(request,"template/addblood.html")
	else:
		return redirect('/login/')
def addbloodcode(request):
	if request.session.has_key('admin'):
		if request.method=="POST":
			a=request.POST['t1']
			b=request.POST['t2']
			c=request.POST['t3']
			d=request.POST['t4']
			e=request.POST['t5']
			f=request.POST['t6']
			data=Blood(btype=a,state=b, address=c, bankname=d, nounit=e, price=f)
			data.save()
			return redirect('/showblood/')
		else:
			return redirect('/addblood/')
		
	else:
		return redirect('/login/')
def showblood(request):
	if request.session.has_key('admin'):
		email = request.session['admin']
		data=Blood.objects.all()
		return render(request,"template/showblood.html", {"usernames" : email,"alldata":data})
	else:
		return redirect('/login/')
def showrequest(request):
	if request.session.has_key('admin'):
		email = request.session['admin']
		data=Bloodrequest.objects.all()
		return render(request,"template/showrequest.html", {"usernames" : email,"alldata":data})
	else:
		return redirect('/login/')
def deleteblood(request,pk):
	id=pk
	Blood.objects.filter(p_id=id).delete()
	return redirect("/showblood/")

def addcamp(request):
	if request.session.has_key('admin'):
		return render(request,"template/addcamp.html")
	else:
		return redirect('/login/')
def addcampcode(request):
	if request.session.has_key('admin'):
		if request.method=="POST":
			a=request.POST['t1']
			b=request.POST['t2']
			c=request.POST['t3']
			d=request.POST['t4']
			e=request.POST['t5']
			data=Camp(cname=a,state=b, address=c, date=d, noday=e)
			data.save()
			return redirect('/showcamp/')
		else:
			return redirect('/addcamp/')
		
	else:
		return redirect('/login/')
def showcamp(request):
	if request.session.has_key('admin'):
		email = request.session['admin']
		data=Camp.objects.all()
		return render(request,"template/showcamp.html", {"usernames" : email,"alldata":data})
	else:
		return redirect('/login/')
def deletecamp(request,pk):
	id=pk
	Camp.objects.filter(p_id=id).delete()
	return redirect("/showcamp/")
def showuser(request):
	if request.session.has_key('admin'):
		email = request.session['admin']
		data=Newuser.objects.all()
		return render(request,"template/showuser.html", {"usernames" : email,"alldata":data})
	else:
		return redirect('/login/')
def user(request):
	if request.session.has_key('email'):
		email = request.session['email']
		data=Newuser.objects.filter(email=email).all()
		return render(request,"template/user.html", {"usernames" : data})
	else:
		return redirect('/login/')
def u_showblood(request):
	if request.session.has_key('email'):
		email = request.session['email']
		data=Blood.objects.all()
		return render(request,"template/u_showblood.html", {"usernames" : email,"alldata":data})
	else:
		return redirect('/login/')
def bloodrequest(request):
	if request.session.has_key('email'):
		if request.method=="POST":
			a=request.POST['t1']
			b=request.POST['t2']
			c=request.POST['t3']
			d=request.POST['t4']
			e=request.POST['t5']
			f=request.POST['t6']
			e=int(e)
			a=int(a)
			total=e*a
			data=Bloodrequest(bname=d,name=b, state=f, bloodid=c, nounit=a, price=e, total=total)
			data.save()
			return redirect('/myrequest/')
		else:
			return redirect('/myrequest/')
	else:
		return redirect('/login/')
def myrequest(request):
	if request.session.has_key('email'):
		email = request.session['email']
		data=Bloodrequest.objects.filter(name=email).all()
		return render(request,"template/myrequest.html", {"alldata" : data})
	else:
		return redirect('/login/')
def deletemyrequest(request,pk):
	id=pk
	Bloodrequest.objects.filter(p_id=id).delete()
	return redirect("/myrequest/")
def u_showcamp(request):
	if request.session.has_key('email'):
		email = request.session['email']
		data=Camp.objects.all()
		return render(request,"template/u_showcamp.html", {"usernames" : email,"alldata":data})
	else:
		return redirect('/login/')
def changepwd(request):
	if request.session.has_key('email'):
		email = request.session['email']
		data=Newuser.objects.filter(email=email).all()
		return render(request,"template/changepwd.html", {"alldata" : data})
	else:
		return redirect('/login/')
def mypassword(request):
	if request.method=="POST":
		pwd= request.POST['t2']
		email = request.session['email']
		user = Newuser.objects.filter(email=email).update(password=pwd)
		return redirect("/changepwd/")
def logout(request):
	if request.session.has_key('email'):
		del request.session['email']
	if request.session.has_key('admin'):
		del request.session['admin']
	return redirect("/login/")
	
def delete_user(request,pk):
	id=pk
	Newuser.objects.filter(p_id=id).delete()
	return redirect("/showuser/")

def updateuser(request,pk):
	id=pk
	data=Newuser.objects.filter(p_id=id).all()
	return render(request,"template/updateuser.html", {"alldata" : data})

def savedata(request):
    if request.session.has_key('admin'):
        if request.method=="POST":
            a=request.POST['t1']
            b=request.POST['t2']
            c=request.POST['t3']
            d=request.POST['t4']
            e=request.POST['t5']
            f=request.POST['t6']
            id=request.POST['t7']
            Newuser.objects.filter(p_id=id).update(name=a,age=b, gender=c,email=d, password=e, address=f)
            return redirect('/showuser/')
        else:
        	return redirect('/showuser/')
    else:
    		return redirect('/login/')
def bloodbank (request):
    return render(request,'template/doctors.html')

def bloodbankcode(request):
	if request.method=="POST":
		a=request.POST['t1']
		b=request.POST['t2']
		c=request.POST['t3']
		d=request.POST['t4']
		e=request.POST['t5']
		data=Bloodbank(no=a,h_name=b,address=c,blood_type=d,av_or_not=e)
		data.save()
		return redirect('/showbloodbank/')
	else:
		return redirect('/doctors/')
			
def showbloodbank(request):
    data=Bloodbank.objects.all()
    return render (request,'template/showbloodbank.html',{"alldata":data})