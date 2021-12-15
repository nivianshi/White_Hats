from django.shortcuts import render
from django.http import HttpResponse          
from django.core.files import  File
import sqlite3 as s

# Create your views here.

def  search_form(request):
      return render(request,"webapp/page1.html")
def  search_form1(request):
      return render(request,"webapp/login.html")

#login_form
def  fetch(request):
      if request.method=='GET':
            conn=s.connect("sqlite3\\library")
            c=conn.cursor()
            id1=request.GET["t1"]
            pswd=request.GET["p1"]
            c.execute("insert into login values(?,?)",(id1,pswd))
            conn.commit()
            conn.close()
            return render(request,"webapp/welcome.html")
            
def  update(request):
      return render(request,"webapp/update.html")

#update entry
def  update1(request):
      if  request.method=='GET':
            conn=s.connect("sqlite3\\library")
            c=conn.cursor()
            cd=request.GET["t1"]
            bn=request.GET["t2"]
            au=request.GET["t3"]
            p=request.GET["t4"]
            bp=request.GET["t5"]
            pd=request.GET["d1"]
            qty=request.GET["t6"]
            c.execute("insert into buk_update values(?,?,?,?,?,?,?)",(cd,bn,au,p,bp,pd,qty))
            conn.commit()
            conn.close()
            return render(request,"webapp/next.html")
      
def  issue(request):
      return render(request,"webapp/issue.html")

#issue records
def  issue1(request):
      conn=s.connect("sqlite3\\library")
      c=conn.cursor()
      a=request.GET["t1"]
      b=request.GET["t2"]
      n=request.GET["t3"]
      d=request.GET["t4"]
      e=request.GET["t5"]
      c.execute("insert into issue values(?,?,?,?,?)",(a,b,n,d,e))
      conn.commit()
      conn.close()
      return HttpResponse("Done")

def  issue2(request):
      return render(request,"webapp/issue.html")

def returns(request):
      return render(request,"webapp/return.html")

def  retrieves(request):
      conn=s.connect("sqlite3\\library")
      c=conn.cursor()
      bid=request.GET["t1"]
      bc=request.GET["t2"]
      bn=request.GET["t3"]
      sid=request.GET["t4"]
      na=request.GET["t5"]
      d=request.GET["t6"]
      rd=request.GET["d1"]
      c.execute("insert into returned values(?,?,?,?,?,?,?)",(bid,bc,bn,sid,na,d,rd))
      conn.commit()
      conn.close()
      return HttpResponse("Book Returned")
     
            
           

       
       
      

