from django.urls import path
from .views import index, log,card,verifyDoc,logout,registration, verifiedDocument,errorpage,confirm,forgotpassword

urlpatterns = [
    path('index/', index, name="index"),
    path('', registration, name="regi"),
    path('login/', log, name="login"),
    path('verify_document/', verifyDoc, name="verifyDoc"),
    path('logout/', logout, name="logout"),
    path('documents/', verifiedDocument, name="verifiedDoc"),
    path('card/',card,name="card"),
    path('error/',errorpage,name="error"),
    path('confirm/',confirm,name = 'confirm'),
    path('forgotpassword/',forgotpassword,name = 'forgotpassword')

]
