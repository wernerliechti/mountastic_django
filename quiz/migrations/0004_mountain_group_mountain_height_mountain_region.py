# Generated by Django 5.0.6 on 2024-06-02 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_mountain_remove_question_correct_answer_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='mountain',
            name='group',
            field=models.CharField(default='Unknown', max_length=255),
        ),
        migrations.AddField(
            model_name='mountain',
            name='height',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='mountain',
            name='region',
            field=models.CharField(default='Unknown', max_length=255),
        ),
    ]