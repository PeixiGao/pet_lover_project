# Generated by Django 3.2.2 on 2021-05-15 03:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FiveDayModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('stock_number', models.CharField(max_length=32)),
                ('stock_name', models.CharField(max_length=32)),
                ('stock_new_price', models.CharField(max_length=32)),
                ('stock_up_and_down_today', models.CharField(max_length=32)),
                ('zhuli_je', models.CharField(max_length=32)),
                ('zhuli_jzb', models.CharField(max_length=32)),
                ('chaodadan_je', models.CharField(max_length=32)),
                ('chaodadan_jzb', models.CharField(max_length=32)),
                ('dd_je', models.CharField(max_length=32)),
                ('dd_jzb', models.CharField(max_length=32)),
                ('zd_je', models.CharField(max_length=32)),
                ('zd_jzb', models.CharField(max_length=32)),
                ('xd_je', models.CharField(max_length=32)),
                ('xd_jzb', models.CharField(max_length=32)),
            ],
            options={
                'verbose_name': '5排行表',
                'verbose_name_plural': '5排行表',
                'db_table': 'five_day',
            },
        ),
        migrations.CreateModel(
            name='TenDayModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('stock_number', models.CharField(max_length=32)),
                ('stock_name', models.CharField(max_length=32)),
                ('stock_new_price', models.CharField(max_length=32)),
                ('stock_up_and_down_today', models.CharField(max_length=32)),
                ('zhuli_je', models.CharField(max_length=32)),
                ('zhuli_jzb', models.CharField(max_length=32)),
                ('chaodadan_je', models.CharField(max_length=32)),
                ('chaodadan_jzb', models.CharField(max_length=32)),
                ('dd_je', models.CharField(max_length=32)),
                ('dd_jzb', models.CharField(max_length=32)),
                ('zd_je', models.CharField(max_length=32)),
                ('zd_jzb', models.CharField(max_length=32)),
                ('xd_je', models.CharField(max_length=32)),
                ('xd_jzb', models.CharField(max_length=32)),
            ],
            options={
                'verbose_name': '10排行表',
                'verbose_name_plural': '10排行表',
                'db_table': 'ten_day',
            },
        ),
        migrations.CreateModel(
            name='ThreeDayModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('stock_number', models.CharField(max_length=32)),
                ('stock_name', models.CharField(max_length=32)),
                ('stock_new_price', models.CharField(max_length=32)),
                ('stock_up_and_down_today', models.CharField(max_length=32)),
                ('zhuli_je', models.CharField(max_length=32)),
                ('zhuli_jzb', models.CharField(max_length=32)),
                ('chaodadan_je', models.CharField(max_length=32)),
                ('chaodadan_jzb', models.CharField(max_length=32)),
                ('dd_je', models.CharField(max_length=32)),
                ('dd_jzb', models.CharField(max_length=32)),
                ('zd_je', models.CharField(max_length=32)),
                ('zd_jzb', models.CharField(max_length=32)),
                ('xd_je', models.CharField(max_length=32)),
                ('xd_jzb', models.CharField(max_length=32)),
            ],
            options={
                'verbose_name': '3排行表',
                'verbose_name_plural': '3排行表',
                'db_table': 'three_day',
            },
        ),
        migrations.CreateModel(
            name='TodayModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('stock_number', models.CharField(max_length=32)),
                ('stock_name', models.CharField(max_length=32)),
                ('stock_new_price', models.CharField(max_length=32)),
                ('stock_up_and_down_today', models.CharField(max_length=32)),
                ('zhuli_je', models.CharField(max_length=32)),
                ('zhuli_jzb', models.CharField(max_length=32)),
                ('chaodadan_je', models.CharField(max_length=32)),
                ('chaodadan_jzb', models.CharField(max_length=32)),
                ('dd_je', models.CharField(max_length=32)),
                ('dd_jzb', models.CharField(max_length=32)),
                ('zd_je', models.CharField(max_length=32)),
                ('zd_jzb', models.CharField(max_length=32)),
                ('xd_je', models.CharField(max_length=32)),
                ('xd_jzb', models.CharField(max_length=32)),
            ],
            options={
                'verbose_name': '今天排行表',
                'verbose_name_plural': '今天排行表',
                'db_table': 'today',
            },
        ),
        migrations.CreateModel(
            name='UserModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=128, unique=True, verbose_name='用户名')),
                ('password', models.CharField(max_length=128, verbose_name='密码')),
                ('permission', models.CharField(max_length=24, verbose_name='权限')),
                ('login_time', models.IntegerField(blank=True, default=0, verbose_name='登录时间')),
                ('reg_time', models.IntegerField(blank=True, default=0, verbose_name='注册时间')),
                ('online', models.SmallIntegerField(default=0, verbose_name='是否在线')),
            ],
            options={
                'verbose_name': '用户表',
                'verbose_name_plural': '用户表',
                'db_table': 'a_user',
            },
        ),
        migrations.CreateModel(
            name='LogModel',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('operation', models.CharField(default='', max_length=100, verbose_name='操作描述')),
                ('time', models.IntegerField(default=0, verbose_name='操作时间')),
                ('ip', models.CharField(default='', max_length=24, verbose_name='用户ip')),
                ('content', models.TextField(default='', verbose_name='请求参数')),
                ('status', models.IntegerField(default=0, verbose_name='请求状态')),
                ('url', models.CharField(default='', max_length=150, verbose_name='请求路径')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Model.usermodel', verbose_name='关联用户id')),
            ],
            options={
                'verbose_name': '日志表',
                'verbose_name_plural': '日志表',
                'db_table': 'a_log',
                'ordering': ('-time',),
            },
        ),
    ]