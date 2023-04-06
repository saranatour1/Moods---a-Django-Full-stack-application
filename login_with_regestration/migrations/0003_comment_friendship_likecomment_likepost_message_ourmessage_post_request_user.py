# Generated by Django 2.2.4 on 2023-04-06 22:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login_with_regestration', '0002_auto_20230407_0123'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=45)),
                ('last_name', models.CharField(max_length=45)),
                ('email', models.CharField(max_length=255, unique=True)),
                ('password_hash', models.CharField(max_length=255)),
                ('birthday', models.DateField()),
                ('gender', models.CharField(max_length=50)),
                ('time_zone', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('post_content', models.TextField()),
                ('likes_count', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user_who_post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='login_with_regestration.User')),
            ],
        ),
        migrations.CreateModel(
            name='OurMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user_group1', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='chat_groups1', to='login_with_regestration.User')),
                ('user_group2', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='chat_groups2', to='login_with_regestration.User')),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('message_receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='received_messages', to='login_with_regestration.User')),
                ('message_sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_messages', to='login_with_regestration.User')),
            ],
        ),
        migrations.CreateModel(
            name='FriendShip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('users', models.ManyToManyField(related_name='friends', to='login_with_regestration.User')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment_content', models.TextField()),
                ('likes_count', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments_on_post', to='login_with_regestration.Post')),
                ('user_who_comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='login_with_regestration.User')),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('request_reciever', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='received_requests', to='login_with_regestration.User')),
                ('request_sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_requests', to='login_with_regestration.User')),
            ],
            options={
                'unique_together': {('request_sender', 'request_reciever')},
            },
        ),
        migrations.CreateModel(
            name='LikePost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes_on_post', to='login_with_regestration.Post')),
                ('user_who_like', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='liked_posts', to='login_with_regestration.User')),
            ],
            options={
                'unique_together': {('user_who_like', 'post')},
            },
        ),
        migrations.CreateModel(
            name='LikeComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes_on_comment', to='login_with_regestration.Comment')),
                ('user_who_like', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='liked_comments', to='login_with_regestration.User')),
            ],
            options={
                'unique_together': {('user_who_like', 'comment')},
            },
        ),
    ]