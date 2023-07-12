from django.shortcuts import render
from .form import ImageForm
from .models import Image

# Create your views here.
def home(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)   #whenever working with Images in form need to add request.FILES.
        if form.is_valid():
            form.save()
    form = ImageForm()
    img = Image.objects.all()
    return render(request, 'myapp/home.html',{'img':img,'form':form})