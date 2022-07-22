from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
from django.views.generic import TemplateView
from .forms import MedicineForm,NoticeForm,HelloForm
from .models import MedicineModel,NoticeModel
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
#迷走する時間指定用のインポートモジュール
from django.utils import timezone
from datetime import datetime,date
import sched, time, datetime

#薬の一覧シリーズ～全部・朝・昼・夜・寝る前・その他～
def index(request):
    data = MedicineModel.objects.all()
    
    params = {
        'title':'今日のお薬',
        'message':'一覧',
        'data':data,
    }
    return render(request,'medicine/index.html',params)

def morning(request):
    #  if MedicineModel.objects.filter(timemorning=False):
    datam = MedicineModel.objects.filter(timemorning=True)
    params = {
        'title':'朝のお薬',
        'message':'一覧',
        'data':datam,
    }
    return render(request,'medicine/morning.html',params)

def noon(request):
    datan = MedicineModel.objects.filter(timenoon=True)
    params = {
        'title':'昼のお薬',
        'message':'一覧',
        'data':datan,
    }
    return render(request,'medicine/noon.html',params)

def night(request):
    datani = MedicineModel.objects.filter(timenight=True)
    params = {
        'title':'夜のお薬',
        'message':'一覧',
        'data':datani,
    }
    return render(request,'medicine/night.html',params)

def sleep(request):
    datas = MedicineModel.objects.filter(timesleep=True)
    params = {
        'title':'眠る前のお薬',
        'message':'一覧',
        'data':datas,
    }
    return render(request,'medicine/sleep.html',params)

def other(request):
    datao = MedicineModel.objects.filter(timeother=True)
    params = {
        'title':'その他のお薬',
        'message':'一覧',
        'data':datao,
    }
    return render(request,'medicine/other.html',params)
#薬の詳細一覧リスト
def list(request):
    data = MedicineModel.objects.all()
    params = {
        'title':'お薬一覧',
        'message':'一覧',
        'data':data,
    }
    return render(request,'medicine/list.html',params)
#薬の追加ページ
def create(request):
    if (request.method == 'POST'):
        obj = MedicineModel()
        medicine = MedicineForm(request.POST, ["title"])
        medicine.save()
        return redirect(to='/medicine/')
    params = {
        'title': 'お薬投稿',
        'messsage': 'Hello',
        'form': MedicineForm(),
    }
    return render(request,'medicine/create.html', params)
#薬の修正ページ
def edit(request, num):
    obj = MedicineModel.objects.get(id=num)
    if (request.method == 'POST'):
        friend = MedicineForm(request.POST, instance=obj)
        friend.save()
        return redirect(to='/medicine')
    params = {
        'title': 'お薬データ修正',
        'id':num,
        'form': MedicineForm(instance=obj),
    }
    return render(request, 'medicine/edit.html', params)
#試作・日付取得
def takeconf(request):
    now = timezone.now()
    print(now)  # コード内でnowをprintしてみる
    context = { 'now': now }
    # if now == 
    # time = datetime.datetime.now()
    # str_time = time.strftime('%H:%M')
    # print(str_time)
    # st = { 'str_time': str_time }
    return render(request, 'medicine/takelist.html', context)
#試作・通知設定画面
def notice(request):
    if (request.method == 'POST'):
        obj = NoticeModel()
        notice = NoticeForm(request.POST)
        notice.save()
        return redirect(to='/medicine/')
    params = {
        'title': '通知設定',
        'messsage': 'Hello',
        'form': NoticeForm(),
    }
    return render(request,'medicine/notice.html', params)

def excuse(request,num):
    obj = MedicineModel.objects.get(id=num)
    if (request.method == 'POST'):
        friend = HelloForm(request.POST, instance=obj)
        friend.save()
        return redirect(to='/medicine')
    params = {
        'title': 'Hello',
          'form': HelloForm(instance=obj),
    }
    return render(request, 'medicine/test2.html', params)

def list(request):
    datali = MedicineModel.objects.all()
    i = 0
    while i <=MedicineModel.objects.all().aggregate(max('id')):
        params = {'mediname':'','message':'一覧','data':datali,}
        i = i+1
    return render(request,'medicine/list.html',params)

# class HelloView(TemplateView):

#     def __init__(self):
#         self.params = {
#             'title':'今日のお薬だよん',
#             'message':'あなたのデータ',
#             'form':HelloForm(),
#         }

#     def get(self, request):
#         return render(request, 'medicine/post.html', self.params)

#     def post(self, request):
#         if (request.method == 'POST'):
#             sh = request.POST['shape']
#             tz = request.POST.getlist('timezone')
#             msg = '薬の名前は' + request.POST.get('medicinename') + \
#                 '<br>一回に飲む量は' + request.POST.get('dosage') + \
#                 sh + 'ですね' +\
#                 '<br>飲む時間帯は' + str(tz) +'<br>' + \
#                 '受診日は' + request.POST.get('consultationdate') + '<br>' + \
#                 'メモ<br>' + request.POST.get('memo')
#             self.params['message'] = msg
#             self.params['form'] = HelloForm(request.POST)
#         return render(request,'medicine/post.html',self.params)
