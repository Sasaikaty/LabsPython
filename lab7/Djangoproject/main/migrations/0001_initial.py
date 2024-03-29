from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bankName', models.CharField(max_length=50, verbose_name='Название банка')),
                ('address', models.CharField(max_length=150, verbose_name='Адрес')),
            ],
            options={
                'verbose_name': 'Банк',
                'verbose_name_plural': 'Банки',
            },
        ),
        migrations.CreateModel(
            name='BankType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bankType', models.CharField(max_length=100, verbose_name='Тип банка')),
            ],
            options={
                'verbose_name': 'Тип банка',
                'verbose_name_plural': 'Типы банков',
            },
        ),
        migrations.CreateModel(
            name='ClientGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isRelible', models.BooleanField(default=False, verbose_name='Надёжный')),
                ('isVIP', models.BooleanField(default=False, verbose_name='VIP')),
                ('type', models.CharField(max_length=50, verbose_name='Тип клиента')),
            ],
            options={
                'verbose_name': 'Группа клиентов',
                'verbose_name_plural': 'Группы клиентов',
            },
        ),
        migrations.CreateModel(
            name='ClientInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=150, verbose_name='Адрес')),
                ('age', models.IntegerField(default=0, verbose_name='Возраст')),
                ('phoneNumber', models.IntegerField(default=0, verbose_name='Номер телефона')),
                ('clientId', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='main.clientgroup')),
            ],
            options={
                'verbose_name': 'Информация о клиенте',
                'verbose_name_plural': 'Информация о клиентах',
            },
        ),
        migrations.CreateModel(
            name='CallHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio', models.CharField(max_length=100, verbose_name='ФИО')),
                ('date', models.DateTimeField(verbose_name='Дата обращения')),
                ('text', models.CharField(max_length=300, verbose_name='Тип обращения')),
                ('bankId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.bank')),
                ('clientId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.clientinfo')),
            ],
            options={
                'verbose_name': 'История обращений',
                'verbose_name_plural': 'История обращений',
            },
        ),
        migrations.AddField(
            model_name='bank',
            name='bankType',
            field=models.ManyToManyField(to='main.banktype'),
        ),
    ]