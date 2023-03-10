# Generated by Django 4.1.3 on 2022-11-21 14:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0002_doctor_alter_mobile_phone_alter_mobile_u'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('sid', models.AutoField(primary_key=True, serialize=False)),
                ('time_slot', models.CharField(max_length=255, verbose_name='Timing')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doctor', to='accounts.doctor', verbose_name='Doctor')),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('apid', models.AutoField(primary_key=True, serialize=False)),
                ('appdate', models.DateField(verbose_name='Appointment Date')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doctors', to='accounts.doctor', verbose_name='Doctors')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patient', to=settings.AUTH_USER_MODEL, verbose_name='Patient')),
            ],
        ),
    ]
