from django.contrib import admin
from .models import Categorys, CarAbout

# admin.site.register(Categorys)
# admin.site.register(CarAbout)



@admin.register(CarAbout)
class CarAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('model', 'name')
    list_filter = ('model',)

@admin.register(Categorys)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)



# Register your models here.
