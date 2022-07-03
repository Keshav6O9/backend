# Generated by Django 4.0.4 on 2022-07-02 12:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='group',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=75)),
                ('summary', models.CharField(max_length=200)),
                ('status', models.SmallIntegerField()),
                ('createdAt', models.DateTimeField(auto_now=True)),
                ('updatedAt', models.DateTimeField(auto_now_add=True)),
                ('profile', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('firstName', models.CharField(max_length=50)),
                ('lastName', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50, unique=True)),
                ('mobile', models.CharField(max_length=15, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('passwordHash', models.CharField(max_length=50)),
                ('registerdAt', models.DateTimeField(auto_now=True)),
                ('lastLogin', models.TimeField(auto_now_add=True)),
                ('intro', models.CharField(max_length=200)),
                ('profile', models.CharField(max_length=200)),
                ('exams', models.CharField(choices=[('upsc', 'UPSC'), ('neet-ug', 'NEET-UG'), ('aiims-ug', 'AIIMS-UG'), ('ugc-net', 'UGC-NET'), ('gate', 'GATE'), ('iit-jee', 'IIT-JEE'), ('ca', 'CA'), ('cat', 'CAT'), ('nda', 'NDA'), ('clat', 'CLAT')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='user_post',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('message', models.CharField(max_length=200)),
                ('createdAt', models.DateTimeField(auto_now=True)),
                ('updatedAt', models.DateTimeField(auto_now_add=True)),
                ('senderId', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='baseapp.user')),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='%(class)s_requests_created', to='baseapp.user')),
            ],
        ),
        migrations.CreateModel(
            name='user_message',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('message', models.CharField(max_length=200)),
                ('createdAt', models.DateTimeField(auto_now=True)),
                ('updatedAt', models.DateTimeField(auto_now_add=True)),
                ('sourceId', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='%(class)s_requests_created', to='baseapp.user')),
                ('targetId', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='baseapp.user')),
            ],
        ),
        migrations.CreateModel(
            name='user_friend',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('type', models.SmallIntegerField()),
                ('status', models.SmallIntegerField()),
                ('createdAt', models.DateTimeField(auto_now=True)),
                ('updatedAt', models.DateTimeField(auto_now_add=True)),
                ('sourceId', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='%(class)s_requests_created', to='baseapp.user')),
                ('targetId', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='baseapp.user')),
            ],
        ),
        migrations.CreateModel(
            name='user_follower',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('type', models.SmallIntegerField()),
                ('createdAt', models.DateTimeField(auto_now=True)),
                ('updatedAt', models.DateTimeField(auto_now_add=True)),
                ('sourceId', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='%(class)s_requests_created', to='baseapp.user')),
                ('targetId', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='baseapp.user')),
            ],
        ),
        migrations.CreateModel(
            name='group_message',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('message', models.CharField(max_length=200)),
                ('createdAt', models.DateTimeField(auto_now=True)),
                ('updatedAt', models.DateTimeField(auto_now_add=True)),
                ('groupId', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='%(class)s_requests_created', to='baseapp.group')),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='baseapp.group')),
            ],
        ),
        migrations.CreateModel(
            name='group_member',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('status', models.SmallIntegerField()),
                ('createdAt', models.DateTimeField(auto_now=True)),
                ('updatedAt', models.DateTimeField(auto_now_add=True)),
                ('groupId', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='%(class)s_requests_created', to='baseapp.group')),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='baseapp.group')),
            ],
        ),
        migrations.CreateModel(
            name='group_follower',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('type', models.SmallIntegerField()),
                ('createdAt', models.DateTimeField(auto_now=True)),
                ('updatedAt', models.DateTimeField(auto_now_add=True)),
                ('groupId', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='%(class)s_requests_created', to='baseapp.group')),
                ('userId', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='baseapp.group')),
            ],
        ),
        migrations.AddField(
            model_name='group',
            name='createdBy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='%(class)s_requests_created', to='baseapp.user'),
        ),
        migrations.AddField(
            model_name='group',
            name='updatedBy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='baseapp.user'),
        ),
    ]