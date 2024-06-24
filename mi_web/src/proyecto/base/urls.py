from django.urls import path
from .views import ListaPendientes, DetalleTarea, CrearTarea, EditarTarea,BorrarTarea, Logueo, PaginaRegistro
from django.contrib.auth.views import LogoutView
urlpatterns = [path('', ListaPendientes.as_view(), name='tareas'),
               path('tarea/<int:pk>', DetalleTarea.as_view(), name='tarea'),
               path('registro/', PaginaRegistro.as_view(), name='registro'),
               path('crear-tarea/', CrearTarea.as_view(), name='crear-tarea'),
               path('editartarea/<int:pk>', EditarTarea.as_view(), name='editar-tarea'),
               path('borrar-tarea/<int:pk>', BorrarTarea.as_view(), name='borrar-tarea'),
               path('login/', Logueo.as_view(), name='login'),
               path('logout/', LogoutView.as_view(next_page='login'), name='logout')
               ]


