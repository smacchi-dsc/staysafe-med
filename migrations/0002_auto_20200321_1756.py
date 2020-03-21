# Generated by Django 3.0.4 on 2020-03-21 17:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('staysafemed', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.RenameField(
            model_name='illnessstatushaspatient',
            old_name='dateUpdate',
            new_name='date_update',
        ),
        migrations.CreateModel(
            name='HospitalHasPatient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_hospitalized', models.DateTimeField()),
                ('hospital', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staysafemed.Hospital')),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staysafemed.Patient')),
            ],
        ),
    ]
