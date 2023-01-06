from queue import Empty
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category, Comment
from .forms import PostForm, EditForm, CommentForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect


#comment alohida page dan yuboriladi
class AddComment(CreateView):
    model = Comment
    form_class = CommentForm
    #fields = '__all__'
    template_name = 'add_comment.html'
    #success_url = reverse_lazy('home')
    
    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super(AddComment, self).form_valid(form)
    
    def get_success_url(self, **kwargs):
            pk = self.kwargs["pk"]
            return reverse( "article-detail", kwargs={'pk': pk})
    

def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user) 
        liked = True
    return HttpResponseRedirect(reverse('article-detail', args=[str(pk)]))


class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-post_date']

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            object_list = self.model.objects.filter(Q(title__contains=query) | Q(snippet__contains=query))
            if not object_list.exists():
                object_list = 'empty list'
        else:
            object_list = self.model.objects.none()
        return object_list

    def get_context_data(self, *args, object_list=None, **kwargs):
        cat_menu = Category.objects.all()
        recent_posts = Post.objects.all().order_by('-post_date')[:20]
        context = super(HomeView, self).get_context_data(*args, **kwargs)
    
        context['cat_menu'] = cat_menu
        context['recent_posts'] = recent_posts
        return context


def CategoryListView(requests):
    cat_menu_list = Category.objects.all()
    return render(requests, 'category_list.html',
                  {'cat_menu_list': cat_menu_list})


def CategoryView(requests, cats):
    # category ga tegishli bolgan postlar
    category_posts = Post.objects.filter(category__contains=cats.replace('-', ' ')).order_by('-post_date')

    return render(requests, 'categories.html',
                  {'cats': cats.title().replace('-', ' '),
                   'category_posts': category_posts
                   })


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)
        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        #stuff = Post.objects.get(id=kwargs['pk'])
        total_likes = stuff.total_likes()

        liked=False
        # user like bosganmi yoqmi aniqlaymiz
        if stuff.likes.filter(id=self.request.user.id).exists(): #self boladi  chunki metod ichidamiz
            liked = True

        context['cat_menu']=cat_menu
        context['total_likes'] = total_likes
        context['liked']=liked
        return context


class AddPostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'


# Category view
class AddCatView(CreateView):
    model = Category
    #form_class = CategoryForm
    template_name = 'add_category.html'
    fields = '__all__'


class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'
    #fields = ['title', 'title_tag', 'body']

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')
