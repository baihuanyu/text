from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth import logout ,login , authenticate
from  django.core.urlresolvers import reverse
from  django.contrib.auth.forms import UserCreationForm
# Create your views here.
def logout_view(request):
    '''注销用户'''
    logout(request)
    return HttpResponseRedirect(reverse('learning_logs:index'))

def register(request):
    '''注册用户的函数'''
    if request.method != 'POST' :
        #显示空的表单
        form = UserCreationForm()
    else:
        #处理填写好的表单
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            #让用户自动登录在重定向到主页
            # 函数authenticate 意思是鉴定 认证 认证用户信息之后传递参数给login进行登录
            authenticated_user = authenticate(username = new_user.username,
                                              password = request.POST['password1'])
            login(request,authenticated_user)
            return HttpResponseRedirect(reverse('learning_logs:index'))
    context = {'form':form}
    return render(request,'users/register.html',context)