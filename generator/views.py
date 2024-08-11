from django.shortcuts import render, redirect
from django.forms import formset_factory
from .forms import TextInputForm
from .models import GeneratedImage
from .tasks import generate_image_task

def home_view(request):
    TextInputFormSet = formset_factory(TextInputForm, extra=1)

    if request.method == 'POST':
        formset = TextInputFormSet(request.POST)
        
        # Check if the formset is valid
        if formset.is_valid():
            text_inputs = [form.cleaned_data['text_input'] for form in formset if form.cleaned_data.get('text_input')]

            if not text_inputs:
                return render(request, 'generator/home.html', {'formset': formset, 'error': 'At least one valid text input is required.'})

            for text_input in text_inputs:
                generate_image_task.delay(text_input)

            return redirect('generate_image')
        else:
            print("Formset errors:", formset.errors)
    
    else:
        formset = TextInputFormSet()

    return render(request, 'generator/home.html', {'formset': formset})

def generate_image_view(request):
    return render(request, 'generator/generate.html')

def display_all_images_view(request):
    images = GeneratedImage.objects.all().order_by('-created_at')
    return render(request, 'generator/display_all.html', {'images': images})
