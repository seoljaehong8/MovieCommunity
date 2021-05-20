from django.urls import path
from . import views

app_name = 'reviews'
urlpatterns = [
    path('', views.review_list_create),
    path('<int:movie_pk>/<int:review_pk>/',views.review_detail_delete_update),
    path('comment/<int:reivew_pk>/<int:comment_pk>/', views.comment_create_delete),

]