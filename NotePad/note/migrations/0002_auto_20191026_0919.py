# Generated by Django 2.2.6 on 2019-10-26 09:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('note', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.ForeignKey(db_column='name', default=None, on_delete=django.db.models.deletion.CASCADE, to='note.Name'),
        ),
    ]
