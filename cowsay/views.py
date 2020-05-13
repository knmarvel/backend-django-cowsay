from django.shortcuts import render
from cowsay.forms import InputTextForm
from cowsay.models import InputText
from cowsay.helpers import cow_translator

def index(request):
    empty_form = InputTextForm()
    if request.method == 'POST':
        form = InputTextForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data.get("text").replace("'","")
            cow = form.cleaned_data.get("cow")
            display_text = cow_translator(text, cow)
            InputText.objects.create(
                text=text,
                cow=cow
            )

            return render(request, "index.html", {"text": text, "display_text": display_text, "empty_form": empty_form})
    return render(request, "index.html", {"empty_form": empty_form})

def history(request):
    objects_of_history_data = InputText.objects.all()
    objects_of_history_data = objects_of_history_data[len(objects_of_history_data)-10:]
    history_data = []
    for item in objects_of_history_data:
        history_data.append(cow_translator(item, item.cow))
    return render(request, "history.html", {"history_data": history_data})
