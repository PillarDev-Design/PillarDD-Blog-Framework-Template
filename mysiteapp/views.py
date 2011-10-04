# Create your views here.
import models, forms
from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.core.mail import send_mail, EmailMessage
from django.core.context_processors import csrf
from django.template import RequestContext
from forms import ContactForm


def home(request):
    mainpagenotes = models.MainPageNote.objects.all().order_by('-pub_date')[:5]
    posttype = models.PostType.objects.all()
    blogs = models.BlogPost.objects.all().order_by('-pub_date')[:1]
    wikis = models.WikiPost.objects.all().order_by('-update_date')[:1]
    tutorials = models.TutorialPost.objects.all().order_by('-pub_date')[:1]
    response_dict = {'mainpagenotes':mainpagenotes, 'posttype':posttype,
            'blogs':blogs, 'wikis':wikis, 'tutorials':tutorials}
    return render_to_response('mysiteapp/home.html', response_dict)

def blogdir(request):
    blogs = models.BlogPost.objects.all().order_by('pub_date')
    categories = models.BlogCategory.objects.all()
    blogsides = models.BlogPost.objects.all().order_by('-pub_date')[:5]
    response_dict = {'blogs':blogs, 'categories':categories, 'blogsides':blogsides}
    return render_to_response('mysiteapp/blogdirectory.html', response_dict)

def blogsearch(request):
    blogsides = models.BlogPost.objects.all().order_by('-pub_date')[:5]
    error = False
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            error = True
            response_dict = {'blogsides':blogsides, 'error':error, 'query':q}
        else:
            blogs = models.BlogPost.objects.filter(title__icontains=q)
            response_dict = {'blogsides':blogsides, 'blogs':blogs, 'query':q}
    return render_to_response('mysiteapp/blogsearch.html', response_dict)

def wikidir(request):
    wikis = models.WikiPost.objects.all().order_by('update_date')
    section = models.WikiSection.objects.all()
    subsection = models.WikiSubsection.objects.all()
    wikisides = models.WikiPost.objects.all().order_by('-update_date')[:5]
    response_dict = {'wikis':wikis, 'section':section,
            'subsection':subsection, 'wikisides':wikisides}
    return render_to_response('mysiteapp/wikidirectory.html', response_dict)

def wikisearch(request):
    wikisides = models.WikiPost.objects.all().order_by('-pub_date')[:5]
    error = False
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            error = True
            response_dict = {'wikisides':wikisides, 'error':error, 'query':q}
        else:
            wikis = models.WikiPost.objects.filter(title__icontains=q)
            response_dict = {'wikisides':wikisides, 'wikis':wikis, 'query':q}
    return render_to_response('mysiteapp/wikisearch.html', response_dict)

def tutorialdir(request):
    tutorials = models.TutorialPost.objects.all().order_by('pub_date')
    categories = models.TutorialCategory.objects.all()
    tutorialside = models.TutorialPost.objects.all().order_by('-pub_date')[:5]
    response_dict = {'tutorials':tutorials,'categories':categories,
            'tutorialside':tutorialside}
    return render_to_response('mysiteapp/tutorialdirectory.html', response_dict)

def tutorialsearch(request):
    tutorialsides = models.TutorialPost.objects.all().order_by('-pub_date')[:5]
    error = False
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            error = True
            response_dict = {'tutorialsides':tutorialsides, 'error':error, 'query':q}
        else:
            tutorials = models.TutorialPost.objects.filter(title__icontains=q)
            response_dict = {'tutorialsides':tutorialsides,
                    'tutorials':tutorials, 'query':q}
    return render_to_response('mysiteapp/tutorialsearch.html', response_dict)

def about(request):
    c = {}
    c.update(csrf(request))
    errors = []
    success = False
    if request.method == "POST":
        if not request.POST.get('subject', ''):
            errors.append('Enter a subject.')
        if not request.POST.get('message', ''):
            errors.append('Enter a message.')
        if request.POST.get('e_mail') and '@' not in request.POST['e_mail']:
            errors.append('Enter a valid e-mail address.')
        if not errors:
            sub = request.POST.get('subject')
            mes = request.POST.get('message')
            ema = request.POST.get('e_mail')
            email = EmailMessage(sub, mes + ' Email: ' + ema, to=['cnabors.sithlord@gmail.com'])
            email.send()
            success = True
            response_dict = {'success':success}
            return render_to_response('mysiteapp/about.html', response_dict,
                context_instance=RequestContext(request))
    response_dict = {'errors':errors}
    return render_to_response('mysiteapp/about.html', response_dict,
            context_instance=RequestContext(request))

def editrequest(request, target_slug):
    errors = []
    success = False
    wiki = models.WikiPost.objects.get(slug=target_slug)
    subsection = models.WikiSubsection.objects.all()
    if request.method == "POST":
        if not request.POST.get('message', ''):
            errors.append('Enter a message.')
        if request.POST.get('e_mail') and '@' not in request.POST['e_mail']:
            errors.append('Enter a valid e-mail address.')
        if not errors:
            sub = target_slug
            mes = request.POST.get('message')
            ema = request.POST.get('e_mail')
            email = EmailMessage(sub, mes + ' Email: ' + ema, to=['cnabors.sithlord@gmail.com'])
            email.send()
            success = True
            response_dict = {'success':success, 'wiki':wiki,
                    'subsection':subsection}
            return render_to_response('mysiteapp/editrequest.html',
                    response_dict, context_instance=RequestContext(request))
    response_dict = {'errors':errors, 'wiki':wiki, 'subsection':subsection}
    return render_to_response('mysiteapp/editrequest.html', response_dict,
            context_instance=RequestContext(request))
    

def get_blog(request, target_slug):
    blog = models.BlogPost.objects.get(slug=target_slug)
    categories = models.BlogCategory.objects.all()
    blogside = models.BlogPost.objects.all().order_by('-pub_date')
    response_dict = {'blog':blog, 'blogside':blogside}
    return render_to_response('mysiteapp/blogpost.html', response_dict)

def get_wiki(request, target_slug):
    wiki = models.WikiPost.objects.get(slug=target_slug)
    subsection = models.WikiSubsection.objects.all()
    response_dict = {'wiki':wiki, 'subsection':subsection}
    return render_to_response('mysiteapp/wikipost.html', response_dict)

def wikiedit(request, target_slug):
    wiki = models.WikiPost.objects.get(slug=target_slug)
    subsection = models.WikiSubsection.objects.all()

    response_dict = {'wiki':wiki, 'subsection':subsection}
    return render_to_response('mysiteapp/editrequest.html', response_dict)

def get_tutorial(request, target_slug):
    tutorial = models.TutorialPost.objects.get(slug=target_slug)
    categories = models.TutorialCategory.objects.all()
    tutorialside = models.TutorialPost.objects.all().order_by('-pub_date')
    response_dict = {'tutorial':tutorial, 'tutorialside':tutorialside}
    return render_to_response('mysiteapp/tutorialpost.html', response_dict)


