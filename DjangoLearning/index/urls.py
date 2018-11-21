#用于处理项目根目录urls.py中设置的根url需要处理的逻辑
# index的urls.py
from django.urls import path, re_path
from . import views
urlpatterns = [
    path('', views.index),
    # 添加带有字符类型、整型和slug的URL
    #path('<year>/<int:month>/<slug:day>', views.mydate),
    # 上面的年份等价于    path('<str:year>/<int:month>/<slug:day>', views.mydate)
    re_path('(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2}).html', views.mydate)
]