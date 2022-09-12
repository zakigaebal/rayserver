# Generated by Django 4.1.1 on 2022-09-12 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LoginUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(default=False, max_length=20, unique=True)),
                ('user_pw', models.CharField(default=False, max_length=255)),
                ('birth_day', models.DateField(null=True, verbose_name='생년월일')),
                ('gender', models.CharField(default='male', max_length=6, verbose_name='성별')),
                ('email', models.CharField(default='', max_length=255, verbose_name='이메일 주소')),
                ('name', models.CharField(max_length=20, null=True, verbose_name='이름')),
                ('age', models.IntegerField(default=20, verbose_name='나이')),
                ('profile_img', models.ImageField(null=True, upload_to='', verbose_name='프로필이미지')),
            ],
            options={
                'verbose_name': '로그인 테스트 테이블',
                'db_table': 'login_user',
            },
        ),
    ]
