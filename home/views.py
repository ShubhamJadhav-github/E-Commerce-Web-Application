import psycopg2
from django.http import QueryDict
from django.shortcuts import render, redirect
from .models import products, Slide, testimonial


# Create your views here.
def index(response):
    all_products = products.objects.all()  # Retrieve all products from the database
    all_slides = Slide.objects.all()
    conn = psycopg2.connect(
            database='ecommerce',
            user='postgres',
            password='1234',
            host='localhost',

        )
    cur = conn.cursor()
    sql = "select * from home_testimonial where status="+"True"
    cur.execute(sql)
    result = cur.fetchall()
    all_active_testimonials = result
    return render(response, 'index.html', {'products': all_products, 'slides': all_slides, 'testimonials': all_active_testimonials})


def register(response):
    if response.method == "POST":
        v1 = response.POST['name']
        v2 = response.POST['email']
        v3 = response.POST['password']
        v4 = response.POST['address']
        conn = psycopg2.connect(
            database='ecommerce',
            user='postgres',
            password='1234',
            host='localhost',

        )
        cur = conn.cursor()
        sql = "insert into home_user(name, email, password, address) values ('" + v1 + "', '" + v2 + "', '" + v3 + "', '" + v4 + "')"
        cur.execute(sql)
        conn.commit()
        redirect('/')
        return render(response, 'loggedin/index.html')
    else:
        return render(response, 'register.html')


def about(response):
    return render(response, 'about.html')


def products_function(response):
    return render(response, 'product.html')


def contact(response):
    return render(response, 'contact.html')


def login(response):
    return render(response, 'login.html')


def buy(response):
    if response.method == "POST":
        product_id = list(response.POST.keys())[-1]
        conn = psycopg2.connect(
            database='ecommerce',
            user='postgres',
            password='1234',
            host='localhost',

        )
        cur = conn.cursor()
        sql = "select * from home_products where id="+product_id
        cur.execute(sql)
        result = cur.fetchone()

        product = {
                'id': result[0],
                'name': result[1],
                'brand': result[2],
                'category': result[3],
                'description': result[4],
                'price': result[5],
                'availability': result[6],
                'seller_id': result[7],
                'image': result[8],
        }
        return render(response, 'buy.html', product)
    else:
        return redirect('/products')
