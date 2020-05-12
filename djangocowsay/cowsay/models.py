from django.db import models
from django.utils import timezone
from datetime import datetime

# Create your models here.
class InputText(models.Model):
    COW_CHOICES = [
        ("default", "default"),
        ("beavis.zen","beavis.zen"),
        ("blowfish","blowfish"),
        ("bud-frogs","bud-frogs"),
        ("bunny","bunny"),
        ("cheese","cheese"),
        ("cower","cower"),
        ("daemon","daemon"),
        ("dragon","dragon"),
        ("dragon-and-cow","dragon-and-cow"),
        ("elephant","elephant"),
        ("elephant-in-snake","elephant-in-snake"),
        ("eyes","eyes"),
        ("flaming-sheep","flaming-sheep"),
        ("ghostbusters","ghostbusters"),
        ("head-in","head-in"),
        ("hellokitty","hellokitty"),
        ("kiss","kiss"),
        ("kitty","kitty"),
        ("koala","koala"),
        ("kosh","kosh"),
        ("luke-koala","luke-koala"),
        ("meow","meow"),
        ("milk","milk"),
        ("moofasa","moofasa"),
        ("moose","moose"),
        ("ren","ren"),
        ("sheep","sheep"),
        ("skeleton","skeleton"),
        ("small","small"),
        ("stegosaurus","stegosaurus"),
        ("stimpy","stimpy"),
        ("supermilker","supermilker"),
        ("surgery","surgery"),
        ("telebears","telebears"),
        ("three-eyes","three-eyes"),
        ("turkey","turkey"),
        ("turtle","turtle"),
        ("tux","tux"),
        ("udder","udder"),
        ("vader","vader"),
        ("vader-koala","vader-koala"),
        ("www","www")
    ]
    text = models.CharField(max_length=200)
    cow = models.CharField(
        max_length=20,
        choices=COW_CHOICES
    )
    

    def __str__(self):
        return self.text