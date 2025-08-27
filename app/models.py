from django.db import models
from django.templatetags.static import static

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=55, default="")
    description = models.CharField(max_length=255, default="")
    weight = models.CharField(max_length=5, default="")
    price = models.DecimalField(max_digits=10, decimal_places=1)  # Melhor que IntegerField p/ preços
    image = models.ImageField(upload_to="static/img/products/", blank=True, null=True)

    def __str__(self):
        return self.title

class Skill(models.Model):
    title = models.CharField(max_length=80, default="")  

    def __str__(self):
        return "Skills"

class MySocialMedia(models.Model):
    whatsapp = models.URLField(max_length=40, default="")
    instagram = models.URLField(max_length=70, default="")

    def __str__(self):
        return "Social Media" 

class SiteConfig(models.Model):   
    website_logo =  models.ImageField(upload_to="static/img/logo/", blank=True, null=True, default=("static/img/logo.png"))
    website_title =  models.CharField(max_length=32, default = "LUNUTS - Castanhas de Caju")
    website_name =  models.CharField(max_length=15, default = "LuNuts")
    home_title = models.CharField(max_length=55, default = "Frescas, deliciosas e direto de Manjacaze")
    home_description = models.CharField(max_length=255, default = "Sabor autêntico, selecionado à mão, com foco em qualidade, tradição e sustentabilidade.")
    home_image = models.ImageField(upload_to="static/img/home/", blank=True, null=True)
    about_description = models.TextField(max_length=255, default="Nascida em Manjacaze, a LUNUTS dedica-se à seleção e transformação de castanha de caju com rigor e carinho. Trabalhamos com produtores locais, valorizando o saber tradicional e promovendo práticas que respeitam o ambiente.")
    mission = models.TextField(max_length=255, default="Levar o melhor sabor de Manjacaze a todo o país, criando impacto social positivo e rendimentos justos para as comunidades locais.")

    #vision = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.website_name
    
    @property
    def home_image_url(self):
        if self.home_image:
            return self.home_image.url
        return static("static/img/home.png")  # fallback padrão: um valor substituto para ser usado no caso da opção ser null

class FrequentlyAskedQuestion(models.Model):
    question = models.CharField(max_length=32, default = "")
    description = models.CharField(max_length=255, default = "")

    def __str__(self):
        return self.question

class CartItem(models.Model):
    session_key = models.CharField(max_length=40)  # sem user
    product = models.ForeignKey(Product, on_delete=models.CASCADE) # se usar a chave como FK e deletar o pai, todos os obectos são deletados...
    product_type = models.CharField(max_length=10, default="Normal")
    weight = models.CharField(max_length=8, default="")
    quantity = models.PositiveIntegerField(default=1)

    def subtotal(self):
        return self.product.price * self.quantity

    def __str__(self):
        return self.session_key

class ContactFormLog(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    message = models.TextField()
    action_time = models.DateTimeField(null=True, blank=True)
    is_success = models.BooleanField(default=False)
    error_message = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class CartFormLog(models.Model):
    cell = models.CharField(max_length=15)
    price = models.CharField(max_length=8)
    cart_item = models.TextField()
    action_time = models.DateTimeField(null=True, blank=True)
    is_success = models.BooleanField(default=False)
    error_message = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.cell
    
