
from datetime import datetime

from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, HttpResponse, Http404
from tuanapp.models import Tuan, Person, Comment
from tuanapp.forms import TuanForm
from django.contrib import auth
from django.contrib.auth.models import User

def user_authenticated(func):
    def handle_args(request):
        if not request.user.is_authenticated():
            request.session['login_from'] = request.META.get('HTTP_REFERER', '/index/')
            return render_to_response('login.html',context_instance=RequestContext(request))
        return func(request)
    return handle_args


def index(request):
    warning1 = 'Are you Ready'
    warning2 = 'for Tuan??'
    alert_type = "alert-info"
    tuan_list = Tuan.objects.all()
    user = request.user
    if request.user.is_authenticated():
        person = Person.objects.get(user=user)
        for tuan in tuan_list:
            if tuan in person.joined_tuan.all():
                tuan.joined = True
            else:
                tuan.joined = False
    else:
        for tuan in tuan_list:
            tuan.joined = False
    
    active_page = "Home"
    return render_to_response('index.html', locals() , context_instance = RequestContext(request))


@user_authenticated
def create_tuan(request):
    if request.method == 'POST':
        form = TuanForm(request.POST)
        if form.is_valid():
            if form.cleaned_data["min_num"] <= form.cleaned_data["max_num"]:
                tuan = form.save(commit = False)
                tuan.initiator = request.user.username
                tuan.save()
                person = Person.objects.get(user=request.user)
                person.joined_tuan.add(tuan)
                person.save()
                return HttpResponseRedirect('/')
            else:
                warning1, warning2, alert_type = (
                    "Dear Qin!",
                    "Failed to create new tuan: Min participates exceeded max participates.",
                    "alert-danger",
                )
        else:
            warning1, warning2, alert_type = (
                "Dear Qin!",
                "Failed to create new tuan. Please correct your inputs.",
                "alert-danger",
            )
    else:
        warning1, warning2, alert_type = (
            "Are you Ready",
            "for Tuan??",
            "alert-info",
        )
        form = TuanForm()
    active_page = "KaiTuan"
    return render(request, 'create_tuan.html', locals())


def update(request):
    if request.method == 'GET':
        return HttpResponseRedirect('/')
    user = request.user
    person = Person.objects.get(user_id=user.id)
    warning1 = 'Ready'
    warning2 = 'for update'
    alert_type = "alert-info"
    upd_id = int(request.POST['upd_id'])
    upd_rest_name = request.POST['upd_rest_name']
    upd_min_num = request.POST['upd_min_num']
    upd_max_num = request.POST['upd_max_num']
    upd_start_time = request.POST['upd_start_time']

    upd_tuan = Tuan.objects.get(id=upd_id)
    upd_current_num = int(upd_tuan.current_num)

    if len(upd_rest_name) == 0:
        warning1 = 'Dear %s!' % user.username
        warning2 = 'update tuan failed, resturant name cannot be empty'
        alert_type = "alert-danger"
    elif int(upd_max_num) < upd_current_num:
        warning1 = 'Dear %s!' % user.username
        warning2 = 'Current participant number is larger than your updated max participant number, update failed...'
        alert_type = 'alert-danger'
    else:
        Tuan.objects.filter(id=upd_id).update(
            rest_name=upd_rest_name, max_num=upd_max_num,
            start_time=upd_start_time, current_num=upd_current_num)
        warning1 =  "Dear %s!" % user.username
        warning2 =  "Update successed!"
        alert_type = "alert-success"
    tuan_list = Tuan.objects.filter(initiator=user.username)
    active_page = "MyTuan"
    return render_to_response('my_tuan.html', locals(), context_instance = RequestContext(request))


@user_authenticated
def vote(request):
    if request.method == 'GET':
        return HttpResponseRedirect('/')
    warning1 = 'Ready'
    warning2 = 'for vote'
    alert_type = "alert-info"
    vote_id = int(request.POST['vote_id'])
    vote_type = request.POST['vote_type']
    referer = request.META['HTTP_REFERER']
    user = request.user

    upd_tuan = Tuan.objects.get(id=vote_id)
    upd_current_num = int(upd_tuan.current_num)
    upd_min_num = int(upd_tuan.min_num)
    upd_max_num = int(upd_tuan.max_num)
    if vote_type == "join":
        if upd_current_num == upd_max_num:
            warning1 = "Dear Qin!"
            warning2 = "This Tuan is full now... Please choose another one~"
            alert_type = "alert-danger"
        else:
            upd_current_num += 1
            Tuan.objects.filter(id=vote_id).update(current_num=upd_current_num)
            upd_user = Person.objects.get(user_id=user.id)
            upd_user.joined_tuan.add(upd_tuan)
            upd_user.save()
            warning1 =  "Dear!"
            warning2 =  "Vote successed!"
            alert_type = "alert-success"
    else:
        upd_current_num -= 1
        Tuan.objects.filter(id=vote_id).update(current_num=upd_current_num)
        upd_user = Person.objects.get(user_id=user.id)
        upd_user.joined_tuan.remove(upd_tuan)
        upd_user.save()
        warning1 =  "Dear!"
        warning2 =  "Vote successed!"
        alert_type = "alert-success"
    tuan_list = Tuan.objects.all()
    active_page = "Home"
    return HttpResponseRedirect(referer)


def delete_tuan(request):
    if request.method == 'GET':
        return HttpResponseRedirect('/')
    user = request.user
    person = Person.objects.get(user_id=user.id)
    warning1 ='Delete'
    warning2 = 'OK'
    alert_type = "alert-success"
    del_id = int(request.POST['del_id'])
    tuan = Tuan.objects.get(id=del_id)
    tuan.delete()
    tuan_list = Tuan.objects.filter(initiator=user.username)
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
    request.session['login_from'] = request.META.get('HTTP_REFERER', '/index/')
    return render_to_response("register.html",context_instance=RequestContext(request))


def register_create(request):
    if request.method == "POST":
        html_from = request.session['login_from']
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
        tuan_user = Person()
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
    tuan_list = Tuan.objects.filter(initiator=person_name)
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

