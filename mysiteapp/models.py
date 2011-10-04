from django.db import models
import datetime

# Create your models here.

# MainPageNote is a moduled model which allows easy additions
# to the front home page.
class MainPageNote(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return self.title
# PostType will allow the front page to show all recent updates
# across all post types (blog/wiki/tutorials)
class PostType(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    def __unicode__(self):
        return self.name
# BlogCategory will allow easy organization of the blog posts
class BlogCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    def __unicode__(self):
        return self.name
# WikiSection will allow easy organization of the main wiki sections
class WikiSection(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    def __unicode__(self):
        return self.name
# WikiSubsection will further organize the wiki db page
class WikiSubsection(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    section = models.ForeignKey(WikiSection)
    def __unicode__(self):
        return self.name
# TutorialCategory will organize the tutorial posts into categories
class TutorialCategory(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    def __unicode__(self):
        return self.name
# BlogPost represents the individual blog posts.
class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    description = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    slug = models.CharField(max_length=255)
    category = models.ForeignKey(BlogCategory)
    post_type = models.ForeignKey(PostType)
    def __unicode__(self):
        return "%s %s %s" % (self.title, self.update_date, self.slug)
# WikiPost represents the individual wiki posts
class WikiPost(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    description = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    slug = models.CharField(max_length=255)
    post_type = models.ForeignKey(PostType)
    section = models.ForeignKey(WikiSection)
    subsection = models.ForeignKey(WikiSubsection)
    def __unicode__(self):
        return "%s %s %s" % (self.title, self.update_date, self.slug)
# TutorialPost represents the individual tutorials that are posted
class TutorialPost(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    description = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    slug = models.CharField(max_length=255)
    post_type = models.ForeignKey(PostType)
    category = models.ForeignKey(TutorialCategory)
    def __unicode__(self):
        return "%s %s %s" % (self.title, self.update_date, self.slug)

