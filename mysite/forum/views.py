import sys
from django.shortcuts import render
from django.utils import timezone
from .models import Post, Autor

def index_view(request):
    ''' View for list of all topics '''
    all_posts = Post.objects.all()
    all_people = Autor.objects.all()

    try:
        form_nickname = request.POST['submit_nickname']
        form_text = request.POST['submit_text']
    except KeyError:
        print('KeyError appeared')
    else:
        if not Autor.objects.filter(pk=form_nickname):
            Autor.objects.create(pk=form_nickname)
        post_autor = Autor.objects.get(pk=form_nickname)
        post_autor.post_set.create(post_text=form_text, post_date=timezone.now())

    return render(request, 'forum/index.html',
                  context={'all_posts': all_posts, 'all_people': all_people})
