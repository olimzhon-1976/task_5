from django.shortcuts import render, redirect
from .forms import RestaurantForm
from .models import Restaurant
from django.shortcuts import get_object_or_404

def add_restaurant(request):
    if request.method == 'POST':
        form = RestaurantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('restaurant_list')
    else:
        form = RestaurantForm()
    return render(request, 'restaurants/add_restaurant.html', {'form': form})



# def restaurant_list(request):
#    restaurants = Restaurant.objects.all()
#    return render(request, 'restaurants/restaurant_list.html', {'restaurants': restaurants})

def restaurant_list(request):
   query = request.GET.get('q')
   if query:
       restaurants = Restaurant.objects.filter(specialization__icontains=query)
   else:
       restaurants = Restaurant.objects.all()
   return render(request, 'restaurants/restaurant_list.html', {'restaurants': restaurants, 'query': query})


def delete_restaurant(request, id):
   restaurant = get_object_or_404(Restaurant, id=id)
   if request.method == 'POST':
       restaurant.delete()
       return redirect('restaurant_list')
   return render(request, 'restaurants/delete_restaurant.html', {'restaurant': restaurant})

def edit_restaurant(request, id):
   restaurant = get_object_or_404(Restaurant, id=id)
   if request.method == 'POST':
       form = RestaurantForm(request.POST, instance=restaurant)
       if form.is_valid():
           form.save()
           return redirect('restaurant_list')
   else:
       form = RestaurantForm(instance=restaurant)
   return render(request, 'restaurants/edit_restaurant.html', {'form': form, 'restaurant': restaurant})