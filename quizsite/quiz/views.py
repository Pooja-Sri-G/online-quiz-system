from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from .models import Question
from .models import Result

import io
from reportlab.pdfgen import canvas

# USER SIGNUP
def signup_view(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=username).exists():
            return render(request, 'quiz/signup.html', {'error': 'Username already exists'})

        user = User.objects.create_user(username=username, email=email, password=password)
        return redirect('login')

    return render(request, 'quiz/signup.html')

# USER LOGIN
def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'quiz/login.html', {'error': 'Invalid username or password'})

    return render(request, 'quiz/login.html')

# LOGOUT
def logout_view(request):
    logout(request)
    return redirect('login')

# DASHBOARD
def dashboard_view(request):
    return render(request, 'quiz/dashboard.html')

# DISPLAY QUIZ
def quiz_view(request):
    questions = Question.objects.all()
    return render(request, 'quiz/quiz.html', {'questions': questions})

# QUIZ SUBMISSION
def submit_quiz_view(request):
    if request.method == "POST":

        questions = Question.objects.all()
        total = questions.count()
        score = 0

        for q in questions:
            user_answer = request.POST.get(f"q{q.id}")
            if user_answer and user_answer == q.correct_answer:
                score += 1

        percentage = round((score / total) * 100, 2) if total > 0 else 0

        Result.objects.create(
            user=request.user,      
            score=score,
            total=total,
            percentage=percentage
        )
        
        request.session['score'] = score
        request.session['percentage'] = percentage
        request.session['total'] = total

        return render(request, 'quiz/result.html', {
            "score": score,
            "total": total,
            "percentage": percentage,
            "username": request.user.username
        })

    return redirect('quiz')

# CERTIFICATE PDF DOWNLOAD
def certificate_view(request):
    user = request.user
    score = request.session.get('score')
    percentage = request.session.get('percentage')

    buffer = io.BytesIO()
    p = canvas.Canvas(buffer)

    p.setFont("Helvetica-Bold", 24)
    p.drawString(140, 800, "Certificate of Completion")

    p.setFont("Helvetica", 14)
    p.drawString(100, 750, f"Name: {user.username}")
    p.drawString(100, 720, f"Email: {user.email}")
    p.drawString(100, 690, f"Score: {score}")
    p.drawString(100, 660, f"Percentage: {percentage:.2f}%")

    p.drawString(100, 620, "Congratulations on successfully completing the quiz!")

    p.showPage()
    p.save()

    buffer.seek(0)
    return HttpResponse(buffer, content_type='application/pdf')

