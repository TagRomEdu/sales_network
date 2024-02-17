# Generated by Django 4.2.9 on 2024-02-17 05:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Name')),
                ('model', models.CharField(blank=True, max_length=100, null=True, verbose_name='Model')),
                ('release_date', models.DateField(auto_now_add=True, null=True, verbose_name='Release date')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
            },
        ),
        migrations.CreateModel(
            name='NetworkLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('network', models.CharField(choices=[('plant', 'Plant'), ('retail_network', 'Retail network'), ('individual_entrepreneur', 'Individual entrepreneur')], max_length=23, verbose_name='Network')),
                ('name', models.CharField(max_length=150, verbose_name='Name')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('country', models.CharField(max_length=15, verbose_name='Country')),
                ('city', models.CharField(max_length=25, verbose_name='City')),
                ('street', models.CharField(max_length=100, verbose_name='Street')),
                ('house_number', models.CharField(max_length=15, verbose_name='House number')),
                ('debt', models.DecimalField(decimal_places=2, default=0.0, help_text='You indicate the debt to the supplier in monetary terms\n            from the moment to the penny.', max_digits=25, verbose_name='Debt')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('hierarchy', models.IntegerField(default=0, help_text='Hierarchy must be between 0 and 2.', verbose_name='Hierarchy')),
                ('distributor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='network_link', to='network_app.networklink', verbose_name='Distributor')),
                ('products', models.ManyToManyField(blank=True, related_name='network_links', to='network_app.product', verbose_name='Products')),
            ],
            options={
                'verbose_name': 'Network link',
                'verbose_name_plural': 'Network links',
            },
        ),
    ]