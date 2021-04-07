# Generated by Django 3.1.1 on 2020-10-18 09:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ExpenseCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='IncomeCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='InnerTransaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField()),
                ('date', models.DateField()),
                ('commentary', models.TextField(blank=True)),
                ('account_from', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='inner_transaction_from_set', to='core.account')),
                ('accout_to', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='inner_transaction_to_set', to='core.account')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='IncomeTransaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField()),
                ('date', models.DateField()),
                ('commentary', models.TextField(blank=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.account')),
                ('income_category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.incomecategory')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ExpenseTransaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.PositiveIntegerField()),
                ('date', models.DateField()),
                ('commentary', models.TextField(blank=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.account')),
                ('expense_category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='core.expensecategory')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]