from django.shortcuts import render,redirect
from collegeapp.models import Department,User,Teacher,Student
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
# Create your views here.




def dep_add(request):
    if request.method=='POST':
        d=request.POST['dep']
        x=Department.objects.create(Dep_Name=d)
        x.save()
        return HttpResponse('success')
    else:
        return render(request,'dep_add.html')
    

def index(request):
    return render(request,'index.html')
# reister Teacher
def reg_teacher(request):
    if request.method=='POST':
        d=request.POST['dep']
        f=request.POST['fname']
        l=request.POST['lname']
        e=request.POST['email']
        u=request.POST['uname']
        p=request.POST['password']
        a=request.POST['age']
        ad=request.POST['address']
        q=request.POST['qual']
        x=User.objects.create_user(first_name=f,last_name=l,email=e,username=u,password=p,usertype='Teacher')
        x.save()
        y=Teacher.objects.create(tid=x,depid_id=d,Age=a,Address=ad,Qualification=q)
        y.save()
        return HttpResponse('successfully registered')
    
    else:
        x=Department.objects.all()
        return render(request,"reg_teacher.html",{'x1':x})
    
def mainhome(request):
    return render(request,'mainhome.html')
# REGISTER STUDENT
def reg_student(request):
    if request.method=='POST':
        d=request.POST["dep"]
        f=request.POST["fname"]
        l=request.POST["lname"]
        e=request.POST["email"]
        u=request.POST["uname"]
        p=request.POST["password"]
        a=request.POST["age"]
        ad=request.POST["address"]
        x = User.objects.create_user(first_name=f,last_name=l,email=e,username=u,password=p,usertype="Student",is_active=False)
        x.save()
        y=Student.objects.create(depid_id=d,sid=x,Age=a,Address=ad)
        y.save()
        return HttpResponse('successfully registered')
    else:
        x=Department.objects.all()
        return render(request,'reg_student.html',{'x1':x})
    


# VIEW STUDENT
def viewstudent(request):
    x=Student.objects.all()
    return render(request,"viewstudent.html",{'x1':x})

def approve(request,aid):
    st=Student.objects.get(id=aid)
    st.sid.is_active=True
    st.sid.save()
    return redirect(viewstudent)

def adminhome(request):
    return (request,"mainhome.html")
def teacherhome(request):
    return render(request,"teacherhome.html")
def studenthome(request):
    return render(request,'studenthome.html')
# login
def logins(request):
    if request.method=='POST':
        u=request.POST['username']
        p=request.POST['password']
        user=authenticate(request,username=u,password=p)
        if user is not None and user.is_superuser==1:
            return redirect(adminhome)
        elif user is not None and user.usertype=='Teacher':
            login(request,user)
            request.session['teach_id']=user.id
            return redirect(teacherhome)
        elif user is not None and user.usertype=='Student' and user.is_active==1:
            login(request,user)
            request.session['std_id']=user.id
            return redirect(studenthome)
        else:
            return HttpResponse("NOT VALID")
    else:
        return render(request,'logins.html')
#  Approved student
def approved_stview(request):
    x=User.objects.filter(is_active=1,usertype='Student')
    return render(request,'approved_stview.html',{'x1':x})

    
# update student profile
def updatest(request):
    stud=request.session.get('std_id')
    student=Student.objects.get(sid_id=stud)
    user=User.objects.get(id=stud) 
    return render(request,"updatest.html",{'view':student,"data":user})

def updatestudent(request,uid):
    if request.method=='POST':
        stud=Student.objects.get(id=uid)
        sid=stud.sid_id
        user=User.objects.get(id=sid)
        user.first_name=request.POST['fname']
        user.last_name=request.POST['lname']
        user.email=request.POST['email']
        user.username=request.POST['uname']
        user.save()
        stud.Age=request.POST['age']
        stud.Address=request.POST['address']
        stud.save()
        return HttpResponse('success')
    

# update teacher
def updatetr(request):
    teach=request.session.get("teach_id")
    teacher=Teacher.objects.get(tid_id=teach)
    user=User.objects.get(id=teach)
    return render(request,'updatetr.html',{'view1':teacher,'data1':user}) 

def updateteacher(request,utid):
   if request.method=='POST':
       tech=Teacher.objects.get(id=utid)
       tid=tech.tid_id
       user=User.objects.get(id=tid)
       user.first_name=request.POST['fname']
       user.last_name=request.POST['lname']
       user.email=request.POST['email']
       user.username=request.POST['uname']
       user.password=request.POST['password']
       user.save()
       tech.Age=request.POST['age']
       tech.Address=request.POST['address']
       tech.Qualification=request.POST['qual']
       tech.save()
       return HttpResponse("Successfully Updated")

# display teacher details 
def viewteacher(request):
    y=Teacher.objects.all()
    return render (request,'viewteacher.html',{'y1':y})





# delete teacher details
def deletetr(request,dtid):
    x=User.objects.get(id=dtid)#foreign key 
    x.delete()
    return redirect(viewteacher)

# deletestudent details
def deletestud(request,dsid):
    y=User.objects.get(id=dsid)
    y.delete()
    return redirect(viewstudent)


# def deletetr(request,dtid):
    



def lgout(request):
    logout(request)
    return redirect(logins)