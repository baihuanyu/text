from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'learning_log.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    # 主页
    url(r'^$',views.index , name= 'index'),
    #显示学习主题
    url(r'^topics/$',views.topics,name='topics'),
    #特定主题的详细页面 其中<topic_id>需和视图里面的 参数名字一样
    url(r'^topics/(?P<topic_id>\d+)/$',views.topic,name='topic'),
    #用于添加新主题的路由
    url(r'^new_topics/$',views.new_topic,name='new_topic'),
    # 添加主题输入的路由
    url(r'^new_entry/(?P<topic_id>\d+)/$',views.new_entry,name='new_entry'),
    #编辑条目的页面
    url(r'^edit_entry/(?P<entry_id>\d+)/$',views.edit_entry,name="edit_entry"),


]
