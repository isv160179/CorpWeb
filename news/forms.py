from django import forms
from django.core.exceptions import ValidationError

# from users.models import UserVB
from .models import News, NewsComments, NewsLikes


# Построение формы связанной с моделями:
class AddNewsForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):  # Конструктор экземпляра класса AddNewsForm
        super().__init__(*args, **kwargs)  # Вызываем конструктор базового класса ModelForm
        self.fields['author'].empty_label = 'Автор не выбран'

    class Meta:
        model = News  # Связь с моделью
        fields = ['title', 'content', 'image', 'is_published', 'author']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'name_of_class1'}),
            'content': forms.Textarea(attrs={'cols': 60, 'rows': 10, 'class': 'name_of_class2'}),
        }

    # def clean_slug(self):
    #     """ Функция пользовательского валидатора """
    #     slug = self.cleaned_data['slug']  # Получаем данные из экземпляра класса, содержащиеся в ячейке Slug
    #     if len(slug) > 20:
    #         raise ValidationError('Длина превышает 20 символов')
    #     return slug


class CommentForm(forms.ModelForm):
    class Meta:
        model = NewsComments
        fields = ('content',)
        widgets = {'content': forms.Textarea(
            attrs={'cols': 40, 'rows': 3, 'class': 'news_new-comment_text', 'placeholder': 'Текст комментария'}), }


class LikeForm(forms.ModelForm):
    class Meta:
        model = NewsLikes
        fields = ()

