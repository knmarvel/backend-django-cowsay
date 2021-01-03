# Generated by Django 3.0.6 on 2021-01-03 22:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='InputText',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200)),
                ('cow', models.CharField(choices=[('default', 'default'), ('bud-frogs', 'bud-frogs'), ('bunny', 'bunny'), ('calvin', 'calvin'), ('cheese', 'cheese'), ('cower', 'cower'), ('daemon', 'daemon'), ('dragon', 'dragon'), ('dragon-and-cow', 'dragon-and-cow'), ('duck', 'duck'), ('elephant', 'elephant'), ('elephant-in-snake', 'elephant-in-snake'), ('eyes', 'eyes'), ('flaming-sheep', 'flaming-sheep'), ('fox', 'fox'), ('ghostbusters', 'ghostbusters'), ('gnu', 'gnu'), ('hellokitty', 'hellokitty'), ('kangaroo', 'kangaroo'), ('kiss', 'kiss'), ('kitty', 'kitty'), ('koala', 'koala'), ('kosh', 'kosh'), ('luke-koala', 'luke-koala'), ('mech-and-cow', 'mech-and-cow'), ('milk', 'milk'), ('moofasa', 'moofasa'), ('moose', 'moose'), ('pony', 'pony'), ('pony-smaller', 'pony-smaller'), ('ren', 'ren'), ('sheep', 'sheep'), ('skeleton', 'skeleton'), ('snowman', 'snowman'), ('stegosaurus', 'stegosaurus'), ('stimpy', 'stimpy'), ('suse', 'suse'), ('three-eyes', 'three-eyes'), ('turkey', 'turkey'), ('turtle', 'turtle'), ('tux', 'tux'), ('unipony', 'unipony'), ('unipony-smaller', 'unipony-smaller'), ('vader', 'vader'), ('vader-koala', 'vader-koala'), ('www', 'www')], max_length=20)),
            ],
        ),
    ]
