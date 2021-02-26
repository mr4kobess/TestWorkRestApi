# Generated by Django 3.1.7 on 2021-02-26 12:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0011_auto_20210226_1107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='quiz',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='question', to='quiz.quiz'),
        ),
        migrations.AlterField(
            model_name='question',
            name='type',
            field=models.CharField(choices=[('Text', 'text'), ('OneQ', 'one'), ('ManyQ', 'many')], max_length=10, null=True, verbose_name='Тип вопроса'),
        ),
    ]