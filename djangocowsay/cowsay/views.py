from django.shortcuts import render
from cowsay.forms import InputTextForm
from cowsay.models import InputText

def index(request):
    empty_form = InputTextForm
    if request.method == 'POST':
        form = InputTextForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data
            display_text = form.cleaned_data.get('text')
            InputText.objects.create(
                text=display_text
            )
            return render(request, "index.html", {"display_text": display_text, "empty_form": empty_form})

    display_text = "foo"
    return render(request, "index.html", {"display_text": display_text, "empty_form": empty_form})
