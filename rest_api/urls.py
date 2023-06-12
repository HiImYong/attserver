
import json
from django.urls import path
from ninja import NinjaAPI

from . models import Clients
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
    print('get_id ...')
    ob_id = Clients.objects.all().first()
    dict_id = {}
    dict_id['id'] = ob_id.userId
    dict_id['pw'] = ob_id.userPw
    dict_id['name'] = ob_id.name
    # js_id = json.dumps(dict_id) // Ninja는 내부적으로 딕셔너리를 JSON으로 변환하여 응답으로 전송하므로, 특별히 필요가 없음.
    return dict_id


urlpatterns = [    
    path('hello/', views.hello, name='test'),
    path('rest/', api.urls)
]