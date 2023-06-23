# Generated by Django 4.2.2 on 2023-06-23 11:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0011_remove_messages_count_alter_messages_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='comments',
            fields=[
                ('comment_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('posted_date', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('comment', models.TextField()),
                ('curr_user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('post', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='posts.messages')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
