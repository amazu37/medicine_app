# Generated by Django 3.0.4 on 2022-07-19 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MedicineModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medicinename', models.CharField(max_length=30, verbose_name='名前')),
                ('dosage', models.IntegerField(default=0, verbose_name='一回の服用量')),
                ('shape', models.CharField(max_length=30, verbose_name='形状')),
                ('timemorning', models.BooleanField(default=False, verbose_name='朝')),
                ('timenoon', models.BooleanField(default=False, verbose_name='昼')),
                ('timenight', models.BooleanField(default=False, verbose_name='夜')),
                ('timesleep', models.BooleanField(default=False, verbose_name='寝る前')),
                ('timeother', models.BooleanField(default=False, verbose_name='その他')),
                ('amount', models.IntegerField(default=0, verbose_name='処方量')),
                ('hospital', models.CharField(max_length=30, verbose_name='病院')),
                ('department', models.CharField(max_length=30, verbose_name='診療科')),
                ('purpose', models.CharField(max_length=30, verbose_name='効用')),
                ('recorddate', models.DateField(verbose_name='作成日時')),
                ('lastday', models.DateField(verbose_name='最終処方日')),
                ('memo', models.CharField(max_length=500, verbose_name='メモ')),
            ],
        ),
    ]
