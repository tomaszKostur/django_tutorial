from django.shortcuts import render
from django.utils import timezone
from .models import Post, Autor
import logging


logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger('forum_views')

def index_view(request):
    return render(request, 'forum/index.html',
                  context={})

def topic_view(request, topic_name):
    ''' View for list of all topics '''
    log.debug('request: %s', request)

    topic_posts = Post.objects.filter(topic=topic_name)
    all_people = Autor.objects.all()

    try:
        form_nickname = request.POST['submit_nickname']
        form_text = request.POST['submit_text']
    except KeyError:
        log.debug('KeyError appeared')
    else:
        if not Autor.objects.filter(pk=form_nickname):
            Autor.objects.create(pk=form_nickname)
        post_autor = Autor.objects.get(pk=form_nickname)
        post_autor.post_set.create(topic=topic_name,
                                   post_text=form_text,
                                   post_date=timezone.now())

    for pk in Post.objects.values_list('pk', flat=True):
        try:
            log.debug('delete_%d', pk)
            if request.POST['delete_{}'.format(pk)]:
                Post.objects.get(pk=pk).delete()

        except KeyError:
            log.debug('Key Error DELETE button')

    return render(request, 'forum/topic.html',
                  context={'topic': topic_name,
                           'topic_posts': topic_posts, 'all_people': all_people})
