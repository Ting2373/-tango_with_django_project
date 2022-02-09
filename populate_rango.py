import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 
'tango_with_django_project.settings')

import django
django.setup()
from rango.models import Category, Page

def populate():
    python_pages = [
        {'title': 'Official Python Tutorial',
        'url': 'http://docs.python.org/3/tutorial/',
        'views': 33},
        {'title':'How to Think like a Computer Scientist',
        'url':'http://www.greenteapress.com/thinkpython/',
        'views': 44},
        {'title':'Learn Python in 10 Minutes',
        'url':'http://www.korokithakis.net/tutorials/python/',
        'views': 55},
    ]

    django_pages = [
        {'title':'Official Django Tutorial',
        'url':'https://docs.djangoproject.com/en/2.1/intro/tutorial01/',
        'views': 66},
        {'title':'Django Rocks',
        'url':'http://www.djangorocks.com/',
        'views': 77},
        {'title':'How to Tango with Django',
        'url':'http://www.tangowithdjango.com/',
        'views': 88},
    ]

    other_pages = [
        {'title':'Bottle',
        'url':'http://bottlepy.org/docs/dev/',
        'views': 99},
        {'title':'Flask',
        'url':'http://flask.pocoo.org',
        'views': 22},
    ]

    cats = {
        'Python': {'pages': python_pages, 'views': 128, 'likes': 64},
        'Django': {'pages': django_pages, 'views': 64, 'likes': 32,},
        'Other Frameworks': {'pages': other_pages,'views': 32, 'likes': 16}
    }

    for cat, cat_data in cats.items():
        c = add_cat(cat, views=cat_data['views'], likes=cat_data['likes'])
        for p in cat_data['pages']:
            add_page(c, p['title'], p['url'], p['views'])
            
            

    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print(f'- {c}: {p}')

def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title,views=views)[0]
    p.url=url
    p.views=views
    p.save()
    return p

def add_cat(name, views, likes):
    c = Category.objects.get_or_create(name=name, views=views, likes=likes)[0]
    c.likes=likes
    c.views=views
    c.save()
    
    return c

if __name__ == '__main__':
    print('Strating Rango population script...')
    populate()