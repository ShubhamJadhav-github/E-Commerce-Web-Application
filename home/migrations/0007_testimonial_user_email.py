# Generated by Django 4.2.7 on 2023-11-12 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_testimonial_user_profile_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='testimonial',
            name='user_email',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
