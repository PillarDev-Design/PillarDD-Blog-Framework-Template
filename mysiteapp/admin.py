# Import models
from mysiteapp.models import MainPageNote
from mysiteapp.models import BlogPost
from mysiteapp.models import WikiPost
from mysiteapp.models import TutorialPost
from mysiteapp.models import PostType
from mysiteapp.models import BlogCategory
from mysiteapp.models import WikiSection
from mysiteapp.models import WikiSubsection
from mysiteapp.models import TutorialCategory
from django.contrib import admin

class BlogPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'pub_date', 'update_date')
    search_fields = ('title',)
    list_filter = ('pub_date',)
    date_hierarchy = 'pub_date'
    fields = ('title', 'content', 'description', 'slug', 'category', 'post_type')

# Register models
admin.site.register(MainPageNote)
admin.site.register(BlogPost, BlogPostAdmin)
admin.site.register(WikiPost)
admin.site.register(TutorialPost)
admin.site.register(PostType)
admin.site.register(BlogCategory)
admin.site.register(WikiSection)
admin.site.register(WikiSubsection)
admin.site.register(TutorialCategory)
