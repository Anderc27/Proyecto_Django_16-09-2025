from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Usuario, Pregunta, Resultado
from django.core.mail import send_mail
from django.contrib.auth.hashers import make_password

@login_required
def dashboard(request):
    if request.user.rol == 'administrador':
        return redirect('admin_dashboard')
    elif request.user.rol == 'candidato':
        return redirect('examen')
    else:
        return redirect('logout')

@login_required
def admin_dashboard(request):
    if request.user.rol != 'administrador':
        return redirect('login')
    candidatos = Usuario.objects.filter(rol='candidato')
    resultados = Resultado.objects.all()
    return render(request, 'app_principal/admin_dashboard.html', {'candidatos': candidatos, 'resultados': resultados})

@login_required
def crear_candidato(request):
    if request.user.rol != 'administrador':
        return redirect('login')

    if request.method == 'POST':
        nombre = request.POST['nombre']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        
        candidato = Usuario.objects.create_user(
            username=username, email=email, password=password,
            rol='candidato', first_name=nombre
        )
        
        send_mail(
            'Inscripción al examen',
            f'Hola {nombre}, tu usuario es {username} y tu contraseña es {password}',
            'from@example.com',
            [email],
        )
        return redirect('admin_dashboard')
    return render(request, 'app_principal/crear_candidato.html')

@login_required
def presentar_examen(request):
    if request.user.rol != 'candidato':
        return redirect('login')
    
    resultado, created = Resultado.objects.get_or_create(candidato=request.user)
    
    if resultado.presentado:
        return render(request, 'app_principal/mensaje.html', {'puntaje': resultado.puntaje})
    
    preguntas = Pregunta.objects.all()[:10]
    
    if request.method == 'POST':
        puntaje = 0
        for pregunta in preguntas:
            resp = request.POST.get(f'pregunta_{pregunta.id}')
            if resp == pregunta.respuesta_correcta:
                puntaje += 1
        resultado.puntaje = puntaje
        resultado.presentado = True
        resultado.save()
        return render(request, 'app_principal/resultado.html', {'puntaje': puntaje})
    
    return render(request, 'app_principal/examen.html', {'preguntas': preguntas})
