from locale import currency
from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.contrib import messages
from django.contrib.auth import get_user_model
import re
import razorpay
from django.views.decorators.csrf import csrf_exempt

def landing_page(request):
    return render(request, 'landing.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        phone_number = request.POST['phone_number']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        # Email validation
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_regex, email):
            messages.error(request, "Invalid email format")
            return redirect('register')

        phone_number = ''.join(filter(str.isdigit, phone_number))
        if len(phone_number) < 10:
            messages.error(request,"Phone number must be at least 10 digits long")
            return redirect('register')

        # Password match check
        if password != confirm_password:
            messages.error(request, "Passwords do not match")
            return redirect('register')

        if CustomUser.objects.filter(email=email).exists():
            messages.error(request, "Email already in use")
            return redirect('register')

        user = CustomUser(
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            email=email,
            password=password
        )
        user.save()
        messages.success(request, "Registration successful! Please log in.")
        return redirect('login')

    return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        try:
            user = CustomUser.objects.get(email=email, password=password)
            request.session['user_id'] = user.id
            return redirect('main')
        except CustomUser.DoesNotExist:
            messages.error(request, "Invalid email or password")
            return redirect('login')

    return render(request, 'login.html')

def profile(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')

    user = CustomUser.objects.get(id=user_id)
    return render(request, 'profile.html', {'user': user})

def main(request):
    if not request.session.get('user_id'):
        return redirect('login')
    query = request.GET.get('query')
    if query:
        products = Product.objects.filter(
            name__icontains=query
        ) | Product.objects.filter(
            category__icontains=query
        ) | Product.objects.filter(
            description__icontains=query
        )
    else:
        products = Product.objects.all()

    return render(request, 'main.html', {'products': products})

def logout_view(request):
    request.session.flush()
    return redirect('landing')

def cart(request):
    if not request.user.is_authenticated:
        return redirect('login')
    cart_items = Cart.objects.filter(user=request.user)
    return render(request, 'cart.html', {'cart_items': cart_items})

User = get_user_model()
def add_to_cart(request, product_id):
    if not request.user.is_authenticated:
        return redirect('login')
    user = User.objects.get(id=request.user.id)
    product = get_object_or_404(Product, id=product_id)
    cart_item, created = Cart.objects.get_or_create(user=user, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('main')

def remove_from_cart(request, cart_id):
    if request.user.is_authenticated:
        cart_item = get_object_or_404(Cart, id=cart_id, user=request.user)
        cart_item.delete()
        return redirect('cart')
    else:
        return redirect('login')

def wishlist(request):
    if not request.user.is_authenticated:
        return redirect('login')
    wishlist_items=Wishlist.objects.filter(user=request.user)
    return render(request,'wishlist.html',{'wishlist_items': wishlist_items})

def add_to_wishlist(request, product_id):
    if not request.user.is_authenticated:
        return redirect('login')
    user = User.objects.get(id=request.user.id)
    product = get_object_or_404(Product, id=product_id)
    wishlist_item, created = Wishlist.objects.get_or_create(user=user, product=product)
    if created:
        return redirect('wishlist')
    return redirect('main')

def remove_from_wishlist(request, wishlist_id):
    if request.user.is_authenticated:
        wishlist_item = get_object_or_404(Wishlist, id=wishlist_id, user=request.user)
        wishlist_item.delete()
        return redirect('wishlist')
    else:
        return redirect('login')

def checkout(request, product_id):
    if not request.user.is_authenticated:
        return redirect('login')
    razorpay_client = razorpay.Client(auth=('rzp_test_QtVPRK8bBQ0Uwv', 'qXATaOfZlTAnlrvhZjn0BHsa'))

    # Get the product object based on the product_id
    product = get_object_or_404(Product, id=product_id)

    # If POST request, handle order creation and Razorpay order generation
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        address = request.POST.get('address')
        phone_number = request.POST.get('phone_number')
        total_price = product.price * quantity

        if not address or not phone_number:
            return render(request, 'checkout.html', {'product': product, 'error': 'Address and Phone Number are required!'})

        # Create Razorpay order
        razorpay_order = razorpay_client.order.create({
            "amount": int(total_price * 100),  # amount in paise
            "currency": "INR",
            "payment_capture": "1"
        })

        # Create order in the database
        order = Order.objects.create(
            product=product,
            quantity=quantity,
            total_price=total_price,
            address=address,
            phone_number=phone_number,
            payment_id=razorpay_order['id'],
            user=request.user  # No user authentication in this case
        )

        # Pass data to template
        context = {
            'order': order,
            'razorpay_order_id': razorpay_order['id'],
            'razorpay_key': 'rzp_test_QtVPRK8bBQ0Uwv',
            'amount': total_price,  # Pass the amount in rupees (not in paise)
            'currency': 'INR',
            'product': product,
        }

        return render(request, 'checkout.html', context)

    return render(request, 'checkout.html', {'product': product})


@csrf_exempt
def payment_success(request):
    if request.method == "POST":
        payment_id = request.POST.get('razorpay_payment_id')
        order_id = request.POST.get('razorpay_order_id')
        order = Order.objects.get(payment_id=order_id)
        order.payment_status = 'Completed'
        order.save()
        messages.success(request, "Payment successful! Your order has been placed.")
        return redirect('orders')

    return redirect('main')


def orders(request):
    orders = Order.objects.filter(user=request.user).order_by('-ordered_at')
    return render(request, 'orders.html', {'orders': orders})