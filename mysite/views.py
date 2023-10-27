from django.shortcuts import render
from mysite.models import Post, Book
from datetime import datetime
from django.shortcuts import redirect

def homepage(request):
    books = Book.objects.all()
    now = datetime.now()
    return render(request, 'index.html', locals())

def showpost(request, slug):
    try:
        post = Post.objects.get(slug=slug)
        if post:
            return render(request, 'post.html', locals())
        else:
            return redirect("/")
    except:
        return redirect("/")

def showbook(request, img_and_con):
    try:
        book = Post.objects.get(img_and_con=img_and_con)
        if book:
                return render(request, 'book.html', locals())
        else:
            return redirect("/")
    except:
        return redirect("/")


    #select* from post where slug = %slug
    return render(request, 'post.html', locals())



'''
def homepage(request):
    posts = Post.objects.all()
    post_lists = list()
    for count,post in enumerate(posts):
        post_lists.append(f'No. {count} - {post} <br>')
        return HttpResponse(post_lists)
'''
