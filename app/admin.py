from django.contrib import admin
from app.models import Product, Skill, MySocialMedia, SiteConfig, FrequentlyAskedQuestion, ContactFormLog, CartFormLog

# Register your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'description',
        'weight',
        'price',
        'image',
    ]
    
@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = [
        'title',
    ]

    #nao tem permicao para adicionar
    def has_add_permission(self, request, obj = None):
        return False
    
    # #nao tem permicao para deletar
    def has_delete_permission(self, request, obj = None):
        return False

@admin.register(MySocialMedia)
class MySocialMediaAdmin(admin.ModelAdmin):
    list_display = [
        'whatsapp',
        'instagram',
    ]

    # #nao tem permicao para adicionar
    def has_add_permission(self, request, obj = None):
        return False
    
    # #nao tem permicao para deletar
    def has_delete_permission(self, request, obj = None):
        return False
    
@admin.register(SiteConfig)
class SiteConfigAdmin(admin.ModelAdmin):
    list_display = [
        'website_title',
        'website_name',
        'home_title',
        'home_description',
        'home_image',
        'website_logo',
        'about_description',
        'mission',
    ]

    # #nao tem permicao para adicionar
    def has_add_permission(self, request, obj = None):
        return False
    
    # #nao tem permicao para deletar
    def has_delete_permission(self, request, obj = None):
        return False
    
@admin.register(FrequentlyAskedQuestion)
class FrequentlyAskedQuestionAdmin(admin.ModelAdmin):
    list_display = [
        'question',
        'description',
    ]

@admin.register(ContactFormLog)
class ContactFormLogAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'is_success', 'action_time')
    list_filter = ('is_success', 'action_time')
    search_fields = ('name', 'phone_number', 'message')

    # Nao tem permisao para adicionar
    def has_add_permission(self, request, obj = None):
        return False

    # #nao tem permicao para alterar
    def has_change_permission(self, request, obj = None):
        return False
    
    # #o admin nao tem permissao para deletar
    def has_delete_permission(self, request, obj = None):
        return False

@admin.register(CartFormLog)
class CartFormLogAdmin(admin.ModelAdmin):
    list_display = ('cell', 'price', 'cart_item', 'is_success', 'action_time')
    list_filter = ('is_success', 'action_time')
    search_fields = ('cell', 'price', 'cart_Item')

    # Nao tem permisao para adicionar
    def has_add_permission(self, request, obj = None):
        return False

    # #nao tem permicao para alterar
    def has_change_permission(self, request, obj = None):
        return False
    
    # #o admin nao tem permissao para deletar
    def has_delete_permission(self, request, obj = None):
        return False



