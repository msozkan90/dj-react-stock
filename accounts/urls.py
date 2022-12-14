from django.urls import path
from . import views
app_name="accounts"
urlpatterns = [

    path("index",views.index,name="index"),
    path("register/",views.register,name="register"),
    path("signin/",views.signin,name="signin"),
    path("logout/",views.log_out,name="logout"),
    path("add/pharmacy",views.add_pharmacy,name="add_pharmacy"),
    path("add/pharmacy/react",views.add_pharmacy_react,name="add_pharmacy_react"),
    path("edit/pharmacy/<int:pk>/react",views.edit_pharmacy_react,name="edit_pharmacy_react"),
    path("pharmacy/list",views.pharmacy_list,name="pharmacy_list"),
    path("edit/pharmacy/<int:pk>/",views.edit_pharmacy,name="edit_pharmacy"),
 

    
]
