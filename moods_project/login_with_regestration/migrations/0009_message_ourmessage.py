# Generated by Django 2.2.4 on 2023-04-05 07:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('login_with_regestration', '0008_auto_20230404_2350'),
    ]

    operations = [
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
    ]
