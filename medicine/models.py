from ssl import Purpose
from xml.dom.pulldom import default_bufsize
from django.db import models
from django.utils import timezone

class MedicineModel(models.Model):
    medicinename = models.CharField(verbose_name="名前",max_length=30)
    dosage = models.IntegerField(verbose_name="一回の服用量",default=0,)
    shape = models.CharField(verbose_name="形状",max_length=30)
    timemorning = models.BooleanField(verbose_name="朝",default=False)
    timenoon = models.BooleanField(verbose_name="昼",default=False)
    timenight = models.BooleanField(verbose_name="夜",default=False)
    timesleep = models.BooleanField(verbose_name="寝る前",default=False)
    timeother = models.BooleanField(verbose_name="その他",default=False)
    amount = models.IntegerField(verbose_name="処方量",default=0,)
    hospital = models.CharField(verbose_name="病院",max_length=30)
    department = models.CharField(verbose_name="診療科",max_length=30)
    purpose = models.CharField(verbose_name="効用",max_length=30)
    recorddate = models.DateField(verbose_name="作成日時",default=timezone.now)
    lastday = models.DateField(verbose_name="最終処方日")
    memo = models.CharField(verbose_name="メモ",max_length=500)

    def __str__(self):
        return str(self.id) + ',' + \
            str(self.medicinename) + ',' + \
            str(self.lastday)

TAKE_MEDICINE = [
    (1, '飲んだ！'),
    (2, '一部飲めなかった'),
    (3, '飲めなかった……'),
]

class TakeModel(models.Model):
    takemedicine = models.TextField(verbose_name="内服",choices=TAKE_MEDICINE, blank=True)

    def __str__(self):
        return str(self.id)

class NoticeModel(models.Model):
    noticemorning = models.DateTimeField(verbose_name="朝・通知")
    noticenoon = models.DateTimeField(verbose_name="昼・通知")
    noticenight = models.DateTimeField(verbose_name="夜・通知")
    noticesleep = models.DateTimeField(verbose_name="寝る前・通知")

    def __str__(self):
        return str(self.id)