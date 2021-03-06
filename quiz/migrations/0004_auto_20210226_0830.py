# Generated by Django 3.1.7 on 2021-02-26 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_auto_20210226_0821'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='questionmtm',
            options={'verbose_name': 'Вопрос-Выбор', 'verbose_name_plural': 'Вопросы-Выбор'},
        ),
        migrations.AlterField(
            model_name='choiceanswer',
            name='quiz',
            field=models.ManyToManyField(related_name='choice_answer', to='quiz.QuestionMTM'),
        ),
    ]
