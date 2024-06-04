# # from django.shortcuts import render, redirect
# # from .models import Recipes
# # from django.contrib import messages
# # from django.db.models import Q
# # from django.http import HttpResponseRedirect

# # def home(request):
# #     search_query = ""
# #     if request.method == 'POST':
# #         if 'create' in request.POST:
# #             title = request.POST.get('title')
# #             author = request.POST.get('author')
# #             description = request.POST.get('description')
# #             ingredients = request.POST.get('ingredients')
# #             Recipes.objects.create(title=title, author=author, description=description, ingredients=ingredients)
# #             messages.success(request, 'Recipe added successfully.')
# #             return redirect('home')

# #         elif 'search' in request.POST:
# #             search_query = request.POST.get('query')
# #             recipes = Recipes.objects.filter(Q(title__icontains = search_query))
        

# #         elif "update" in request.POST:
# #             id = request.POST.get("id")
# #             title = request.POST.get("title")
# #             author = request.POST.get("author")
# #             description = request.POST.get("description")
# #             ingredients = request.POST.get("ingredients")
            
# #             try:
# #                 recipe = Recipes.objects.get(id=id)
# #             except Recipes.DoesNotExist:
# #                 messages.error(request, "Recipe not found")
# #                 return HttpResponseRedirect('/')
            
# #             recipe.title = title
# #             recipe.author = author
# #             recipe.description = description
# #             recipe.ingredients = ingredients
            
# #             try:
# #                 recipe.save()
# #                 messages.success(request, "Recipe updated successfully")
# #             except Exception as e:
# #                 messages.error(request, f"An error occurred: {str(e)}")

# #             return HttpResponseRedirect('/')  # Redirect to the homepage or an appropriate page

# #         elif 'delete' in request.POST:
# #             recipe_id = request.POST.get('id')
# #             Recipes.objects.filter(id=recipe_id).delete()
# #             messages.success(request, 'Recipe deleted successfully.')
# #             return redirect('home')

# #     recipes = Recipes.objects.all()
# #     context = {'recipes': recipes, 'search_query': search_query}
# #     return render(request, 'home.html',context=context)
# from django.shortcuts import render, redirect
# from .models import Recipes
# from django.contrib import messages
# from django.db.models import Q
# from django.http import HttpResponseRedirect

# def home(request):
#     search_query = ""
#     recipes = Recipes.objects.all()  # Default queryset

#     if request.method == 'POST':
#         if 'create' in request.POST:
#             title = request.POST.get('title')
#             author = request.POST.get('author')
#             description = request.POST.get('description')
#             ingredients = request.POST.get('ingredients')
#             Recipes.objects.create(title=title, author=author, description=description, ingredients=ingredients)
#             messages.success(request, 'Recipe added successfully.')
#             return redirect('home')

#         elif 'search' in request.POST:
#             search_query = request.POST.get('query')
#             recipes = Recipes.objects.filter(Q(title__icontains=search_query))
        
#         elif "update" in request.POST:
#             id = request.POST.get("id")
#             title = request.POST.get("title")
#             author = request.POST.get("author")
#             description = request.POST.get("description")
#             ingredients = request.POST.get("ingredients")
            
#             try:
#                 recipe = Recipes.objects.get(id=id)
#             except Recipes.DoesNotExist:
#                 messages.error(request, "Recipe not found")
#                 return HttpResponseRedirect('/')
            
#             recipe.title = title
#             recipe.author = author
#             recipe.description = description
#             recipe.ingredients = ingredients
            
#             try:
#                 recipe.save()
#                 messages.success(request, "Recipe updated successfully")
#             except Exception as e:
#                 messages.error(request, f"An error occurred: {str(e)}")

#             return HttpResponseRedirect('/')  # Redirect to the homepage or an appropriate page

#         elif 'delete' in request.POST:
#             recipe_id = request.POST.get('id')
#             Recipes.objects.filter(id=recipe_id).delete()
#             messages.success(request, 'Recipe deleted successfully.')
#             return redirect('home')

#     context = {'recipes': recipes, 'search_query': search_query}
#     return render(request, 'home.html', context=context)
from django.shortcuts import render, redirect
from .models import Recipes
from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import Recipes

#translation 

def home(request):
    search_query = ""
    recipes = Recipes.objects.all()  # Default queryset

    if request.method == 'POST':
        if 'create' in request.POST:
            title = request.POST.get('title')
            author = request.POST.get('author')
            description = request.POST.get('description')
            ingredients = request.POST.get('ingredients')
            image = request.FILES.get('image')
            video = request.FILES.get('video')
            
            new_recipe = Recipes.objects.create(
                title=title,
                author=author,
                description=description,
                ingredients=ingredients
            )
            
            if image:
                new_recipe.image = image
                new_recipe.save()
            if video:
                new_recipe.video = video
                new_recipe.save()
                
            messages.success(request, 'Recipe added successfully.')
            return redirect('home')

        elif 'search' in request.POST:
            search_query = request.POST.get('query')
            recipes = Recipes.objects.filter(Q(title__icontains=search_query))
        
        elif 'update' in request.POST:
            id = request.POST.get('id')
            title = request.POST.get('title')
            author = request.POST.get('author')
            description = request.POST.get('description')
            ingredients = request.POST.get('ingredients')
            image = request.FILES.get('image')
            video = request.FILES.get('video')
            
            try:
                recipe = Recipes.objects.get(id=id)
            except Recipes.DoesNotExist:
                messages.error(request, 'Recipe not found')
                return redirect('home')
            
            recipe.title = title
            recipe.author = author
            recipe.description = description
            recipe.ingredients = ingredients
            
            if image:
                recipe.image = image
            if video:
                recipe.video = video
            
            try:
                recipe.save()
                messages.success(request, 'Recipe updated successfully.')
            except Exception as e:
                messages.error(request, f'An error occurred: {str(e)}')

            return redirect('home')

        elif 'delete' in request.POST:
           if request.user.is_authenticated:
             recipe_id = request.POST.get('id')
             Recipes.objects.filter(id=recipe_id).delete()
             messages.success(request, 'Recipe deleted successfully.')
           else:
              messages.error(request, 'You are not authorized to delete recipes.')
        return redirect('home')


    context = {'recipes': recipes, 'search_query': search_query}
    return render(request, 'home.html', context)


def about(request):
    return render(request, 'about.html')
def services(request):
    return render(request, 'services.html')
def contact(request):
    return render(request, 'contact.html')



# authetication

from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .middelware import auth,geust
from .import forms

@geust
def register_view(request):
    
    if request.method == 'POST':
        form = forms.CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Correct way to log the user in
            return redirect('dashboard')
    else:
        initial_data = {'username':'','email':'', 'password1':'','password2':""}
        form = UserCreationForm(initial=initial_data)
    return render(request, 'register.html',{'form':form})
@geust
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
            else:
                messages.error(request, 'Invalid username or password')
        else:
            messages.error(request, 'Invalid username or password')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})
@auth
def dashboard_view(request):

    recipes = Recipes.objects.filter(author=request.user)
    
    # Pass recipes to the template
    return render(request, 'dashboard.html', {'recipes': recipes})


def logout_view(request):
    logout(request)
    return redirect('login')

def add_recipe_view(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        # Include other fields like author, description, ingredients, and image
        author = request.user  # Associate the recipe with the current logged-in user
        description = request.POST.get('description')
        ingredients = request.POST.get('ingredients')
        image = request.FILES.get('image')
        video = request.FILES.get('video')

        # Create the recipe object
        new_recipe = Recipes(title=title, author=author, description=description, ingredients=ingredients, image=image,video=video)
        new_recipe.save()
        
        
    elif 'update' in request.POST:
            id = request.POST.get('id')
            title = request.POST.get('title')
            author = request.user
            description = request.POST.get('description')
            ingredients = request.POST.get('ingredients')
            image = request.FILES.get('image')
            video = request.FILES.get('video')
            
            try:
                recipe = Recipes.objects.get(id=id)
            except Recipes.DoesNotExist:
                messages.error(request, 'Recipe not found')
                return redirect('dashboard')
            
            recipe.title = title
            recipe.author = author
            recipe.description = description
            recipe.ingredients = ingredients
            
            if image:
                recipe.image = image
            if video:
                recipe.video = video
            
            try:
                recipe.save()
                messages.success(request, 'Recipe updated successfully.')
            except Exception as e:
                messages.error(request, f'An error occurred: {str(e)}')

            return redirect('dashboard')

        
        # Redirect back to the dashboard after adding the recipe
    return redirect('dashboard')
     

