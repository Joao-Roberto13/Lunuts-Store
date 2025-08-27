from django.conf import settings
from django.utils import timezone
from django.contrib import messages
from django.core.mail import send_mail
from babel.numbers import format_currency
from django.template.loader import render_to_string
from django.shortcuts import render, redirect, get_object_or_404
from app.models import SiteConfig, Product, MySocialMedia, FrequentlyAskedQuestion, Skill, CartItem, ContactFormLog, CartFormLog


# Create your views here.
def index(request):
    #Sessao para o carrinho
    session_key = _get_session_key(request)
    cart_items = CartItem.objects.filter(session_key=session_key)
    total = sum(item.subtotal() for item in cart_items)
    total = formatarMoeda(total)

    siteConfig = SiteConfig.objects.first()
    product = Product.objects.all()
    socialMedia = MySocialMedia.objects.first()
    faq = FrequentlyAskedQuestion.objects.all()
    skill = Skill.objects.all()
    
    # Divide as tecnologias por vírgula e salva como uma nova variável em cada projeto
    for sk in skill:
        sk.skill_list = [tool.strip() for tool in sk.title.split(",")]

    context = {
        "siteConfig":siteConfig,
        "product":product,
        "socialMedia":socialMedia,
        "faqs":faq,
        "skill":skill,
        "cart_items": cart_items,
        "total": total
    }

    return render(request, "index.html", context)

#############################
#    Carrinho de Compras    #
#############################
def _get_session_key(request):
    if not request.session.session_key:
        request.session.create()
    return request.session.session_key

def add_to_cart(request, product_id):
    if request.method == "POST":
        product = get_object_or_404(Product, id=product_id)
        session_key = _get_session_key(request)

        quantity = int(request.POST.get("quantity"))
        product_type = request.POST.get("product_type")
        weight = product.weight  

        # Se já existe esse produto com o mesmo tipo → soma quantidade
        cart_item, created = CartItem.objects.get_or_create(
            session_key=session_key,
            product=product,
            product_type=product_type,
        )
        if not created:
            cart_item.quantity += quantity
        else:
            cart_item.quantity = quantity
        cart_item.save()

    return redirect("/#products")

def remove_from_cart(request, cart_item_id):
    if request.method == "POST":
        cart_item = get_object_or_404(CartItem, id=cart_item_id)
        cart_item.delete()
    return redirect("home")

#######################
##   Contact Form    ##
#######################
def contact_form(request):
    if request.method == 'POST':
        print("\n\n  Utilizizador submeteu um formulário. \n\n")
        name = request.POST.get('name')
        phone_number = request.POST.get('phone')
        message = request.POST.get('message')

        context = {
            "name": name,
            "phone_number":phone_number,
            "message": message,
        }

        html_content = render_to_string('email.html', context)
        
        is_success = False
        error_message = ""

        try:
            send_mail(
                message=None, # se ntiver irá dar erro. agora usamos o email.html para mandar com a estrutura e style
                subject="LuNuts",
                html_message=html_content,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[settings.EMAIL_HOST_USER],
                fail_silently=False, #.default is True
            )
        except Exception as e:
            error_message = str(e)
            messages.error(request, "Ocorreu um erro, não foi possível enviar email")
        else:
            is_success = True
            messages.success(request, "Email enviado com sucesso")

        ContactFormLog.objects.create(
            name=name,
            phone_number=phone_number,
            message=message,
            action_time=timezone.now(),
            is_success=is_success,
            error_message=error_message
        )

    return redirect('/#contact')

###############################
##     Cart Form Checkout    ##
###############################
def cart_form(request):
    if request.method == 'POST':
        print("\n\n  Utilizador fez checkout do seu Cart. \n\n")
        cell = request.POST.get('cell')
        price = request.POST.get('price')        

        # Pega a sessão atual
        session_key = _get_session_key(request)
        cart_items = CartItem.objects.filter(session_key=session_key)

        # Monta o contexto para o template do email
        context = {
            "cell": cell,
            "price": price,
            "cart_items": cart_items,  # envia a queryset de objetos CartItem
        }

        # Renderiza o template HTML do email
        html_content = render_to_string('email_Cart.html', context)
        
        is_success = False
        error_message = ""

        try:
            if cart_items:
                send_mail(
                    message=None,  # usamos html_message
                    subject="LuNuts Cart",
                    html_message=html_content,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[settings.EMAIL_HOST_USER],
                    fail_silently=False,
                )

                cart_items.delete() # deleta os items, pois ja fez a encomenda
            else:
                raise Exception ("Sem itens no Carrinho")

        except Exception as e:
            error_message = str(e)
            messages.error(request, f"Ocorreu um erro, não foi possível fazer a encomenda: {e}")
        else:
            is_success = True
            messages.success(request, "Encomenda enviada com sucesso")

        # Salva o log do checkout
        CartFormLog.objects.create(
            cell=cell,
            price=price,
            cart_item=", ".join([
                f"{item.quantity}x {item.product.title} ({item.product.weight} - {item.product_type})"
                for item in cart_items
            ]),
            action_time=timezone.now(),
            is_success=is_success,
            error_message=error_message
        )

        # Limpa o carrinho após checkout
        cart_items.delete()

    return redirect('home')

def formatarMoeda(valor):
    return format_currency(valor, "MZN", locale="pt_MZ")






