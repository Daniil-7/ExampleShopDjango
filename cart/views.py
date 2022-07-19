from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect


from account.models import User
from cart.models import Order, ProductsInOrder
from catalog.models import Product


import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from contacts.models import SendMailContacts
from diplom_django_netology import configure


from cloudipsp import Api, Checkout


def add_to_cart(request):
    path = request.GET.get("next")
    if request.method == "POST":
        product_id = request.GET.get("product_id")
        if "cart" not in request.session:
            request.session["cart"] = {}
        cart = request.session.get("cart")
        if product_id in cart:
            cart[product_id]["quantity"] += 1
        else:
            cart[product_id] = {"quantity": 1}
    request.session.modified = True
    return redirect(path)


def del_to_cart(request):
    if request.method == "POST":
        product_id = request.GET.get("product_id")
        cart = request.session.get("cart")
        val_del = True
        if cart[product_id]["quantity"] > 1:
            val_del = False
            cart[product_id]["quantity"] -= 1
        if cart[product_id]["quantity"] == 1 and val_del:
            del cart[product_id]
    request.session.modified = True
    return redirect("/cart/")


def sendOneMail(titleProduct, toaddr):
    info = "Нехватка товара: " + titleProduct
    text_info = ". Есть спрос на товар которого нет. Возможно вы не указали наличине его в админ панели."
    msg = MIMEMultipart()
    msg["From"] = configure.SERVER_EMAIL
    msg["To"] = toaddr
    msg["Subject"] = info
    body = info + "\n\n" + info + text_info
    msg.attach(MIMEText(body, "plain"))
    server = smtplib.SMTP(configure.EMAIL_HOST, configure.EMAIL_PORT)
    server.ehlo()
    server.starttls()
    server.login(configure.SERVER_EMAIL, configure.EMAIL_HOST_PASSWORD)
    text = msg.as_string()
    server.sendmail(configure.SERVER_EMAIL, toaddr, text)
    server.quit()


def sendMail(titleProduct):
    allMail = SendMailContacts.objects.all()
    for i in allMail:
        sendOneMail(titleProduct, i.email)
    sendOneMail(titleProduct, toaddr)


def notify_product_cart(request):
    path = request.GET.get("next")
    if request.method == "POST":
        product_title = request.GET.get("product_title")
        sendMail(product_title)

    return redirect(path)


def saleOneFun(object_list):
    object_list["valsale"] = False
    if object_list["sale"] != 1.0:
        object_list["valsale"] = True
        object_list["saleprice"] = object_list["price"] * object_list["sale"]
        object_list["htmlprice"] = str(100 - object_list["sale"] * 100) + "%"
    return object_list


api = Api(merchant_id=configure.cloudipsp_merchant_id, secret_key=configure.cloudipsp_secret_key)
checkout = Checkout(api=api)


def payment(cout, text):
    coutS = str(cout).split(".")
    if len(coutS[1]) == 1:
        cout = int(coutS[0] + coutS[1] + "0")
    else:
        cout = int(coutS[0] + coutS[1])
    data = {"currency": "RUB", "amount": cout, "order_desc": text}
    return checkout.url(data).get("checkout_url")


def view_cart(request):
    if request.POST.get("order_status") == "approved":
        request.session["cart"] = {}
        request.session.modified = True
        messages.success(request, "Заказ принят")
    context = {}
    cart = request.session.get("cart", None)
    if cart:
        products = {}
        product_list = Product.objects.filter(pk__in=cart.keys()).values(
            "id", "title", "description", "price", "sale"
        )

        for product in product_list:
            products[str(product["id"])] = product
        for key in cart.keys():
            cart[key]["product"] = saleOneFun(products[key])

        outPrice = 0
        outText = ""
        for p in cart:
            p = cart[p]
            outText += p["product"]["title"] + " × " + str(p["quantity"]) + "; "
            for i in range(p["quantity"]):
                if p["product"]["valsale"]:
                    outPrice += p["product"]["saleprice"]
                else:
                    outPrice += p["product"]["price"]
        context["paymentUrl"] = payment(outPrice, outText)
        context["outPrice"] = outPrice
        context["cart"] = cart
    return render(request, "cart.html", context)


@login_required(login_url="login")
def view_order(request):
    if request.method == "POST":
        user_id = request.user.pk
        customer = User.objects.get(pk=user_id)
        cart = request.session["cart"]
        if len(cart) > 0:
            order = Order.objects.create(customer=customer)
            for key, value in cart.items():
                product = Product.objects.get(pk=key)
                quantity = value["quantity"]
                ProductsInOrder.objects.create(
                    order=order, product=product, quantity=quantity
                )
            request.session["cart"] = {}
            request.session.modified = True
            messages.success(request, "Заказ принят")
    return redirect("cart:cart")
