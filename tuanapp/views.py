
from datetime import datetime

from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse
from tuanapp.models import Tuan, Person, Comment
from tuanapp import models
from django import forms
from django.contrib import auth
from django.contrib.auth.models import User

def index(request):
    warning1 = 'Are you Ready'
    warning2 = 'for Tuan??'
    alert_type = "alert-info"
    tuan_list = Tuan.objects.all()
    user = request.user
    active_page = "Home"
    return render_to_response('index.html', locals() , context_instance = RequestContext(request))

def create_tuan(request):
    warning1 = 'Are you Ready'
    warning2 = 'for Tuan??'
    alert_type = "alert-info"
    tuan_list = Tuan.objects.all()
    active_page = "KaiTuan"
    return render_to_response('create_tuan.html', locals() , context_instance = RequestContext(request))

def insert(request):
    if request.method == 'GET':
        return HttpResponseRedirect('/')
    user= request.user

    warning1 = 'Ready'
    warning2 = 'for insert'
    alert_type = "alert-info"
    if not user.is_authenticated(): 
    	request.session['login_from'] = request.META.get('HTTP_REFERER', '/index/')
    	return render_to_response('login.html',context_instance=RequestContext(request))

    rest_name = request.POST['new_rest_name']
    min_num = request.POST['new_min_num']
    max_num = request.POST['new_max_num']
    if min_num > max_num:
        warning1 = 'Dear Qin!'
        warning2 = 'Insert new Tuan failed, minimum number should be less than max number'
        alert_type = "alert-danger"
        active_page = "KaiTuan"
        return render_to_response('create_tuan.html', locals(), context_instance = RequestContext(request))

    init = user.username
    creator = Person.objects.get(user=user)
    date = request.POST['new_date']
    if date == "":
        warning1 =  "Dear %s"%init
        warning2 = ', the input Date can not be empty!'
        alert_type = "alert-danger"
        active_page = "KaiTuan"
        return render_to_response('create_tuan.html', locals(), context_instance = RequestContext(request))
    elif len(rest_name) == 0:
        warning1 = 'Dear Qin!'
        warning2 = 'Insert new Tuan failed, resturant should not be empty...'
        alert_type = "alert-danger"
        active_page = "KaiTuan"
        return render_to_response('create_tuan.html', locals(), context_instance = RequestContext(request))
    else:
        try:
            tmp = Tuan.objects.get(init=init, date=date)
            warning1 =  "Dear %s"%init
            warning2 =  ", you have already created the activity on %s. Please update your Tuan instead of creating new one." % date
            alert_type = "alert-warning"
            active_page = "KaiTuan"
            return render_to_response('create_tuan.html', locals(), context_instance = RequestContext(request))
        except Tuan.DoesNotExist:
            warning1 =  "Dear %s"%init
            warning2 =  ", you didn't initiate Tuan before, create Tuan for %s."%init
            alert_type = "alert-success"
            newtuan = Tuan()
            newtuan.rest_name = rest_name
            newtuan.min_num = min_num
            newtuan.max_num = max_num
            newtuan.init = init
            newtuan.date = date
            newtuan.save()
            creator.joined_tuan.add(newtuan)
            creator.save()
        tuan_list = Tuan.objects.all()
        active_page = "Home"
        return render_to_response('index.html', locals(), context_instance = RequestContext(request))

def update(request):
    if request.method == 'GET':
        return HttpResponseRedirect('/')
    user = request.user
    warning1 = 'Ready'
    warning2 = 'for update'
    alert_type = "alert-info"
    upd_id = int(request.POST['upd_id'])
    upd_rest_name = request.POST['upd_rest_name']
    upd_min_num = request.POST['upd_min_num']
    upd_max_num = request.POST['upd_max_num']
    upd_date = request.POST['upd_date']

    upd_tuan = Tuan.objects.get(id=upd_id)
    upd_crt_num = int(upd_tuan.crt_num)

    if len(upd_rest_name) == 0:
        warning1 = 'Dear %s!' % user.username
        warning2 = 'update tuan failed, resturant name cannot be empty'
        alert_type = "alert-danger"
    elif int(upd_max_num) < upd_crt_num:
        warning1 = 'Dear %s!' % user.username
        warning2 = 'Current participant number is larger than your updated max participant number, update failed...'
        alert_type = 'alert-danger'
    else:
        upd_progress = int(float(upd_crt_num)/int(upd_max_num)*100)
        Tuan.objects.filter(id=upd_id).update(rest_name=upd_rest_name, max_num=upd_max_num, date=upd_date, progress=upd_progress)
        warning1 =  "Dear %s!" % user.username
        warning2 =  "Update successed!"
        alert_type = "alert-success"
    tuan_list = Tuan.objects.filter(init=user.username)
    active_page = "MyTuan"
    return render_to_response('my_tuan.html', locals(), context_instance = RequestContext(request))

def vote(request):
    if request.method == 'GET':
        return HttpResponseRedirect('/')
    warning1 = 'Ready'
    warning2 = 'for vote'
    alert_type = "alert-info"
    vote_id = int(request.POST['vote_id'])
    user = request.user
    print "leo debug =>", user.is_authenticated()
    if not user.is_authenticated():
    	request.session['login_from'] = request.META.get('HTTP_REFERER', '/index/')
    	return render_to_response('login.html',context_instance=RequestContext(request))

    upd_tuan = Tuan.objects.get(id=vote_id)
    upd_crt_num = int(upd_tuan.crt_num)
    upd_min_num = int(upd_tuan.min_num)
    upd_max_num = int(upd_tuan.max_num)
    if upd_crt_num == upd_max_num:
        warning1 = "Dear Qin!"
        warning2 = "This Tuan is full now... Please choose another one~"
        alert_type = "alert-danger"
    else:
        upd_crt_num += 1
        upd_progress = int(float(upd_crt_num)/upd_max_num*100)
        Tuan.objects.filter(id=vote_id).update(crt_num=upd_crt_num, progress=upd_progress)	        
        upd_user = Person.objects.get(user_id=user.id)
        upd_user.joined_tuan.add(upd_tuan)
        upd_user.save()
        #upd_tuan.save()
        warning1 =  "Dear!"
        warning2 =  "Vote successed!"
        alert_type = "alert-success"

    tuan_list = Tuan.objects.all()
    active_page = "Home"
    return render_to_response('index.html', locals(), context_instance = RequestContext(request))

def delete(request):
    if request.method == 'GET':
        return HttpResponseRedirect('/')
    user = request.user
    warning1 ='Delete'
    warning2 = 'OK'
    alert_type = "alert-success"
    del_id = int(request.POST['del_id'])
    tuan = Tuan.objects.get(id=del_id)
    tuan.delete()
    tuan_list = Tuan.objects.filter(init=user.username)
    active_page = "MyTuan"
    return render_to_response('my_tuan.html', locals(), context_instance = RequestContext(request))

def acc_login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = auth.authenticate(username = username, password=password)
    if user is not None:
        auth.login(request,user)
        active_page = ""
        return render_to_response('redirect.html',{"refresh_url":request.session['login_from']},context_instance=RequestContext(request))
    else:
        return render_to_response('login.html',{'login_err':'Warning: wrong name or wrong password!'},context_instance=RequestContext(request))

def logout_view(request):
    user= request.user
    auth.logout(request)
    request.session['login_from'] = request.META.get('HTTP_REFERER', '/index/')
    return render_to_response('redirect.html',{"refresh_url":request.session['login_from']},context_instance=RequestContext(request))

def Login(request):
    request.session['login_from'] = request.META.get('HTTP_REFERER', '/index/')
    return render_to_response('login.html',context_instance=RequestContext(request))

def register(request):
    print "method==>",request.method
    print 'refer==>',request.META.get("HTTP_REFERER")
    request.session['login_from'] = request.META.get('HTTP_REFERER', '/index/')
    return render_to_response("register.html",context_instance=RequestContext(request))

def register_create(request):
    if request.method == "POST":
        html_from = request.session['login_from']
        print "html is from==>",html_from
        errors = ""
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        email = request.POST.get('email')
        filter_result = User.objects.filter(username = username)
        #print "filter_Result is ",filter_result
        if len(filter_result) >0:
            errors ='Username already exists, please try another username.'
            return render_to_response("register.html", locals(),context_instance=RequestContext(request))

        if password1 != password2:
            errors='Two passwords differ, please try again.'
            return render_to_response('register.html',locals(),context_instance=RequestContext(request))

        user= User.objects.create_user(
            username = username,
            password = password1,
            email = email,
            )
        user.save
        tuan_user = models.Person()
        tuan_user.user_id = user.id
        tuan_user.save()
        user = auth.authenticate(username=username, password=password1)
        auth.login(request,user)
        return render_to_response('redirect.html',{"refresh_url":html_from},context_instance=RequestContext(request))


def my_tuan(request):
    user = request.user
    warning1 = 'Dear %s, are you Ready' % user.username
    warning2 = 'for Tuan??'
    alert_type = "alert-info"
    person = Person.objects.get(user_id=user.id)
    person_name = user.username
    tuan_list = Tuan.objects.filter(init=person_name)
    joined_tuan_list = person.joined_tuan.all()
    active_page = "MyTuan"
    return render_to_response('my_tuan.html', locals() , context_instance = RequestContext(request))


def tuan_detail(request, tuan_id):
    tuan = Tuan.objects.get(id = tuan_id)

    if request.method == 'POST':
        content = request.POST.get('content')
        user = request.user
        now = datetime.now()
        comment = Comment.objects.create(
        tuan = tuan, content = content, person = Person.objects.get(user = user),
        published  = now)
        comment.save()

    comments = tuan.comment_set.all()
    return render(request, 'detail_tuan.html', {'tuan': tuan, 'comments': comments})

