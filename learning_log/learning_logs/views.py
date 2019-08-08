from django.shortcuts import render
from .models import Topic,Entry
from  django.core.urlresolvers import reverse
from .forms import TopicForms,EntryForm
from django.contrib.auth.decorators import  login_required
#保护用户信息
from django.http import HttpResponseRedirect,Http404

# Create your views here.
def index(request):
    '''学习笔记的主页'''
    return render(request,'learning_logs/index.html')
@login_required
def topics(request):
    '''显示所有的主题'''
    #只允许用户访问自己的主题 那么就会注销掉之前的 相比多加了个filter 获取owner属性当前的用户信息
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    #查询数据库 请求提供Topic对象 并按照属性date_added对他们进行排序
    #topics = Topic.objects.order_by('date_added')
    #将返回的查询结果储存到一个上下文中 是个字典
    context = {'topics':topics}
    return render(request,'learning_logs/topics.html',context)
@login_required
def topic(request,topic_id):
    '''显示某个特定主题的全部内容'''
    topic = Topic.objects.get(id=topic_id)
    #date-added增加一个 - 号 表示先显示最近的条目
    # 确认请求的主题属于当前用户
    if topic.owner != request.user:
        raise Http404
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic':topic,'entries':entries}
    # 返回单个特定的话题的值
    return render(request,'learning_logs/topic.html',context)

@login_required
def new_topic(request):
    '''添加新主题'''
    if request.method != 'POST':
        #未提交数据 创建一个新表单
        form = TopicForms()
    else:
        #post提交的数据 对数据进行处理
        form =TopicForms(request.POST)
        #核实用户输入的字段满足条件 ，前面model里面设置的 200字符
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()

            #form.save()
            return HttpResponseRedirect(reverse('learning_logs:topics'))
    context = {'form':form}
    return render(request,'learning_logs/new_topic.html',context)
@login_required
def new_entry(request,topic_id):
    '''在指定主题添加内容'''
    topic = Topic.objects.get(id=topic_id)
    if request.method != 'POST' :
        form = EntryForm()
    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)# 加参数表示不迁移到数据库
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse("learning_logs:topic",args=[topic_id]))
    context = {'topic':topic,'form':form}
    return render(request,'learning_logs/new_entry.html',context)
@login_required
def edit_entry(request,entry_id):
    '''编辑已有的条目'''
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    #保护编辑
    if topic.owner != request.user:
        raise Http404

    if request.method !='POST':
        #初次请求时 用当前的内容填充表单
        form = EntryForm(instance=entry,data=request.POST)
        if form.is_valid():
            form.save()
            return  HttpResponseRedirect(reverse('learning_logs:topic',args=[topic.id]))
    context = {'entry':entry,'topic':topic,'form':form}
    return  render(request,'learning_logs/edit_entry.html',context)
