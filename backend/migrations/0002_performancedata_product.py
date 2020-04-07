# Generated by Django 3.0.4 on 2020-04-07 02:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25)),
                ('celltechnology', models.CharField(max_length=25)),
                ('cellmanufacturer', models.CharField(max_length=25)),
                ('numberofcells', models.CharField(max_length=25)),
                ('numberofcellsinseries', models.CharField(max_length=25)),
                ('numberofseriesstrings', models.CharField(max_length=25)),
                ('numberofdiodes', models.CharField(max_length=25)),
                ('productlength', models.CharField(max_length=25)),
                ('productwidth', models.CharField(max_length=25)),
                ('productweight', models.CharField(max_length=25)),
                ('superstratetype', models.CharField(max_length=25)),
                ('superstratemanufacturer', models.CharField(max_length=25)),
                ('substratetype', models.CharField(max_length=25)),
                ('substratemanufacturer', models.CharField(max_length=25)),
                ('frametype', models.CharField(max_length=25)),
                ('frameadhesive', models.CharField(max_length=25)),
                ('encapsulatetype', models.CharField(max_length=25)),
                ('encapsulantmanufacturer', models.CharField(max_length=25)),
                ('junctionboxtype', models.CharField(max_length=25)),
                ('junctionboxymanufacturer', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='performancedata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maxsystemvoltage', models.CharField(max_length=25)),
                ('voc', models.CharField(max_length=25)),
                ('isc', models.CharField(max_length=25)),
                ('vmp', models.CharField(max_length=25)),
                ('imp', models.CharField(max_length=25)),
                ('pmp', models.CharField(max_length=25)),
                ('ff', models.CharField(max_length=25)),
                ('modelnumber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.product')),
                ('sequenceid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.testSequence')),
            ],
        ),
    ]