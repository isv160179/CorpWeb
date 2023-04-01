from django.urls import path


from .views import *

from .views import *

urlpatterns = [
    path('', NewsListView.as_view(), name='news'),
    # path('<int:news_id>/', ShowNews.as_view(), name='news'),
    path('<int:news_id>/', news_detail, name='news_detail'),
    path('add_news/', AddNews.as_view(), name='add_news'),
    path('like/', news_like, name='like'),
]
