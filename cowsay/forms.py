from django import forms


class InputTextForm(forms.Form):
    COW_CHOICES = [
        ("default", "default"),
        ("bud-frogs", "bud-frogs"),
        ("bunny", "bunny"),
        ("calvin", "calvin")
        ("cheese", "cheese"),
        ("cower", "cower"),
        ("daemon", "daemon"),
        ("dragon", "dragon"),
        ("dragon-and-cow", "dragon-and-cow"),
        ("duck", "duck"),
        ("elephant", "elephant"),
        ("elephant-in-snake", "elephant-in-snake"),
        ("eyes", "eyes"),
        ("flaming-sheep", "flaming-sheep"),
        ("fox", "fox"),
        ("ghostbusters", "ghostbusters"),
        ("gnu", "gnu"),
        ("hellokitty", "hellokitty"),
        ("kangaroo", "kangaroo"),
        ("kiss", "kiss"),
        ("kitty", "kitty"),
        ("koala", "koala"),
        ("kosh", "kosh"),
        ("luke-koala", "luke-koala"),
        ("mech-and-cow", "mech-and-cow"),
        ("milk", "milk"),
        ("moofasa", "moofasa"),
        ("moose", "moose"),
        ("pony", "pony"),
        ("pony-smaller", "pony-smaller"),
        ("ren", "ren"),
        ("sheep", "sheep"),
        ("skeleton", "skeleton"),
        ("snowman", "snowman"),
        ("stegosaurus", "stegosaurus"),
        ("stimpy", "stimpy"),
        ("suse", "suse"),
        ("three-eyes", "three-eyes"),
        ("turkey", "turkey"),
        ("turtle", "turtle"),
        ("tux", "tux"),
        ("unipony", "unipony"),
        ("unipony-smaller", "unipony-smaller"),
        ("vader", "vader"),
        ("vader-koala", "vader-koala"),
        ("www", "www")
    ]
    text = forms.CharField(max_length=200)
    cow = forms.ChoiceField(
        widget=forms.Select,
        choices=COW_CHOICES
    )

    def __str__(self):
        return self.text
