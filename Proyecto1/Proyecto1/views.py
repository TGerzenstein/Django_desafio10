from django.shortcuts import render

def index(request):

    template_name = 'index.html'
    nombres = ['A','B','C']
    contexto = {'nombres': nombres}
    
    return render(request, template_name, contexto)
