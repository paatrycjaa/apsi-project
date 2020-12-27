# Generated by Django 3.0.3 on 2020-11-27 16:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='StatusPomyslu',
            fields=[
                ('status', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='UstawieniaOceniania',
            fields=[
                ('ustawienia', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('opis', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Uzytkownik',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imie', models.CharField(max_length=200)),
                ('nazwisko', models.CharField(max_length=300)),
                ('sso', models.CharField(max_length=9)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Pomysl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tematyka', models.CharField(max_length=100)),
                ('opis', models.TextField()),
                ('planowane_korzysci', models.TextField(blank=True)),
                ('planowane_koszty', models.TextField(blank=True)),
                ('ocena_wazona', models.FloatField(blank=True)),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='innovation_module.StatusPomyslu')),
                ('ustawienia_oceniania', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='innovation_module.UstawieniaOceniania')),
                ('uzytkownik', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='innovation_module.Uzytkownik')),
            ],
        ),
         migrations.AlterField(
            model_name='pomysl',
            name='ocena_wazona',
            field=models.FloatField(null=True),
        ),
        migrations.CreateModel(
            name='Ocena',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateTimeField(verbose_name='%Y-%m-%d %H:%M:%S')),
                ('ocena_liczbowa', models.IntegerField()),
                ('opis', models.CharField(max_length=500)),
                ('pomysl', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='innovation_module.pomysl')),
                ('uzytkownik', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='innovation_module.uzytkownik')),
            ],
        ),
    ]
