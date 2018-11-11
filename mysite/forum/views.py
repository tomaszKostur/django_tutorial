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
        post_autor.post_set.create(post_text=form_text,
                                   post_date=timezone.now())

    for pk in Post.objects.values_list('pk', flat=True):
        try:
            print('delete_{}'.format(pk))
            if request.POST['delete_{}'.format(pk)]:
                Post.objects.get(pk=pk).delete()

        except KeyError:
            print('Key Error DELETE button')

    return render(request, 'forum/index.html',
                  context={'all_posts': all_posts, 'all_people': all_people})
