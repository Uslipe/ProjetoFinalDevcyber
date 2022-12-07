from django.shortcuts import render, redirect
from django.http import HttpResponse 
from .forms import CadastrarProduto

# Create your views here.

def cadastrar (request):
    if request.method == 'POST':
        form = CadastrarProduto(request.POST)

        if form.is_valid():
            done = form.save(commit = False)
            done.save()
            return redirect('/')
    else:
        form = CadastrarProduto()
        return render(request,'list.html', {'form': form})
        
    
    