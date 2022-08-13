# Generated by Django 4.1 on 2022-08-12 12:06

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Assocapi', '0007_alter_association_user_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='association',
            options={'ordering': ('nameassociation',)},
        ),
        migrations.AddField(
            model_name='association',
            name='date_added',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='association',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
        migrations.AddField(
            model_name='association',
            name='logoassociation',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/'),
        ),
    ]