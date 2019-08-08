from  django import  forms
from .models import Topic,Entry

class TopicForms(forms.ModelForm):
    class Meta:
        # 根据哪个模型生成表单
        model = Topic
        #表单只包含一个字段
        fields = ['text']
        #防止django为字段text生成标签
        labels = {'text':''}

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']
        labels = {'text':''}
        # widgets 是一个html表单元素  form.texyarea让用户输入时候的字节变成80
        widgets = {'text':forms.Textarea(attrs={'cols':80})}
