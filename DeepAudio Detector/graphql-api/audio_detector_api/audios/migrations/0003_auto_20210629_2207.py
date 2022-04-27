# Generated by Django 3.1.7 on 2021-06-29 22:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audios', '0002_auto_20210629_1905'),
    ]

    operations = [
        migrations.AddField(
            model_name='audio',
            name='hash_text',
            field=models.CharField(blank=True, help_text='Last Predcit Result', max_length=64, null=True),
        ),
        migrations.AlterField(
            model_name='audio',
            name='audio_file',
            field=models.FileField(help_text='Audio file', upload_to='audios/unlabeled'),
        ),
        migrations.AlterField(
            model_name='audio',
            name='result',
            field=models.FloatField(blank=True, help_text='Last Predcit Result', null=True),
        ),
    ]