import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PronafMaisAlimentos', '0002_entradasmaisalimentos_resultado'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entradasmaisalimentos',
            name='resultado',
        ),
        migrations.AddField(
            model_name='entradasmaisalimentos',
            name='dataPrimeiraParcela',
            field=models.DateField(default=datetime.datetime(2021, 10, 23, 8, 13, 12, 694825), max_length=10),
        ),
        migrations.AddField(
            model_name='entradasmaisalimentos',
            name='dataSimulacao',
            field=models.DateField(default=datetime.datetime(2021, 10, 23, 8, 13, 12, 694825), max_length=10),
        ),
    ]
