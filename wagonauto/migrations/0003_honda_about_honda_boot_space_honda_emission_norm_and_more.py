# Generated by Django 4.1 on 2022-12-26 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wagonauto', '0002_suzuki_about_suzuki_boot_space_suzuki_emission_norm_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='honda',
            name='about',
            field=models.TextField(default='About'),
        ),
        migrations.AddField(
            model_name='honda',
            name='boot_space',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='honda',
            name='emission_norm',
            field=models.CharField(default='BS IV', max_length=64),
        ),
        migrations.AddField(
            model_name='honda',
            name='engine_type',
            field=models.CharField(default='Type 0', max_length=64),
        ),
        migrations.AddField(
            model_name='honda',
            name='fuel_type',
            field=models.CharField(default='P/D/C', max_length=64),
        ),
        migrations.AddField(
            model_name='honda',
            name='gear_box',
            field=models.CharField(default='5 gears', max_length=64),
        ),
        migrations.AddField(
            model_name='honda',
            name='height',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='honda',
            name='length',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='honda',
            name='max_power',
            field=models.CharField(default='0 @ 0rpm', max_length=64),
        ),
        migrations.AddField(
            model_name='honda',
            name='max_torque',
            field=models.CharField(default='0 @ 0rpm', max_length=64),
        ),
        migrations.AddField(
            model_name='honda',
            name='mileage',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='honda',
            name='no_cylinders',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='honda',
            name='others',
            field=models.TextField(default='Others'),
        ),
        migrations.AddField(
            model_name='honda',
            name='seating',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='honda',
            name='tank_capacity',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='honda',
            name='transmission_type',
            field=models.CharField(default='Automatic', max_length=64),
        ),
        migrations.AddField(
            model_name='honda',
            name='valves_per_cylinder',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='honda',
            name='weight',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='honda',
            name='width',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='hyundai',
            name='about',
            field=models.TextField(default='About'),
        ),
        migrations.AddField(
            model_name='hyundai',
            name='boot_space',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='hyundai',
            name='emission_norm',
            field=models.CharField(default='BS IV', max_length=64),
        ),
        migrations.AddField(
            model_name='hyundai',
            name='engine_type',
            field=models.CharField(default='Type 0', max_length=64),
        ),
        migrations.AddField(
            model_name='hyundai',
            name='fuel_type',
            field=models.CharField(default='P/D/C', max_length=64),
        ),
        migrations.AddField(
            model_name='hyundai',
            name='gear_box',
            field=models.CharField(default='5 gears', max_length=64),
        ),
        migrations.AddField(
            model_name='hyundai',
            name='height',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='hyundai',
            name='length',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='hyundai',
            name='max_power',
            field=models.CharField(default='0 @ 0rpm', max_length=64),
        ),
        migrations.AddField(
            model_name='hyundai',
            name='max_torque',
            field=models.CharField(default='0 @ 0rpm', max_length=64),
        ),
        migrations.AddField(
            model_name='hyundai',
            name='mileage',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='hyundai',
            name='no_cylinders',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='hyundai',
            name='others',
            field=models.TextField(default='Others'),
        ),
        migrations.AddField(
            model_name='hyundai',
            name='seating',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='hyundai',
            name='tank_capacity',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='hyundai',
            name='transmission_type',
            field=models.CharField(default='Automatic', max_length=64),
        ),
        migrations.AddField(
            model_name='hyundai',
            name='valves_per_cylinder',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='hyundai',
            name='weight',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='hyundai',
            name='width',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='kia',
            name='about',
            field=models.TextField(default='About'),
        ),
        migrations.AddField(
            model_name='kia',
            name='boot_space',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='kia',
            name='emission_norm',
            field=models.CharField(default='BS IV', max_length=64),
        ),
        migrations.AddField(
            model_name='kia',
            name='engine_type',
            field=models.CharField(default='Type 0', max_length=64),
        ),
        migrations.AddField(
            model_name='kia',
            name='fuel_type',
            field=models.CharField(default='P/D/C', max_length=64),
        ),
        migrations.AddField(
            model_name='kia',
            name='gear_box',
            field=models.CharField(default='5 gears', max_length=64),
        ),
        migrations.AddField(
            model_name='kia',
            name='height',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='kia',
            name='length',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='kia',
            name='max_power',
            field=models.CharField(default='0 @ 0rpm', max_length=64),
        ),
        migrations.AddField(
            model_name='kia',
            name='max_torque',
            field=models.CharField(default='0 @ 0rpm', max_length=64),
        ),
        migrations.AddField(
            model_name='kia',
            name='mileage',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='kia',
            name='no_cylinders',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='kia',
            name='others',
            field=models.TextField(default='Others'),
        ),
        migrations.AddField(
            model_name='kia',
            name='seating',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='kia',
            name='tank_capacity',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='kia',
            name='transmission_type',
            field=models.CharField(default='Automatic', max_length=64),
        ),
        migrations.AddField(
            model_name='kia',
            name='valves_per_cylinder',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='kia',
            name='weight',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='kia',
            name='width',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='mahindra',
            name='about',
            field=models.TextField(default='About'),
        ),
        migrations.AddField(
            model_name='mahindra',
            name='boot_space',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='mahindra',
            name='emission_norm',
            field=models.CharField(default='BS IV', max_length=64),
        ),
        migrations.AddField(
            model_name='mahindra',
            name='engine_type',
            field=models.CharField(default='Type 0', max_length=64),
        ),
        migrations.AddField(
            model_name='mahindra',
            name='fuel_type',
            field=models.CharField(default='P/D/C', max_length=64),
        ),
        migrations.AddField(
            model_name='mahindra',
            name='gear_box',
            field=models.CharField(default='5 gears', max_length=64),
        ),
        migrations.AddField(
            model_name='mahindra',
            name='height',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='mahindra',
            name='length',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='mahindra',
            name='max_power',
            field=models.CharField(default='0 @ 0rpm', max_length=64),
        ),
        migrations.AddField(
            model_name='mahindra',
            name='max_torque',
            field=models.CharField(default='0 @ 0rpm', max_length=64),
        ),
        migrations.AddField(
            model_name='mahindra',
            name='mileage',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='mahindra',
            name='no_cylinders',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='mahindra',
            name='others',
            field=models.TextField(default='Others'),
        ),
        migrations.AddField(
            model_name='mahindra',
            name='seating',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='mahindra',
            name='tank_capacity',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='mahindra',
            name='transmission_type',
            field=models.CharField(default='Automatic', max_length=64),
        ),
        migrations.AddField(
            model_name='mahindra',
            name='valves_per_cylinder',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='mahindra',
            name='weight',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='mahindra',
            name='width',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tata',
            name='about',
            field=models.TextField(default='About'),
        ),
        migrations.AddField(
            model_name='tata',
            name='boot_space',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tata',
            name='emission_norm',
            field=models.CharField(default='BS IV', max_length=64),
        ),
        migrations.AddField(
            model_name='tata',
            name='engine_type',
            field=models.CharField(default='Type 0', max_length=64),
        ),
        migrations.AddField(
            model_name='tata',
            name='fuel_type',
            field=models.CharField(default='P/D/C', max_length=64),
        ),
        migrations.AddField(
            model_name='tata',
            name='gear_box',
            field=models.CharField(default='5 gears', max_length=64),
        ),
        migrations.AddField(
            model_name='tata',
            name='height',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tata',
            name='length',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tata',
            name='max_power',
            field=models.CharField(default='0 @ 0rpm', max_length=64),
        ),
        migrations.AddField(
            model_name='tata',
            name='max_torque',
            field=models.CharField(default='0 @ 0rpm', max_length=64),
        ),
        migrations.AddField(
            model_name='tata',
            name='mileage',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='tata',
            name='no_cylinders',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tata',
            name='others',
            field=models.TextField(default='Others'),
        ),
        migrations.AddField(
            model_name='tata',
            name='seating',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tata',
            name='tank_capacity',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='tata',
            name='transmission_type',
            field=models.CharField(default='Automatic', max_length=64),
        ),
        migrations.AddField(
            model_name='tata',
            name='valves_per_cylinder',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tata',
            name='weight',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='tata',
            name='width',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='toyota',
            name='about',
            field=models.TextField(default='About'),
        ),
        migrations.AddField(
            model_name='toyota',
            name='boot_space',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='toyota',
            name='emission_norm',
            field=models.CharField(default='BS IV', max_length=64),
        ),
        migrations.AddField(
            model_name='toyota',
            name='engine_type',
            field=models.CharField(default='Type 0', max_length=64),
        ),
        migrations.AddField(
            model_name='toyota',
            name='fuel_type',
            field=models.CharField(default='P/D/C', max_length=64),
        ),
        migrations.AddField(
            model_name='toyota',
            name='gear_box',
            field=models.CharField(default='5 gears', max_length=64),
        ),
        migrations.AddField(
            model_name='toyota',
            name='height',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='toyota',
            name='length',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='toyota',
            name='max_power',
            field=models.CharField(default='0 @ 0rpm', max_length=64),
        ),
        migrations.AddField(
            model_name='toyota',
            name='max_torque',
            field=models.CharField(default='0 @ 0rpm', max_length=64),
        ),
        migrations.AddField(
            model_name='toyota',
            name='mileage',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='toyota',
            name='no_cylinders',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='toyota',
            name='others',
            field=models.TextField(default='Others'),
        ),
        migrations.AddField(
            model_name='toyota',
            name='seating',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='toyota',
            name='tank_capacity',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='toyota',
            name='transmission_type',
            field=models.CharField(default='Automatic', max_length=64),
        ),
        migrations.AddField(
            model_name='toyota',
            name='valves_per_cylinder',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='toyota',
            name='weight',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='toyota',
            name='width',
            field=models.PositiveIntegerField(default=0),
        ),
    ]