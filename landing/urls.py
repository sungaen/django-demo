from django.urls import path

from landing import views


app_name = "landing"
urlpatterns = [
    
    path("index/", views.index, name="home"),## 리스트에 정리하는 것
    # path("create/", views.post_create, name="create"),
    path("temptest/", views.temp_test),
    path("read-all/", views.post_read_all, name="read-all"),
    path("read/<int:post_id>/", views.post_read, name="read"),
    path("update/<int:post_id>/",views.post_update, name="update"),
    path("delete/<int:post_id>/", views.post_delete, name="delete"),
    path("create/", views.post_create, name="create"),
    path("path-test/<int:i>/<int:j>/", views.temp_test, name="url_test"),
]