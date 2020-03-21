# Generated by Django 3.0.4 on 2020-03-21 22:47

import datetime
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion
import staysafemed.models.patient_otp


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='IllnessStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('illnessStatus', models.IntegerField(choices=[(0, 'healthy'), (1, 'ill_at_home'), (2, 'hospitalized')], unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='IllnessStatusHasPatient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('illness_status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staysafemed.IllnessStatus')),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ssn', models.CharField(max_length=45, unique=True)),
                ('mobile_number_1', models.CharField(blank=True, max_length=30)),
                ('mobile_number_2', models.CharField(blank=True, max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
            ],
            options={
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='PatientOTP',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('otp', models.CharField(blank=True, default=staysafemed.models.patient_otp.generateOtp, max_length=8, null=True)),
                ('date_issued', models.DateTimeField(default=datetime.datetime.utcnow)),
                ('date_expire', models.DateTimeField(default=staysafemed.models.patient_otp.expireDate)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staysafemed.Patient')),
            ],
        ),
        migrations.AddField(
            model_name='patient',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staysafemed.Doctor'),
        ),
        migrations.AddField(
            model_name='patient',
            name='illness_status',
            field=models.ManyToManyField(through='staysafemed.IllnessStatusHasPatient', to='staysafemed.IllnessStatus'),
        ),
        migrations.AddField(
            model_name='illnessstatushaspatient',
            name='patient',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staysafemed.Patient'),
        ),
        migrations.CreateModel(
            name='IllnessData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('breath_frequency', models.DecimalField(decimal_places=2, max_digits=5)),
                ('hear_rate', models.DecimalField(decimal_places=2, max_digits=5)),
                ('systolic_pressure', models.DecimalField(decimal_places=2, max_digits=5)),
                ('body_temperature', models.DecimalField(decimal_places=2, max_digits=5)),
                ('notes', models.TextField(blank=True)),
                ('date_create', models.DateTimeField(default=datetime.datetime.utcnow)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('date_delete', models.DateTimeField(blank=True, null=True)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='staysafemed.Patient')),
            ],
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
