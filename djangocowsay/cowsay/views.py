from django.shortcuts import render
from cowsay.forms import InputTextForm
from cowsay.models import InputText
import subprocess

def index(request):
    empty_form = InputTextForm()
    if request.method == 'POST':
        form = InputTextForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data.get('text')
            display_text = cow_translator(text, "cow")
            InputText.objects.create(
                text=text
            )

            return render(request, "index.html", {"text": text, "display_text": display_text, "empty_form": empty_form})
    return render(request, "index.html", {"empty_form": empty_form})

def history(request):
    objects_of_history_data = InputText.objects.all()
    objects_of_history_data = objects_of_history_data[len(objects_of_history_data)-10:]
    history_data = []
    for item in objects_of_history_data:
        history_data.append(cow_translator(item, "cow"))
    return render(request, "history.html", {"history_data": history_data})

def cow_translator(text, cow_version):
    if cow_version == "cow":
        display_text = subprocess.Popen(f"cowsay {text}", shell=True, stdout=subprocess.PIPE).stdout.read()
        return display_text.decode('utf8')