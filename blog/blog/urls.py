from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


handler404 = views.page_not_found

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", views.index, name="index"), #pagina principal
    path("about/", views.about, name="about"), #pagina de about
    path("user/", include("apps.user.urls")), #apartado de login
    path("post/", include("apps.post.urls")), #apartado de post
    path("contact/", include("apps.contact.urls")), #apartado de contacto
    ] +static(settings.STATIC_URL,
document_root=settings.STATIC_ROOT)
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL,
document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

 ## Password Reset ### https://www.youtube.com/watch?v=y-4-qv9_zP8
    #tiene un input de email para enviar el link de reseteo de contraseña
    #path("reset_password/", auth_views.PasswordResetView.as_view(), name="reset_password"),
    #envia el link de reseteo de contraseña al email y muestra un mensaje de que se envio correctamente
    #path("reset_password_send", auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    #tiene identificador de usuario y token para resetear la contraseña
    #path("reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    #muestra el mensaje de que la contraseña se reseteo correctamente
    #path("reset_password_complete/", auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),