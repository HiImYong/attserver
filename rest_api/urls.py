
import json
from django.urls import path
from ninja import NinjaAPI

from . models import Clients, LastTime
from . import views
import mysql.connector



api = NinjaAPI()


# # MySQL 데이터베이스 연결 설정
# db = mysql.connector.connect(
#     host="127.0.0.1",
#     user="root",
#     password="24320919",
#     database="att_server_db",
#     port="3306"
# )

@api.get('/getId/')
def get_id(request):
    try:        
        print('>> get user')
        ob_id = Clients.objects.all().first()
        dict_id = {}
        dict_id['id'] = ob_id.userId
        dict_id['pw'] = ob_id.userPw
        dict_id['name'] = ob_id.name
        # js_id = json.dumps(dict_id) // Ninja는 내부적으로 딕셔너리를 JSON으로 변환하여 응답으로 전송하므로, 특별히 필요가 없음.
        return dict_id
    
    except Exception as err:
        print('오류가 발생하였습니다.')
        print(err)
        
@api.post('/setId/')
def set_id(request):
    try:        
        print('>> set user')
        
        # request에서 아이디 비밀번호 받아오기\
        post_usernm = request.POST.get('userName')
        post_userId = request.POST.get('userId')
        pose_userPw = request.POST.get('userPw')        
        # orm으로 받아온 값 저장
        client = Clients(name=post_usernm, userId=post_userId,userPw=pose_userPw)
        client.save()
        dict_id = {'result' : 'success'}
        return dict_id
    
    except Exception as err:
        print('오류가 발생하였습니다.')
        print(err)        
        
@api.get('/getLastTime/')
def get_id(request):
    try:        
        print('>> get last time')
        id = request.GET.get('userId')
        ob_id = LastTime.objects.filter(userId = id).first()
        dict_id = {}
        dict_id['id'] = ob_id.userId
        dict_id['time'] = ob_id.lastTime
        
        # js_id = json.dumps(dict_id) // Ninja는 내부적으로 딕셔너리를 JSON으로 변환하여 응답으로 전송하므로, 특별히 필요가 없음.
        return dict_id
    
    except Exception as err:
        print('오류가 발생하였습니다.')
        print(err)        
        
@api.post('/setLastTime/')
def set_lastTime(request):
    try:
        print(">> set last time")
        post_userId = request.POST.get('userId')
        pose_time = request.POST.get('lastTime')   
        times = LastTime(userId=post_userId, lastTime=pose_time)
        times.save()
        dict_id = {'result' : 'success'}
        return dict_id
    
    except Exception as err:
        print('오류가 발생하였습니다.')
        print(err)      


urlpatterns = [    
    path('hello/', views.hello, name='test'),
    path('rest/', api.urls)
]