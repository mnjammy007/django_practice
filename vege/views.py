from django.shortcuts import render, redirect
from .models import Recipe, Student, SubjectMarks
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q, Sum
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your views here.


@login_required(login_url="/vege/login")
def recipes(request):
    if request.method == "POST":
        data = request.POST
        recipe_name = data.get("recipe_name")
        recipe_description = data.get("recipe_description")
        recipe_image = request.FILES.get("recipe_image")
        Recipe.objects.create(
            recipe_name=recipe_name,
            recipe_description=recipe_description,
            recipe_image=recipe_image,
        )
        return redirect("/vege/recipes")

    queryset = Recipe.objects.all()

    if request.GET.get("search"):
        queryset = queryset.filter(recipe_name__icontains=request.GET.get("search"))

    context = {"recipes": queryset}
    return render(request, "recipes.html", context=context)


@login_required(login_url="/vege/login")
def delete_recipe(request, id):
    try:
        Recipe.objects.get(id=id).delete()
    except:
        pass
    return redirect("/vege/recipes")


@login_required(login_url="/vege/login")
def update_recipe(request, id):
    queryset = Recipe.objects.get(id=id)
    if request.method == "POST":
        data = request.POST
        recipe_image = request.FILES.get("recipe_image")
        recipe_name = data.get("recipe_name")
        recipe_description = data.get("recipe_description")

        queryset.recipe_name = recipe_name
        queryset.recipe_description = recipe_description
        if recipe_image:
            queryset.recipe_image = recipe_image

        queryset.save()
        return redirect("/vege/recipes")

    # will execute if the URL being requested has a query
    # parameter named search. For example, if the URL is
    #  http://127.0.0.1:8000/vege/update_recipe/1?search=tomato
    if request.GET.get("search"):
        print("Nasir", request.GET.get("search"))

    context = {"recipe": queryset}
    return render(request, "update_recipes.html", context=context)


def login_page(request):
    if request.method == "POST":
        data = request.POST
        username = data.get("username")
        password = data.get("password")
        if not User.objects.filter(username=username).exists():
            messages.error(request, "User does not exist")
            return redirect("/vege/login")
        user = authenticate(username=username, password=password)
        if user is None:
            messages.error(request, "Invalid password")
            return redirect("/vege/login")
        else:
            login(request, user)
            return redirect("/vege/recipes")
    return render(request, "login.html")


def logout_page(request):
    logout(request)
    return redirect("/vege/login")


def register(request):
    if request.method == "POST":
        data = request.POST
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        username = data.get("username")
        password = data.get("password")

        user = User.objects.filter(username=username)
        if user.exists():
            messages.error(request, "User already exists")
            return redirect("/vege/register")

        user = User.objects.create(
            first_name=first_name, last_name=last_name, username=username
        )
        user.set_password(password)
        user.save()
        messages.success(request, "User created successfully")
        return redirect("/vege/login")
    return render(request, "register.html")


def get_students(request):
    queryset = Student.objects.all()

    search_key = request.GET.get("search")

    if search_key:
        queryset = queryset.filter(
            Q(student_name__icontains=search_key)
            | Q(student_email__icontains=search_key)
            | Q(student_id__student_id__icontains=search_key)
            | Q(department__department__icontains=search_key)
        )

    paginator = Paginator(queryset, 25)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {"students": page_obj}
    return render(request, "report/students.html", context=context)


def get_student_marks(request, student_id):
    queryset = SubjectMarks.objects.filter(student__student_id__student_id=student_id)
    total_marks = queryset.aggregate(total_marks=Sum("marks"))
    context = {"student_marks": queryset, "total_marks": total_marks}
    return render(request, "report/student_marks.html", context=context)
