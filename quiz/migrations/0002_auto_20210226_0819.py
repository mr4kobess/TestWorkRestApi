# Generated by Django 3.1.7 on 2021-02-26 08:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ChoiceAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200, verbose_name='Текст')),
            ],
        ),
        migrations.CreateModel(
            name='QuestionManyToOne',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Вопрос-Текст',
                'verbose_name_plural': 'Вопросы-Текст',
            },
        ),
        migrations.AlterModelOptions(
            name='questiontext',
            options={'verbose_name': 'Вопрос-Текст', 'verbose_name_plural': 'Вопросы-Текст'},
        ),
        migrations.AlterModelOptions(
            name='quiz',
            options={'verbose_name': 'Опрос', 'verbose_name_plural': 'Опросы'},
        ),
        migrations.RemoveField(
            model_name='questiontext',
            name='answer',
        ),
        migrations.AddField(
            model_name='quiz',
            name='date_finish',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='quiz',
            name='date_start',
            field=models.DateTimeField(auto_created=True, null=True),
        ),
        migrations.AddField(
            model_name='quiz',
            name='desc',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='questiontext',
            name='quiz',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question_text', to='quiz.quiz'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='name',
            field=models.CharField(max_length=150, verbose_name='Название'),
        ),
        migrations.DeleteModel(
            name='QuestionNum',
        ),
        migrations.AddField(
            model_name='questionmanytoone',
            name='quiz',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question_mtm', to='quiz.quiz'),
        ),
        migrations.AddField(
            model_name='choiceanswer',
            name='quiz',
            field=models.ManyToManyField(to='quiz.Quiz'),
        ),
    ]