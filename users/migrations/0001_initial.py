# Generated by Django 4.2 on 2023-05-01 10:52

from django.db import migrations, models
import django_resized.forms
import users.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=255, verbose_name='Имя')),
                ('last_name', models.CharField(blank=True, max_length=255, verbose_name='Фамилия')),
                ('avatar', django_resized.forms.ResizedImageField(blank=True, crop=['middle', 'center'], force_format=None, keep_meta=True, null=True, quality=-1, scale=None, size=(400, 400), upload_to='users_avatar', verbose_name='Изображение')),
                ('email', models.EmailField(blank=True, max_length=254, unique=True, verbose_name='Почта')),
                ('username', models.CharField(max_length=255, unique=True, verbose_name='Имя пользователя')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Статус сотрудника')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активен')),
                ('phone', models.CharField(max_length=255, null=True, validators=[users.validators.phone_validator], verbose_name='Номер телефона')),
                ('user_type', models.CharField(choices=[('super_user', 'Директор'), ('admin', 'Админ'), ('seller', 'Продавец'), ('deliveryman', 'Доставщик')], default='seller', max_length=255, verbose_name='Тип пользователя')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
    ]
