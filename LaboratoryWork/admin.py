from django.contrib import admin

from .models import Article, Review, LaboratoryWork, LaboratoryStand

class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published')
    list_display_links = ('title', 'author')


admin.site.register(Article, ArticleAdmin)
admin.site.register(Review)
admin.site.register(LaboratoryWork)
admin.site.register(LaboratoryStand)