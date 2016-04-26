# Create your views here.
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from tuanapp.models import Tuan

def index(request):
	warning1 = 'Are you Ready'
	warning2 = 'for Tuan??'
	alert_type = "alert-info"
	tuan_list = Tuan.objects.all()
	return render_to_response('index.html', locals() , context_instance = RequestContext(request))

def create_tuan(request):
	warning1 = 'Are you Ready'
	warning2 = 'for Tuan??'
	alert_type = "alert-info"
	tuan_list = Tuan.objects.all()
	return render_to_response('create_tuan.html', locals() , context_instance = RequestContext(request))

def insert(request):
	if request.method == 'GET':
		return HttpResponseRedirect('/')
	warning1 = 'Ready'
	warning2 = 'for insert'
	alert_type = "alert-info"
	rest_name = request.POST['new_rest_name']
	max_num = request.POST['new_max_num']
	init = request.POST['new_init']
	date = request.POST['new_date']                                 
	if len(rest_name) == 0:
		warning1 = 'Dear Qin!'
		warning2 = 'Insert new Tuan failed, resturant should not be empty...'
		alert_type = "alert-danger"
		tuan_list = Tuan.objects.all()
		return render_to_response('create_tuan.html', locals(), context_instance = RequestContext(request))			
	else:		
		try:
			tmp = Tuan.objects.get(init=init)
			warning1 =  "Dear %s"%init
			warning2 =  ", you have already created the activity. Please update your Tuan instead of create new one."
			alert_type = "alert-warning"
			tuan_list = Tuan.objects.all()
			return render_to_response('create_tuan.html', locals(), context_instance = RequestContext(request))
		except Tuan.DoesNotExist:
			warning1 =  "Dear %s"%init
			warning2 =  ", you didn't initiate Tuan before, create Tuan for %s."%init
			alert_type = "alert-success"
			newtuan = Tuan()
			newtuan.rest_name = rest_name
			newtuan.max_num = max_num
			newtuan.init = init
			newtuan.date = date
			newtuan.save()   
		tuan_list = Tuan.objects.all()
		return render_to_response('index.html', locals(), context_instance = RequestContext(request)) 		

def update(request):
	if request.method == 'GET':
		return HttpResponseRedirect('/')
	warning1 = 'Ready'
	warning2 = 'for update'
	alert_type = "alert-info"
	upd_id = int(request.POST['upd_id'])
	upd_rest_name = request.POST['upd_rest_name']
	upd_max_num = request.POST['upd_max_num']
	upd_date = request.POST['upd_date']

	upd_tuan = Tuan.objects.get(id=upd_id)
	upd_crt_num = int(upd_tuan.crt_num)

	if len(upd_rest_name) == 0:
		warning1 = 'Dear Qin!'
		warning2 = 'update tuan failed, resturant name cannot be empty'
		alert_type = "alert-danger"
	elif int(upd_max_num) < upd_crt_num:
		warning1 = 'Dear Qin!'
		warning2 = 'Current participant number is larger than your updated max participant number, update failed...'
		alert_type = 'alert-danger'
	else:		
		upd_progress = int(float(upd_crt_num)/int(upd_max_num)*100)
		Tuan.objects.filter(id=upd_id).update(rest_name=upd_rest_name, max_num=upd_max_num, date=upd_date, progress=upd_progress)
		warning1 =  "Dear!"
		warning2 =  "Update successed!"
		alert_type = "alert-success"
	tuan_list = Tuan.objects.all()
	return render_to_response('index.html', locals(), context_instance = RequestContext(request))

def vote(request):
	if request.method == 'GET':
		return HttpResponseRedirect('/')
	warning1 = 'Ready'
	warning2 = 'for vote'
	alert_type = "alert-info"
	vote_id = int(request.POST['vote_id'])
                                     
	upd_tuan = Tuan.objects.get(id=vote_id)
	upd_crt_num = int(upd_tuan.crt_num)
	upd_max_num = int(upd_tuan.max_num)
	if upd_crt_num == upd_max_num:
		warning1 = "Dear Qin!"
		warning2 = "This Tuan is full now... Please choose another one~"
		alert_type = "alert-danger"
	else:
		upd_crt_num += 1	
		upd_progress = int(float(upd_crt_num)/upd_max_num*100)
		Tuan.objects.filter(id=vote_id).update(crt_num=upd_crt_num, progress=upd_progress)
		warning1 =  "Dear!"
		warning2 =  "Vote successed!"
		alert_type = "alert-success"

	tuan_list = Tuan.objects.all()
	return render_to_response('index.html', locals(), context_instance = RequestContext(request))

def delete(request):
	if request.method == 'GET':
		return HttpResponseRedirect('/')
	warning1 ='Delete'
	warning2 = 'OK'
	alert_type = "alert-success"
	del_id = int(request.POST['del_id'])
	tuan = Tuan.objects.get(id=del_id)
	tuan.delete()
	tuan_list = Tuan.objects.all()
	return render_to_response('index.html', locals(), context_instance = RequestContext(request))
