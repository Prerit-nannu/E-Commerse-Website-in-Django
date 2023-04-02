from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.db.models import Max, Min

from Website.models import Slider, banner, Main_Category, Product, Category, Order
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages

from django.contrib.auth.decorators import login_required
from cart.cart import Cart

def BASE(request):
    return render(request, 'base.html')

def HOME(request):
    sliders = Slider.objects.all().order_by('-id')[0:3]
    banners = banner.objects.all().order_by('-id')[0:3]
    main_category = Main_Category.objects.all()
    product = Product.objects.filter(section__name = "Top Deal of the Day" )

    context = {
        'sliders':sliders,
        'banners':banners,
        'main_category':main_category,
        'product':product,
    }
    return render(request, 'home.html',context)


def PRODUCT_DETAILS(request,slug):
    product = Product.objects.get(slug = slug)

    context ={
        'product':product,
    }
    return render(request,"product/product_detail.html",context)


def MY_ACCOUNT(request):
    return render(request, 'account/my-account.html')


def REGISTER(request):
    if request.method =="POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'User Already Exists')
            return redirect('my_account')

        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email Already Exists')
            return redirect('my_account')

        user = User(
            username=username,
            email=email,
        )

        user.set_password(password)
        user.save()
        return redirect('my_account')

    return render(request, "account\my-account.html")


def LOGIN(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,'Email and Password are invalid !')
            return redirect('my_account')

    return render(request, "account\my-account.html")

def logout(request):
    request.session.clear()
    return redirect('home')

def PROFILE(request):
    return render(request, 'profile\profile.html')


def PRODUCT(request):
    category = Category.objects.all()
    product = Product.objects.all()

    # filter by price
    min_price = Product.objects.all().aggregate(Min('price'))
    max_price = Product.objects.all().aggregate(Max('price'))

    FilterPrice = request.GET.get('FilterPrice')
    if FilterPrice:
        Int_FilterPrice = int(FilterPrice)
        product = Product.objects.filter(price__lte=Int_FilterPrice)
    else:
        product = Product.objects.all()

    context = {
        'category':category,
        'product':product,
        'min_price':min_price,
        'max_price':max_price,
        'FilterPrice': FilterPrice,
    }
    return render(request, 'product\product.html',context)

def filter_data(request):
    categories = request.GET.getlist('category[]')
    brands = request.GET.getlist('brand[]')

    allProducts = Product.objects.all().order_by('-id').distinct()
    if len(categories) > 0:
        allProducts1 = allProducts.filter(Categories__id__in=categories).distinct()

    if len(brands) > 0:
        allProducts1 = allProducts.filter(Brand__id__in=brands).distinct()

    t = render_to_string('ajax/product.html', {'product': allProducts})

    return JsonResponse({'data': t})

# For Card Details

def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


def cart_detail(request):
    return render(request, 'account\cart.html')


def CHECKOUT(request):
    if request.method == "POST":
        user = request.session.get('User')
        cart = request.session.get('cart')
        products = Product.get_products_by_id(list(cart.keys()))
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        print(user, products, address, phone, email)
        for product in products:
            print(cart.get(str(product.id)))
            order = Order(
                          product=product,
                          user=User.id,
                          price = product.price,
            )

            order.placeOrder()
        request.session['cart'] = {}

        return render(request, 'account\checkout.html')
    else:
        return render(request, 'account\order.html')


def ORDER(request):
    if request.method == "POST":
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        cart = request.session.get('cart')
        products = Product.get_products_by_id(list(cart.keys()))


        return render(request, 'account\order.html')

    if request.method == "GET":
        #orders = Order.get_orders_by_user(User)
        #print(orders)
        return render(request, 'account\order.html')


def ERROR(request):
    return render(request, 'account\Page_Not_Found.html')
