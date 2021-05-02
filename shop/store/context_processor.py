from store.models import Category,Typefile


def menu_links(request):
    links=Category.objects.all()
    return dict(links=links)

def typefile_links(request):
    tlinks=Typefile.objects.all()
    return dict(tlinks=tlinks)
