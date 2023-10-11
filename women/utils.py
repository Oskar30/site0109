from women import models

menu = [{"title":"О сайте", "url_name":"about"},
        {"title":"Добавить статью", "url_name":"add_page"},
        {"title":"Обратная связь", "url_name":"contact"}]

class DataMixin:
    paginate_by = 10
    def get_user_context(self, **kwargs):
        context = kwargs
        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu.pop(1)

        context['menu'] = user_menu
        #categories = models.Category.objects.all()
        #context['categories'] = categories
        #if 'cat_selected' not in context:
        #    context['cat_selected'] = 0
        return context