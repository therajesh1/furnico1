from django.shortcuts import render

# Create your views here.
# ecommerce/views.py

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Product, Category,Contact
from django.core.mail import send_mail

# ecommerce/views.py




from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


# views.py
from django.shortcuts import render, redirect
from .models import Product, Category, Customer, Shopkeeper

# views.py
from django.shortcuts import render, redirect
from .models import Product, Category, Customer, Shopkeeper




from django.shortcuts import render
from .models import Product, Customer, Shopkeeper, Category

from django.shortcuts import render
from .models import Product, Category
import random

# def home(request):
#     # Fetch all products that are not out of stock
#     all_products = list(Product.objects.filter(is_out_of_stock=False))

#     # Check if there are any products available
#     if len(all_products) > 0:
#         # Randomly select 9 products
#         products = random.sample(all_products, min(9, len(all_products)))  # Ensure no more than available
#     else:
#         products = []  # No products available

#     # Fetch all categories
#     categories = Category.objects.all()
    
#     # Render the template with the context
#     return render(request, 'home.html', {
#         'products': products, 
#         'categories': categories
#     })

import random
from django.shortcuts import render
from .models import Product, Category

# def home(request):
#     # Get the selected city from query parameter or session
#     selected_city = request.GET.get('city', request.session.get('selected_city', None))

#     # Store the selected city in session for persistence
#     if selected_city:
#         request.session['selected_city'] = selected_city

#     # Fetch all products that are not out of stock and belong to shops in the selected city
#     if selected_city:
#         all_products = list(Product.objects.filter(is_out_of_stock=False, shopkeeper__city=selected_city))
#     else:
#         all_products = list(Product.objects.filter(is_out_of_stock=False))

#     # Check if there are any products available
#     if len(all_products) > 0:
#         # Randomly select up to 9 products
#         products = random.sample(all_products, min(9, len(all_products)))
#     else:
#         products = []

#     # Fetch all categories
#     categories = Category.objects.all()

#     # Render the template with the context
#     return render(request, 'home.html', {
#         'products': products, 
#         'categories': categories,
#         'selected_city': selected_city
#     })

import random
from django.shortcuts import render
from .models import Product, Category

def home(request):
    # Get the selected city from query parameter or session
    selected_city = request.GET.get('city', request.session.get('selected_city', None))

    # Store the selected city in session for persistence
    if selected_city:
        request.session['selected_city'] = selected_city

    # Filter products based on stock availability and selected city
    products_query = Product.objects.filter(is_out_of_stock=False)
    
    if selected_city:
        products_query = products_query.filter(shopkeeper__city__iexact=selected_city)

    # Randomly select up to 9 products
    products = random.sample(list(products_query), min(9, products_query.count())) if products_query.exists() else []

    # Fetch all categories
    categories = Category.objects.all()

    # Render the template with the context
    return render(request, 'home.html', {
        'products': products, 
        'categories': categories,
        'selected_city': selected_city
    })

# ecommerce/views.py
from django.contrib.auth.models import User

from django.shortcuts import render, redirect
from .models import Shopkeeper

# eco/views.py



from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Shopkeeper, Customer
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Shopkeeper, Customer

def register_shopkeeper(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        shop_name = request.POST['shop_name']
        address = request.POST['address']
        city = request.POST['city']
        phone_number = request.POST['phone_number']
        terms_accepted = request.POST.get('terms_accepted')  # Check if terms are accepted

        if terms_accepted:  # Ensure the shopkeeper accepts the terms
            # Check if the username already exists
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists. Please choose a different username.')
            else:
                # Create user
                user = User.objects.create_user(username=username, password=password)
                # Create shopkeeper instance
                shopkeeper = Shopkeeper(user=user, shop_name=shop_name, address=address, city=city, phone_number=phone_number)
                shopkeeper.save()
                messages.success(request, 'Registration successful! You can now log in.')
                return redirect('/login')  # Redirect after registration

    return render(request, 'register_shopkeeper.html')


def register_customer(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        address = request.POST['address']
        city = request.POST['city']
        phone_number = request.POST['phone_number']

        # Check if the username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists. Please choose a different username.')
        else:
            # Create user
            user = User.objects.create_user(username=username, password=password)
            # Create customer instance
            customer = Customer(user=user, address=address, city=city, phone_number=phone_number)
            customer.save()
            messages.success(request, 'Registration successful! You can now log in.')
            return redirect('/login')  # Redirect after registration

    return render(request, 'register_customer.html')



def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'product_detail.html', {'product': product})




from django.shortcuts import redirect, get_object_or_404
from .models import  Product








def signin(request):
    return render(request,'signin.html')

from datetime import datetime

# @login_required(login_url='login')
def contact(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        msg=request.POST.get('msg')
        contact=Contact(name=name,email=email,phone=phone,msg=msg,date=datetime.today())
        contact.save()
        messages.success(request, "your message has been sent")

    return render(request,'contact.html')


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Product, Shopkeeper

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Product, Shopkeeper, Category
# import markdown

# def process_description(description_text):
#     return markdown.markdown(description_text)


@login_required
def add_product(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        description = request.POST.get('description')
        category_id = request.POST.get('category')  # Assuming you pass category ID from the template
        price = request.POST.get('price')
        # description_html = markdown.markdown(description)

        # Handle multiple file uploads
        image = request.FILES.get('image')  # For image1
        image2 = request.FILES.get('image2')  # For image2
        image3 = request.FILES.get('image3')  # For image3
        image4 = request.FILES.get('image4')  # For image4
        # model3d = request.FILES.get('model_3d')  # For the 3D model

        # Create the product instance
        product = Product(
            shopkeeper=Shopkeeper.objects.get(user=request.user),
            name=name,
            description=description,
            # description=description_html,  # Save the HTML version of the description

            category_id=category_id,
            price=price,
            image=image,
            image2=image2,
            image3=image3,
            image4=image4,
            # model3d=model3d,  # Save the 3D model file

            is_out_of_stock=False  # Default value
        )
        product.save()
        return redirect('/add_product')  # Redirect to home or a success page

    # If GET request, render the add product page
    categories = Category.objects.all()  # Fetch categories to display in the template
    return render(request, 'add_product.html', {'categories': categories})




from django.contrib.auth import authenticate, login
from .models import Customer, Shopkeeper


# from django.http import JsonResponse
# from .models import Product

# def product_search_api(request):
#     query = request.GET.get("query", "")
#     keywords = query.split()
#     products = Product.objects.all()

#     for keyword in keywords:
#         products = products.filter(
#             name__icontains=keyword
#         ) | products.filter(description__icontains=keyword)

#     results = [
#         {
#             "id": product.id,
#             "name": product.name,
#             "description": product.description,
#             "image_url": product.image.url if product.image else "",
#         }
#         for product in products
#     ]
#     return JsonResponse(results, safe=False)


#2nd best
# from django.db.models import Q

# def product_search_api(request):
#     query = request.GET.get("query", "")
#     keywords = query.split()  # Split query into individual keywords
#     products = Product.objects.all()

#     # Initialize the query filter to be an empty Q object
#     query_filter = Q()

#     # Loop through keywords and combine them with AND logic (all conditions must match)
#     for keyword in keywords:
#         query_filter &= (Q(name__icontains=keyword) | Q(description__icontains=keyword))

#     # Apply the combined filter to the queryset
#     products = products.filter(query_filter)

#     results = [
#         {
#             "id": product.id,
#             "name": product.name,
#             "description": product.description,
#             "image_url": product.image.url if product.image else "",
#         }
#         for product in products
#     ]
#     return JsonResponse(results, safe=False)



from django.http import JsonResponse
from django.db.models import Q
from .models import Product

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import InternshipApplications

def internship_registration(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        college = request.POST.get('college')
        year = request.POST.get('year')
        role = request.POST.get('role')
        resume = request.FILES.get('resume')
 


        

        

        InternshipApplications.objects.create(
            name=name,
            email=email,
            college=college,
            year=year,
            role=role,
            resume=resume
        )
        return redirect('internship_registration')

    return render(request, 'internship_registration.html')



def product_search(request):
    query = request.GET.get("query", "")
    keywords = query.split()
    
    # Start with all products
    products = Product.objects.all()

    # Use Q objects to combine filters logically (OR) for name and description
    query_filter = Q()
    for keyword in keywords:
        query_filter &= (Q(name__icontains=keyword) | Q(description__icontains=keyword))


    # Apply the filter to the products
    products = products.filter(query_filter)

    # Prepare the results
    # results = [
    #     {
    #         "id": product.id,
    #         "name": product.name,
    #         "description": product.description,
    #         "image_url": product.image.url if product.image else "",
    #     }
    #     for product in products
    # ]

    # return JsonResponse(results, safe=False)
    return render(request, 'search_results.html', {'products': products, 'query': query})



from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Shopkeeper, Customer


from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib.auth.models import User



def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user_type = request.POST['user_type']  # Get the user type from the form
        
        # Check if the user exists in the database
        if not User.objects.filter(username=username).exists():
            messages.error(request, 'Username does not exist.')
        else:
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect based on user type
                if user_type == 'shopkeeper' and hasattr(user, 'shopkeeper'):
                    return redirect('add_product')  # Redirect to add product page for shopkeepers
                elif user_type == 'customer' and hasattr(user, 'customer'):
                    return redirect('home')  # Redirect to home for customers
                else:
                    messages.error(request, 'User type mismatch. Please select the correct user type.')
            else:
                messages.error(request, 'Incorrect password. Please try again.')

    return render(request, 'login.html')



# from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return redirect('login')  # Redirect to login page after logout



# views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product
from django.contrib import messages


from django.shortcuts import get_object_or_404, redirect
from .models import Product, Shopkeeper
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Product

@login_required
def manage_products(request):
    # Check if the user is a shopkeeper
    if not hasattr(request.user, 'shopkeeper'):
        return redirect('error_page')  # Redirect customers or unauthorized users

    # Get the shopkeeper instance
    # shopkeeper = request.user.shopkeeper
    try:
        shopkeeper = Shopkeeper.objects.get(user=request.user)
    except Shopkeeper.DoesNotExist:
        return redirect('error_page')  # Redirect if the user is not a shopkeeper
    # Fetch the products for the shopkeeper
    products = Product.objects.filter(shopkeeper=shopkeeper)

    return render(request, 'manage_products.html', {'products': products})

@login_required
def delete_product(request, product_id):
    # Get the product instance or 404 if not found
    product = get_object_or_404(Product, id=product_id)

    # Ensure the product belongs to the logged-in shopkeeper
    if product.shopkeeper != request.user.shopkeeper:
        return redirect('error_page')  # Redirect if the shopkeeper does not own the product

    product.delete()  # Delete the product
    return redirect('manage_products')  # Redirect back to manage products

@login_required
def toggle_stock_status(request, product_id):
    # Get the product instance or 404 if not found
    product = get_object_or_404(Product, id=product_id)

    # Ensure the product belongs to the logged-in shopkeeper
    if product.shopkeeper != request.user.shopkeeper:
        return redirect('error_page')  # Redirect if the shopkeeper does not own the product

    # Toggle the stock status
    product.is_out_of_stock = not product.is_out_of_stock
    product.save()  # Save the product with the new stock status

    return redirect('manage_products')  # Redirect back to manage products




from django.shortcuts import render
from django.views import View  # Import the View class
from .models import Product  # Assuming you have a Product model
from django.shortcuts import render
from django.views import View
from .models import Product

class SofaView(View):
    def get(self, request):
        # Get the selected city from query parameter or session
        selected_city = request.GET.get('city', request.session.get('selected_city', None))

        # Store the selected city in session for persistence
        if selected_city:
            request.session['selected_city'] = selected_city

        # Fetch products that are from the 'Sofa' category and belong to shopkeepers in the selected city
        if selected_city:
            # Filter by category 'Sofa' and shopkeeper's cities
            products = Product.objects.filter(category__name='Sofa', shopkeeper__city=selected_city)
        else:
            # If no city is selected, just filter by the 'Sofa' category
            products = Product.objects.filter(category__name='Sofa')

        # Render the template with the filtered products
        return render(request, 'sofa.html', {'products': products, 'selected_city': selected_city})

# class SofaView(View):
#     def get(self, request):
#         products = Product.objects.filter(category__name='Sofa')  # Filter products by category
#         return render(request, 'sofa.html', {'products': products})


class ShoeView(View):
     def get(self, request):
        # Get the selected city from query parameter or session
        selected_city = request.GET.get('city', request.session.get('selected_city', None))

        # Store the selected city in session for persistence
        if selected_city:
            request.session['selected_city'] = selected_city

        # Fetch products that are from the 'Sofa' category and belong to shopkeepers in the selected city
        if selected_city:
            # Filter by category 'Sofa' and shopkeeper's cities
            products = Product.objects.filter(category__name='Shoerack', shopkeeper__city=selected_city)
        else:
            # If no city is selected, just filter by the 'Sofa' category
            products = Product.objects.filter(category__name='Shoerack')

        # Render the template with the filtered products
        return render(request, 'shoerack.html', {'products': products, 'selected_city': selected_city})
# class BedView(View):
#     def get(self, request):
#         products = Product.objects.filter(category__name='Bed')  # Filter products by category
#         return render(request, 'bed.html', {'products': products})
from django.views import View
from django.shortcuts import render
from .models import Product

class MandirView(View):
    def get(self, request):
        # Get the selected city from query parameter or session
        selected_city = request.GET.get('city', request.session.get('selected_city', None))

        # Store the selected city in session for persistence
        if selected_city:
            request.session['selected_city'] = selected_city
            products = Product.objects.filter(category__name='Mandir', shopkeeper__city=selected_city)
        else:
            products = None  # No products if city is not selected

        return render(request, 'mandir.html', {'products': products, 'selected_city': selected_city})


# class MandirView(View):
#     def get(self, request):
#         products = Product.objects.filter(category__name='Mandir')  # Filter products by category
#         return render(request, 'mandir.html', {'products': products})
# class TableView(View):
#     def get(self, request):
#         products = Product.objects.filter(category='Table')  # Filter products by category
#         return render(request, 'table.html', {'products': products})
class TableView(View):
    def get(self, request):
        # Get the selected city from query parameter or session
        selected_city = request.GET.get('city', request.session.get('selected_city', None))

        # Store the selected city in session for persistence
        if selected_city:
            request.session['selected_city'] = selected_city

        # Fetch products that are from the 'Sofa' category and belong to shopkeepers in the selected city
        if selected_city:
            # Filter by category 'Sofa' and shopkeeper's cities
            products = Product.objects.filter(category__name='Table', shopkeeper__city=selected_city)
        else:
            # If no city is selected, just filter by the 'Sofa' category
            products = Product.objects.filter(category__name='Table')

        # Render the template with the filtered products
        return render(request, 'table.html', {'products': products, 'selected_city': selected_city})


class ChairView(View):
    def get(self, request):
        # Get the selected city from query parameter or session
        selected_city = request.GET.get('city', request.session.get('selected_city', None))

        # Store the selected city in session for persistence
        if selected_city:
            request.session['selected_city'] = selected_city

        # Fetch products that are from the 'Sofa' category and belong to shopkeepers in the selected city
        if selected_city:
            # Filter by category 'Sofa' and shopkeeper's cities
            products = Product.objects.filter(category__name='Chair', shopkeeper__city=selected_city)
        else:
            # If no city is selected, just filter by the 'Sofa' category
            products = Product.objects.filter(category__name='Chair')

        # Render the template with the filtered products
        return render(request, 'chair.html', {'products': products, 'selected_city': selected_city})

class CupboardView(View):
    def get(self, request):
        # Get the selected city from query parameter or session
        selected_city = request.GET.get('city', request.session.get('selected_city', None))

        # Store the selected city in session for persistence
        if selected_city:
            request.session['selected_city'] = selected_city

        # Fetch products that are from the 'Sofa' category and belong to shopkeepers in the selected city
        if selected_city:
            # Filter by category 'Sofa' and shopkeeper's cities
            products = Product.objects.filter(category__name='Cupboard', shopkeeper__city=selected_city)
        else:
            # If no city is selected, just filter by the 'Sofa' category
            products = Product.objects.filter(category__name='Cupboard')

        # Render the template with the filtered products
        return render(request, 'cupboard.html', {'products': products, 'selected_city': selected_city})


from django.shortcuts import render, redirect
from eco.models import Product, Order
from django.contrib import messages

@login_required(login_url='login')
def checkout(request, product_id):
    product = Product.objects.get(id=product_id)

    if request.method == 'POST':
        address = request.POST['address']
        phone_number = request.POST['phone_number']
        email = request.POST['email']

        # Create an order
        order = Order.objects.create(
            customer=request.user.customer,
            product=product,
            address=address,
            phone_number=phone_number,
            email=email
        )
        messages.success(request, 'Order placed successfully!')
        return redirect('order_summary', order_id=order.id)

    return render(request, 'checkout.html', {'product': product})

# def order_summary(request, order_id):
#     order = Order.objects.get(id=order_id)
#     return render(request, 'order_summary.html', {'order': order})
from django.utils.timezone import now, localtime

@login_required(login_url='login')
def order_summary(request, order_id):
    order = Order.objects.get(id=order_id)
    order_local_time = localtime(order.order_date)  # Ensure local time is passed
    context = {
        'order': order,
        'current_time': localtime(now()),  # Pass current local time to JavaScript
    } 
    return render(request, 'order_summary.html', context)


from django.shortcuts import get_object_or_404, redirect
from django.http import JsonResponse
from .models import Order

# views.py
# def shop_products(request, slug):
#     shop = get_object_or_404(Shopkeeper)
#     products = shop.products.all()
#     context = {
#         "shop": shop,
#         "products": products,
#     }
#     return render(request, "shop_products.html", context)
from django.shortcuts import render, get_object_or_404
from .models import Shopkeeper

def shop_products(request, shop_name, city):
    # Use shop_name and city to filter the Shopkeeper
    shop = get_object_or_404(Shopkeeper, shop_name=shop_name, city=city)
    # Fetch products related to the shop
    products = shop.product_set.all()  # product_set is the default related name for a ForeignKey
    category_slug = request.GET.get('category')  # Get category from query params (if provided)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)  # Filter products by category
    # Pass the shop and products to the context
    context = {
        "shop": shop,
        "products": products,
    }

    return render(request, "shop_products.html", context)

# from django.shortcuts import render, get_object_or_404
# from .models import Shopkeeper, Product, Category

# def shop_products(request, shop_name, city):
#     # Get the shopkeeper based on the shop name and city
#     shop = get_object_or_404(Shopkeeper, shop_name=shop_name, city=city)
    
#     # Fetch all products related to this shop
#     products = Product.objects.filter(shopkeeper=shop)
    
#     # If a category is provided (for filtering)
#     category_slug = request.GET.get('category')  # Get category from query params (if provided)
#     if category_slug:
#         category = get_object_or_404(Category, slug=category_slug)
#         products = products.filter(category=category)  # Filter products by category
    
#     context = {
#         "shop": shop,
#         "products": products,
#     }
    
#     return render(request, "shop_products.html", context)


from django.shortcuts import get_object_or_404, redirect
from .models import Order

@login_required(login_url='login')
def delete_order(request, order_id):
    order = get_object_or_404(Order, id=order_id)

    # You can add additional checks if needed, like confirming the user is the one who made the order.
    order.delete()

    return redirect('home')  # Redirect to the orders page after deletion



def process_payment(request, order_id):
    order = Order.objects.get(id=order_id)
    order.is_paid = True  # Update status to paid
    order.save()
    messages.success(request, 'Payment successful!')
    return redirect('order_summary', order_id=order.id)

from django.utils import timezone
from datetime import timedelta  # Add this import

def customer_orders(request):
    orders = Order.objects.filter(customer=request.user.customer)
    # Adjust order_date by adding 5 hours 30 minutes (if necessary)
    for order in orders:
        order.order_date = order.order_date + timedelta(hours=5, minutes=30)
    return render(request, 'customer_orders.html', {'orders': orders})

def shopkeeper_orders(request):
    shopkeeper = request.user.shopkeeper
    orders = Order.objects.filter(product__shopkeeper=shopkeeper)
    return render(request, 'shopkeeper_orders.html', {'orders': orders})
