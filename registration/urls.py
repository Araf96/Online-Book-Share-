from django.conf.urls import url,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from material.frontend import urls as frontend_urls



app_name = 'onlinebookshare'

urlpatterns = [
    url(r'^$', views.UserView.as_view(), name='sign_in'),
    url(r'^signup/$', views.CreateAccountView.as_view(), name='sign_up'),
    url(r'^homepage/$', views.update_home, name='homepage'),
    url(r'^profile/$', views.user_about, name='account'),
    url(r'^overview/$', views.Overview, name='overview'),
    url(r'^help/$', views.Help, name='help'),
    url(r'^buy_exchange/$', views.Buy_or_Exchange, name='buy_exchange'),
    url(r'^boex_details/(?P<book_no>[0-9]+)/$', views.buy_book_details, name='buybookdetails'),
    url(r'^profile_update/$', views.update_profile, name='update_profile'),
    url(r'^mylibrary/$', views.user_library, name='library'),
    url(r'^addbook/$', views.add_book, name='addbook'),
    url(r'^details/(?P<book_no>[0-9]+)/$', views.book_details, name='bookdetails'),
    url(r'^delete/(?P<book_no>[0-9]+)/$', views.book_delete, name='bookdelete'),
    url(r'^favorite/(?P<book_no>[0-9]+)/$', views.book_favorite, name='bookfavorite'),
    url(r'^home/$', views.Home, name='home'),
    url(r'^post/$', views.Post, name='post'),
    url(r'^messages/$', views.Messages, name='messages'),
    url(r'^search/$', views.search_books, name='search'),
    url(r'^logout/$', views.log_out, name='logout'),
    url(r'^createnotification/$', views.CreateNotification, name='createnotification'),
    url(r'^notificatgionread/$', views.NotificatgionRead, name='notificatgionread'),

]













