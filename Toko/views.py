from django.shortcuts import render
from .models import Toko
from .forms import TokoForm

# Create your views here.

def tampilan_toko(request):
    list_barang = Toko.objects.all()
    return render(request, 'Toko/toko.html', {'list_barang': list_barang })

def input_post(request):
    if request.method == "POST":
        form = TokoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('toko')
    else :
        form = TokoForm()
    return render(request, 'Toko/toko_form.html', {'form' : form})

def toko_detail(request, toko_id):
    barang = Toko.objects.get(pk=toko_id)
    return render(request, 'Toko/toko_detail.html', {'barang' : barang})