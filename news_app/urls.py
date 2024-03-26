from django.urls import path
from .views import news_list, news_detail, homePageView, ContactPageView, fourPageView, HomePageView, LocalNewsView, XorijNewsView, SportNewsView, TechNewsView


urlpatterns = [
    path('', HomePageView.as_view(), name='home_page'),
    path('news/', news_list, name='all_news_list'),
    path("news/<slug:news>/", news_detail, name='news_detail_page'),
    path('contact-us/', ContactPageView.as_view(), name='contact_page'),
    path('404-page/', fourPageView, name='four_page'),
    path('mahalliy/', LocalNewsView.as_view(), name='local_news_page'),
    path('xorijiy/', XorijNewsView.as_view(), name='foreign_news_page'),
    path('sport/', SportNewsView.as_view(), name='sport_news_page'),
    path('texnologiya/', TechNewsView.as_view(), name='tech_news_page'),
]