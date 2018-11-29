#用于处理项目根目录urls.py中设置的根url需要处理的逻辑
# index的urls.py
from django.urls import path, re_path
from . import views
urlpatterns = [
    path('', views.index)

    # 添加带有字符类型、整型和slug的URL
    #path('<year>/<int:month>/<slug:day>', views.mydate),
    # 上面的年份等价于    path('<str:year>/<int:month>/<slug:day>', views.mydate)

    #re_path('(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2}).html', views.mydate)
    # 上面的正则表达式 运行时显示page not found 或许是书上的例子有问题？

    #re_path('(?P<year>[0-9]{4}).html', views.myyear, name='myyear'),
    #不是很明白这有啥实际应用，写个demo能用点心么

    #re_path('(?P<year>[0-9]{4}).html', views.myyear_dict, {'month':'05'}, name='myyear_dict')
    #这个也不知道干嘛的

     #path('download.html', views.download)
    #下载文件
]