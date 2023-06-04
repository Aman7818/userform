from django.urls import path
from userform.views import UserFormView, FormListView

urlpatterns = [
    path('user-form/', UserFormView.as_view(), name='user_form'),
    path('form-list/', FormListView.as_view(), name='form_list'),
]
