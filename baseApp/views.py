

from cProfile import run
import email
from itertools import count
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from .models import podatoci,coursevi,UserCourses,UserNotes


def taskList(request):
    return HttpResponse("hello my friend")
def FindCoursesPg(request):
    allCourses = coursevi.objects.all()
   
    zapisani = UserCourses.objects.get(user=request.session['mail'])
    krajnaNiza=[]
    for somet in allCourses:
        if somet.title in zapisani.courses:
            pass
        else:
            krajnaNiza.append(somet.title)
       
    if request.method=="POST":
        if 'Filter' in request.POST:
            allCoursesi = coursevi.objects.all()
            cena = request.POST.get('FreeC',False)
            cena1= request.POST.get('PaidC',False)
            ins1 = request.POST.get('Ins1',False)
            ins2 = request.POST.get('Ins2',False)
            ins3 = request.POST.get('Ins3',False)
            inter = request.POST.get('Intermediate',False)
            Beg = request.POST.get('Begginer',False)
            Exp = request.POST.get('Expert',False)
            ExD = request.POST.get('ED',False)
            VxD = request.POST.get('VD',False)
            WxA = request.POST.get('WA',False)
            MxD = request.POST.get('MD',False)
            PxE = request.POST.get('PE',False)


            zapisanit = UserCourses.objects.get(user=request.session['mail'])
            kraNiza=[]
            for someti in allCoursesi:
                if someti.title in zapisanit.courses:
                    pass
                else:
                    if  someti.price==cena1:
                        kraNiza.append(someti.title)
                    if  someti.price==cena:
                        kraNiza.append(someti.title)
                    if  someti.instructor==ins1:
                        kraNiza.append(someti.title)
                    if  someti.instructor==ins2:
                        kraNiza.append(someti.title)
                    if  someti.instructor==ins3:
                        kraNiza.append(someti.title)
                    if someti.dificulty==inter:
                        kraNiza.append(someti.title)
                    if someti.dificulty==Beg:
                        kraNiza.append(someti.title)
                    if someti.dificulty==Exp:
                        kraNiza.append(someti.title)
                    if someti.title==ExD:
                        kraNiza.append(someti.title)
                    if someti.title==PxE:
                        kraNiza.append(someti.title)
                    if someti.title==MxD:
                        kraNiza.append(someti.title)
                    if someti.title==VxD:
                        kraNiza.append(someti.title)
                    if someti.title==WxA:
                        kraNiza.append(someti.title)

                    
            return render(request,'baseApp/FindCourses.html',{'potr':kraNiza})
            
             
        elif 'kopce' in request.POST:
            select = request.POST.get('testoj',False)
            korisnik = request.session['mail']
            najaven = UserCourses.objects.get(user=korisnik)
            SiteCourses = coursevi.objects.all()
            if select in najaven.courses:
                pass
            else:
                najaven.courses = najaven.courses + select + ','
                
                najaven.save()
            konkretnaNiza =[]
            for item in SiteCourses:
                if item.title in najaven.courses:
                    pass
                else:
                    konkretnaNiza.append(item)
                
            return render(request,'baseApp/FindCourses.html',{'potr':konkretnaNiza})

    return render(request,'baseApp/FindCourses.html',{'potr':krajnaNiza})
def ViewCoursesPg(request):
    if request.method=="POST":
        imeCourses = request.POST.get('ime',False)
        site = UserCourses.objects.get(user=request.session['mail'])
        zbor = imeCourses + ','
        sit = ""+site.courses+""
        if zbor in site.courses:
            sit = sit.replace(zbor,'')
            site.courses = sit
            site.save()
            return redirect('/courses')

    promenlive= request.session['naslov']

    return render(request,'baseApp/ViewCourses.html',{'VTitle':promenlive})
       

        
    broj1 = request.session['mail']
    broj2 = request.session['first']
    return render(request,'baseApp/ViewCourses.html',{'broj1':broj1,
    'broj2':broj2})
def HomePg(request):
   
   return render(request, 'baseApp/home.html')
def IndexPg(request):
    if request.method =="POST":
        title = request.POST.get('title',False)
        duration = request.POST.get('duration',False)
        desc = request.POST.get('description',False)
        inst = request.POST.get('Instructor',False)
        quiz = request.POST.get('Quiz',False)
        diff = request.POST.get('dificulty',False)
        pri = request.POST.get('Price',False)
        courses = coursevi()
        courses.title = title
        courses.duration = duration
        courses.description = desc
        courses.dificulty = diff
        courses.instructor = inst
        courses.testing = quiz
        courses.price = pri
        courses.save()
    return render(request,'baseApp/index.html')
def NotesPg(request):
     
    if request.method=="POST":
        if 'DeleteNote' in request.POST:
            sub = request.POST.get('delSubject')
            noTek = request.POST.get('delNote')
            objNote=UserNotes.objects.filter(subject=sub,note=noTek)
            objNote.delete()
        elif 'takeNote' in request.POST:
            newNote = UserNotes()
            newNote.user = request.session['mail']
            newNote.subject = request.POST.get('subject',False)
            newNote.note = request.POST.get('note',False)
            newNote.save()
    broj1 = request.session['mail']
    broj2 = request.session['first']

    takenNotes = UserNotes.objects.all()

    return render(request,'baseApp/notes.html',{'broj1':broj1,
    'broj2':broj2,'notes':takenNotes})    
def CertificationsPg(request):
    broj1 = request.session['mail']
    broj2 = request.session['first']
    return render(request,'baseApp/analytics.html',{'broj1':broj1,
    'broj2':broj2})
def AnalyticsPg(request):
    broj1 = request.session['mail']
    broj2 = request.session['first']
    return render(request,'baseApp/analytics.html',{'broj1':broj1,
    'broj2':broj2}
    )    
def ProfilePg(request):
    broj1 = request.session['mail']
    broj2 = request.session['first']
    broj3 = request.session['last']
    broj4 = request.session['country']
    broj5 = request.session['age']

   
    return render(request,'baseApp/profile.html',{'broj1':broj1,
    'broj2':broj2,
    'broj3':broj3,
    'broj4':broj4,
    'broj5':broj5
    
    
    })
def CoursesPg(request):
    if request.method=="POST":
        Vtitle = request.POST.get('VTitle',True)
        request.session['naslov'] = Vtitle
        return redirect('/viewCourses')
    broj1 = request.session['mail']
    broj2 = request.session['first']
    korisnik = request.session['mail']
    najaven = UserCourses.objects.get(user=korisnik)
    
    niza = najaven.courses.split(',')
    niza.remove('')
    return render(request,'baseApp/courses.html',{'broj1':broj1,
    'broj2':broj2,
    'najaven':niza
    })      


def LoginPg(request):
    if request.method == "POST":
        Lemail = request.POST.get('logMail',False)
        Lpass = request.POST.get('logPass',False)

        user = authenticate(username=Lemail,password=Lpass)
        
        if user is not None:
            login(request,user)
            fname = user.first_name
            pod = podatoci.objects.get(email=Lemail) 
            request.session['mail'] = pod.email
            request.session['first'] = pod.firstName
            request.session['last'] = pod.lastName
            request.session['country'] = pod.country
            request.session['age'] = pod.Age
            

            return redirect('/profile')
        else:
            greska = 'invalid credentials'
            return render(request,'baseApp/login.html',{'greska':greska})



    return render(request, 'baseApp/login.html')

def RegisterPg(request):
   if request.method == "POST":
        fname = request.POST.get('fname',False)
        lname = request.POST.get('lname',False)
        email = request.POST.get('email',False)
        pass1 = request.POST.get('pass1',False)
        country = request.POST.get('country',False)
        age = request.POST.get('age',False)
        
        
       
       

        podatok = podatoci()
        podatok.poId = 1
        podatok.firstName = fname
        podatok.lastName = lname
        podatok.country = country
        podatok.email = email
        podatok.Age = age
        pok = podatoci.objects.all()
        korisnik = "Korisnikot "
        for por in pok:
            if fname in por.firstName:
                korisnik = korisnik + fname + " vejke postoi"
                return render(request,'baseApp/register.html',{'korisnik':korisnik})
            if email in por.email:
                korisnik = korisnik + email + " vejke postoi"
                
                return render(request,'baseApp/register.html',{'korisnik':korisnik})

        myuser = User.objects.create_user(email,fname,pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        podatok.save()

        UserCasovi = UserCourses()
        UserCasovi.user = email
        UserCasovi.courses=''
        UserCasovi.save()

        
        return redirect('/login')
   else:
        return render(request,'baseApp/register.html')

            
   
  
   

   




 

   
  
  
