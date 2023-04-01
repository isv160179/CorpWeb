from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render, redirect
from django.views.decorators.http import require_POST
from django.views.generic import ListView, DetailView, CreateView

from CorpWebsite.utils import DataMixin
from home.models import WebsiteFeatures
from .models import *
from .forms import AddNewsForm, CommentForm, LikeForm


@login_required
def news_detail(request, news_id):
    news = get_object_or_404(News, pk=news_id)
    comments = news.news_comments.all()
    likes = news.news_likes.all()
    new_comment = None
    # new_like = None
    like_present = False
    if likes.filter(author=request.user):
        like_present = True
    if request.method == 'POST':
        comment_form = CommentForm(request.POST, prefix='banned')
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.author = request.user
            new_comment.news = news
            new_comment.save()
    else:
        comment_form = CommentForm(prefix='banned')

    if request.method == 'POST' and not comment_form.is_valid():
        like_form = LikeForm(request.POST, prefix='expected')
        comment_form = CommentForm(prefix='banned')

        if not like_present:
            new_like = like_form.save(commit=False)
            new_like.author = request.user
            new_like.news = news
            new_like.save()
            like_present = True
        else:
            like_user = likes.get(author=request.user)
            like_user.delete()
            like_present = False
    else:
        like_form = LikeForm(prefix='expected')

    menu = WebsiteFeatures.objects.filter(is_active=True)
    context = {
        'menu': menu,
        'menu_selected': 0,
        'news': news,
        'comments': comments,
        'likes': likes,
        'new_comment': new_comment,
        'like_present': like_present,
        'comment_form': comment_form,
        'like_form': like_form,
        'title': 'Подробнее о новости',
        'word_colleague': ('коллеге', 'коллегам', 'коллегам'),
        'word_comments': ('комментарий', 'комментария', 'комментариев'),
    }
    return render(request, 'news/news_detail.html', context=context)


@login_required
@require_POST
def news_like(request):
    news_id = request.POST.get('id')
    action = request.POST.get('action')
    if news_id and action:
        try:
            news = News.objects.get(id=news_id)
            if action == 'love':
                news.users_love.add(request.user)
            else:
                news.users_love.remove(request.user)
            return JsonResponse({'status': 'ok'})
        except:
            pass
    return JsonResponse({'status': 'ok'})


class NewsListView(DataMixin, ListView):
    """ Класс отображения всех новостей на главной странице сайта """
    paginate_by = 5  # Количество отображаемых на странице новостей
    model = News  # Указание на модель
    template_name = 'news/index.html'  # Указание на страницу, которая должна вызываться
    # в качестве представления модели вместо стандартной main/news_list.html
    context_object_name = 'news'  # Указание на пользовательскую переменную,

    # в которую передаются данные об экземпляре класса вместо стандартной object_list

    def get_queryset(self):
        """
        Функция возвращает из модели экземпляры,
        которые удовлетворяют указанным условиям
        """
        return News.objects.filter(is_published=True).order_by('-time_create').select_related('author')

    def get_context_data(self, *, object_list=None, **kwargs):
        """ Функция создания контекста с динамическими (изменяемыми данными)"""
        context = super().get_context_data(**kwargs)  # Передаем в словарь context данные из модели (всю таблицу)
        c_def = self.get_user_context(title=f'Новости', menu_selected=1)
        return dict(list(context.items()) + list(c_def.items()))


# class ShowNews(DataMixin, DetailView):
#     """ Класс отображения выбранной новости по кнопке 'Подробнее' или по иконке 'Комментарии' """
#     model = News
#     template_name = 'news/news.html'
#     pk_url_kwarg = 'news_id'
#     # slug_url_kwarg = 'news_slug'  # Переопределение переменной - вместо стандартной slug указываем news_slug
#     context_object_name = 'news'
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         c_def = self.get_user_context(title='Подробнее о новости', words=('коллеге', 'коллегам', 'коллегам'))
#         return dict(list(context.items()) + list(c_def.items()))


class AddNews(DataMixin, CreateView):
    """ Класс добавления новой новости """
    form_class = AddNewsForm
    template_name = 'news/add_news.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Добавить новость')
        return dict(list(context.items()) + list(c_def.items()))
