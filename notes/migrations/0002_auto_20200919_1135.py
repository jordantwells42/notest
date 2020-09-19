# Generated by Django 3.1.1 on 2020-09-19 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='defintion',
            name='term',
        ),
        migrations.RemoveField(
            model_name='example',
            name='term',
        ),
        migrations.RemoveField(
            model_name='question',
            name='term',
        ),
        migrations.RemoveField(
            model_name='section',
            name='note',
        ),
        migrations.RemoveField(
            model_name='term',
            name='section',
        ),
        migrations.AddField(
            model_name='note',
            name='sections',
            field=models.ManyToManyField(related_name='notes', to='notes.Section'),
        ),
        migrations.AddField(
            model_name='section',
            name='terms',
            field=models.ManyToManyField(related_name='sections', to='notes.Term'),
        ),
        migrations.AddField(
            model_name='term',
            name='definitions',
            field=models.ManyToManyField(related_name='terms', to='notes.Defintion'),
        ),
        migrations.AddField(
            model_name='term',
            name='examples',
            field=models.ManyToManyField(related_name='terms', to='notes.Example'),
        ),
        migrations.AddField(
            model_name='term',
            name='questions',
            field=models.ManyToManyField(related_name='terms', to='notes.Question'),
        ),
    ]
