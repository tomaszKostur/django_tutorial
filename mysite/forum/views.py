import sys
from django.shortcuts import render
from django.utils import timezone
from .models import Post, Autor

def index_view(request):
    ''' View for list of all topics '''
    all_posts = Post.objects.all()
    all_people = Autor.objects.all()
    try:
        new_post = Post(post_date=timezone.now(),
                        post_text=request.POST['submit_text'])
        new_post.save()
    except:
        print("looks like some unexpected error", sys.exc_info()[0])

    return render(request, 'forum/index.html',
                  context={'all_posts': all_posts, 'all_people': all_people})
