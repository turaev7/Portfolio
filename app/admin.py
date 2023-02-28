from django.contrib import admin
from .models import *
# Register your models here.


class MeAdmin(admin.ModelAdmin):
    list_display = ['name','surname','phone', 'email']
    list_per_page = 10
    search_fields = ['name','surname','phone', 'email']
    class Meta:
        model = Me
admin.site.register(Me, MeAdmin)



class PortfolioAdmin(admin.ModelAdmin):
    list_display = ['p_name','p_date']
    list_per_page = 10
    search_fields = ['p_name','p_date']
    class Meta:
        model = Portfolio
admin.site.register(Portfolio, PortfolioAdmin)





class TotalAdmin(admin.ModelAdmin):
    list_display = ['works','month_experience','total_clients','awards']
    list_per_page = 10
    search_fields = ['works','month_experience','total_clients','awards']
    class Meta:
        model = Total
admin.site.register(Total, TotalAdmin)


class BlogAdmin(admin.ModelAdmin):
    list_display = ['blog_name']
    list_per_page = 10
    search_fields = ['blog_name']
    class Meta:
        model = Blog
admin.site.register(Blog, BlogAdmin)







