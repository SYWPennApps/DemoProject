# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response,redirect
from django.conf import settings
from SYWAPI.SYWAPI_Session import *
from models import User,UserFollowship

import os.path
def landing(request):
	sywapi_session=SYWAPI_Session(settings.SYWAPP['app_id'],settings.SYWAPP['app_secret'],settings.SYWAPP['api_baseurl'],settings.SYWAPP['syw_baseurl'],settings.SYWAPP['app_baseurl'])
	user_token=request.GET['token']
	user=sywapi_session.get_current_user(user_token)
	return render_to_response('landing.html',{'user':user,'SYWAPP':settings.SYWAPP})

def postlogin(request):
	sywapi_session=SYWAPI_Session(settings.SYWAPP['app_id'],settings.SYWAPP['app_secret'],settings.SYWAPP['api_baseurl'],settings.SYWAPP['syw_baseurl'],settings.SYWAPP['app_baseurl'])
	user_token=request.GET['token']
	user=sywapi_session.get_current_user(user_token)
	dbuser,created=User.objects.get_or_create(syw_id=user['id'],name=user['name'],image_url=user.get('imageUrl'))
	
	powerful_sywapi_session=SYWAPI_Session(settings.SYWDEFAPP['app_id'],settings.SYWDEFAPP['app_secret'],settings.SYWDEFAPP['api_baseurl'],settings.SYWDEFAPP['syw_baseurl'],settings.SYWDEFAPP['app_baseurl'])
	offline_token=powerful_sywapi_session.get_offline_token(int(user['id']))
	user_followers=powerful_sywapi_session.get_user_followers(int(user['id']),offline_token)
	for f_id in user_followers:
		print f_id
		try:
			offline_token=powerful_sywapi_session.get_offline_token(f_id)
			f_details=powerful_sywapi_session.get_user_profile_details(offline_token)
			user_followship=UserFollowship(followed_by=dbuser,follower_id=f_id,follower_name=f_details['name'],follower_image_url=f_details['imageUrl'],birth_day=f_details['birthday']['day'],birth_month=f_details['birthday']['month'])
			user_followship.save()
		except Exception:
			continue
	
	return render_to_response('postlogin.html',{'user':user,'SYWAPP':settings.SYWAPP})
	

def home(request,user_id):
	user_followers=UserFollowship.objects.filter(followed_by=user_id).order_by('birth_month', 'birth_day')
	return render_to_response('home.html',{'followers':user_followers,'SYWAPP':settings.SYWAPP})
	
	
def get_user_wishlist(request,user_id):
	powerful_sywapi_session=SYWAPI_Session(settings.SYWDEFAPP['app_id'],settings.SYWDEFAPP['app_secret'],settings.SYWDEFAPP['api_baseurl'],settings.SYWDEFAPP['syw_baseurl'],settings.SYWDEFAPP['app_baseurl'])
	offline_token=powerful_sywapi_session.get_offline_token(int(user_id))
	user_wishlist=powerful_sywapi_session.get_user_wishlist(int(user_id),offline_token)
	return HttpResponse(json.dumps(user_wishlist),mimetype="application/json")
	