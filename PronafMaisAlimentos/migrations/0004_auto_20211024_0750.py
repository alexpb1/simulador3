import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PronafMaisAlimentos', '0003_auto_20211023_0813'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entradasmaisalimentos',
            name='dataSimulacao',
        ),
        migrations.AlterField(
            model_name='entradasmaisalimentos',
            name='dataPrimeiraParcela',
            field=models.DateField(default=datetime.datetime(2021, 10, 24, 7, 50, 39, 558304)),
        ),
    ]
