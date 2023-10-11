from django.urls import path
from women import views

urlpatterns = [
    path('', views.Index.as_view(), name='home'),
    path('category/<slug:cat_slug>', views.Category.as_view(), name='category'),
    path('post/<slug:post_slug>', views.ShowPost.as_view(), name='post'),
    path('addpage/', views.AddPage.as_view(), name='add_page'),
    path('register/', views.RegisterUser.as_view(), name='register'),
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    
    

    #path('categories/', views.categories, name='categories'),
    #
]

