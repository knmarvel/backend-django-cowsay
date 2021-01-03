from django.shortcuts import render
from cowsay.forms import InputTextForm
from cowsay.models import InputText
from cowsay.helpers import cow_translator


def index(request):
    empty_form = InputTextForm()
    if request.method == 'POST':
        form = InputTextForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data.get("text").replace("'", "")
            cow = form.cleaned_data.get("cow")
            display_text = cow_translator(text, cow)
            InputText.objects.create(
                text=text,
                cow=cow
            )

            return render(
                request,
                "index.html",
                {"display_text": display_text,
                    "empty_form": empty_form})
    return render(request, "index.html", {"empty_form": empty_form})


def history(request):
    moo_history = InputText.objects.all()
    if len(moo_history) > 10:
        moo_history = moo_history[len(moo_history)-10:]
    history_data = []
    for item in moo_history:
        history_data.append(cow_translator(item.text, item.cow))
    return render(request, "history.html", {"history_data": history_data})
