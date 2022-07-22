from django import forms 
from.models import MedicineModel,NoticeModel
from django.utils import timezone

class NoticeForm(forms.Form):
    model = NoticeModel
    noticemorning = forms.TimeField(label='朝の通知',\
    widget=forms.DateTimeInput(attrs={"type": "datetime-local", "value": timezone.datetime.now()}),
        input_formats=['%Y-%m-%dT%H:%M'])
    noticenoon = forms.TimeField(label='昼の通知',\
    widget=forms.DateTimeInput(attrs={"type": "datetime-local", "value": timezone.datetime.now()}),
        input_formats=['%Y-%m-%dT%H:%M'])
    noticenight = forms.TimeField(label='夜の通知',\
    widget=forms.DateTimeInput(attrs={"type": "datetime-local", "value": timezone.datetime.now()}),
        input_formats=['%Y-%m-%dT%H:%M'])
    noticesleep = forms.TimeField(label='寝る前の通知',\
    widget=forms.DateTimeInput(attrs={"type": "datetime-local", "value": timezone.datetime.now()}),
        input_formats=['%Y-%m-%dT%H:%M'])
        
# class NoticeForm(forms.ModelForm):
#     class Meta:
#         model = NoticeModel
#         fields = ['noticemorning','noticenoon','noticenight','noticesleep']
#         widgets = {
#             forms.NumberInput(attrs={"type": "time"})
#         }

class MedicineForm(forms.ModelForm):
    class Meta:
        model = MedicineModel
        fields = ['medicinename','dosage','shape','amount',\
            'timemorning','timenoon','timenight','timesleep','timeother',\
                'hospital','department','purpose','lastday','recorddate','memo']

#試作・未使用
class HelloForm(forms.Form):
    medicinename = forms.CharField(label='薬の名前',\
        widget=forms.TextInput(attrs={'class':'form-control'}))
    dosage = forms.IntegerField(label='一回の服用数',min_value=1,\
        widget=forms.NumberInput(attrs={'class':'form-control'}))
    shapedata = [
        ('錠','錠剤・カプセル剤'),
        ('袋','粉薬'),
        ('ml','シロップ・液剤'),
        ('滴','点眼・点鼻薬'),
        ('回','塗り薬'),
        ('回','注射'),
        ('回','その他'),
    ]
    shape = forms.ChoiceField(label='形状', \
            choices=shapedata,widget=forms.Select(attrs={'class':'form-control'}))
    hospital = forms.CharField(label='病院',\
        widget=forms.TextInput(attrs={'class':'form-control'}))
    department = forms.CharField(label='診療科',\
        widget=forms.TextInput(attrs={'class':'form-control'}))
    purpose = forms.CharField(label='効用',\
        widget=forms.TextInput(attrs={'class':'form-control'}))
    amount = forms.IntegerField(label='処方数',min_value=1,\
    widget=forms.NumberInput(attrs={'class':'form-control'}))
    recorddate = forms.DateField(label='登録日',\
    widget=forms.TextInput(attrs={'class':'form-control'}))
    lastday = forms.DateField(label='受診日',\
    widget=forms.TextInput(attrs={'class':'form-control'}))
    memo = forms.CharField(label='メモ',\
        widget=forms.TextInput(attrs={'class':'form-control','rows':2}))

    # timezonedata=[
    #     ('朝','朝'),
    #     ('昼','昼'),
    #     ('夜','夜'),
    #     ('寝る前','寝る前'),
    #     ('その他','その他'),
    # ]
    # timezone = forms.MultipleChoiceField(label='飲む時間', \
    #         choices=timezonedata,widget=forms.CheckboxSelectMultiple(attrs={'class':'form-control'}))

    
    # timemorning = models.BooleanField(verbose_name="朝",default=False)
    # timenoon = models.BooleanField(verbose_name="昼",default=False)
    # timenight = models.BooleanField(verbose_name="夜",default=False)
    # timesleep = models.BooleanField(verbose_name="寝る前",default=False)
    # timeother = models.BooleanField(verbose_name="その他",default=False)
    # purpose = models.CharField(verbose_name="効用",max_length=30)