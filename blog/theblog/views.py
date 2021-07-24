from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView, DetailView,CreateView,UpdateView,DeleteView
from .models import Post,Category
from django.urls import reverse,reverse_lazy
from .forms import PostForm
from django.http import HttpResponseRedirect
# Create your views here.
class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    fields='__all__'
    ordering = ['-published_date']
    def get_context_data(self, *args,**kwargs):
        cat_menu = Category.objects.all()
        context = super().get_context_data(*args,**kwargs)
        context["cat_menu"] = cat_menu
        return context
def LikeView(request,pk):
    # print(request.POST.get('post_id'))
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True
    
    return HttpResponseRedirect(reverse('article', args=[str(pk)]))
def CategoryListView(request):
    cat_menu_list = Category.objects.all()
    return render(request,'categories_menu.html',{'cat_menu_list':cat_menu_list})
def CategoryView(request,cats):
# #     # print(cats,' is category')
# #     # print(Category.objects.get(name=cats))
#     # category_posts = Post.objects.filter(category=Category.objects.all().filter(name=cats.replace('-',' ')).first())
    category_posts = Post.objects.filter(category=cats.replace('-',' '))
    return render(request,'categories.html',{'cats':cats.title().replace('-',' '),'category_posts':category_posts})
# def CategoryByid(request,id):
#     print(id,' is id \n')
#     category_posts = Category.objects.all().filter(id=id)
#     return render(request,'categories.html',{'cats':id,'category_posts':category_posts})
class article_view(DetailView):
    model = Post
    template_name = 'article_detail.html'
    fields = '__all__'
    def get_context_data(self, *args,**kwargs):
        cat_menu = Category.objects.all()
        stuff = get_object_or_404(Post,id=self.kwargs['pk'])
        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True
        total_likes = stuff.total_likes()
        context = super().get_context_data(*args,**kwargs)
        context["cat_menu"] = cat_menu
        context["total_likes"] = total_likes
        context["liked"] = liked
        return context
class AddPost(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'add_post.html'
    # fields = '__all__'
    #fields = ('title','body')
class EditPost(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'edit_post.html'
    # fields =('title','body')
class DeletePost(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')
class AddCategory(CreateView):
    model = Category
    # form_class = PostForm
    template_name = 'add_category.html'
    fields ='__all__'
