from store.models import Category,Typefile,Published


def menu_links(request):
    links=Category.objects.all()
    return dict(links=links)

def typefile_links(request):
    tlinks=Typefile.objects.all()
    return dict(tlinks=tlinks)

def published_links(request):
    plinks=Published.objects.all()
    return dict(plinks=plinks)
