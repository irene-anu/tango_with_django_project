import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')

import django
django.setup()

from rango.models import Category, Page  # Import the models you need

def populate():
    # First, we will create lists of dictionaries containing the pages
    # we want to add into each category.
    # Then we will create a dictionary of dictionaries for our categories.

    python_pages = [
        {"title": "Official Python Tutorial", "url":"http://docs.python.org/3/tutorial/", "views": 80},
        {"title":"How to Think like a Computer Scientist", "url":"http://www.greenteapress.com/thinkpython/","views": 50},
        {"title":"Learn Python in 10 Minutes", "url":"http://www.korokithakis.net/tutorials/python/","views": 860}]

    django_pages = [
        {"title":"Official Django Tutorial", "url":"https://docs.djangoproject.com/en/2.1/intro/tutorial01/", "views": 820},
        {"title":"Django Rocks", "url":"http://www.djangorocks.com/", "views": 680},
        {"title":"How to Tango with Django", "url":"http://www.tangowithdjango.com/", "views": 980}]

    other_pages = [
        {"title":"Bottle", "url":"http://bottlepy.org/docs/dev/","views": 83},
        {"title":"Flask", "url":"http://flask.pocoo.org","views": 813}]

    cats = {"Python": {"pages": python_pages, "views": 128, "likes": 64},
            "Django": {"pages": django_pages, "views": 64,"likes": 32},
            "Other Frameworks": {"pages": other_pages, "views": 32, "likes": 16}}

    # If you want to add more categories or pages,
    # add them to the dictionaries above.

    # The code below goes through the cats dictionary, then adds each category,
    # and then adds all the associated pages for that category.
    for cat, cat_data in cats.items():
        c = add_cat(cat,cat_data["views"],cat_data["likes"])
        for p in cat_data["pages"]:
            add_page(c, p["title"], p["url"],p["views"])

    # Print out the categories we have added.
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print(f"- {c}: {p}")

def add_page(cat, title, url, views):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url=url
    p.views=views
    p.save()
    return p

def add_cat(name, views =0, likes = 0):
    c = Category.objects.get_or_create(name=name)[0]
    c.views = views
    c.likes = likes
    c.save()
    return c

# Start execution here!
if __name__ == '__main__':     #Importing the module will not run this code; any classes or functions will however be fully accessible to you.
    print("Starting Rango population script...")
    populate()
