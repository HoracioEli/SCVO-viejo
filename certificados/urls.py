from django.urls import path
from . import views



urlpatterns = [
    path("",views.index, name="index"),
    path('registrarPoliza/', views.registrarPoliza),
    path('nuevaPoliza/', views.nuevaPoliza),
    path('edicionPoliza/<int:id>', views.edicionPoliza),
    path('editarPoliza/<int:id>', views.editarPoliza),
    path('eliminacionPoliza/<int:id>', views.eliminacionPoliza),
    path('listadoEmpleados/<int:id>', views.listadoEmpleados),
    path('edicionEmpleado/<int:id>', views.edicionEmpleado),
    path('editarEmpleado/<int:id>/<int:id_poliza>', views.editarEmpleado),
    path('registrarEmpleado/<int:id_poliza>', views.registrarEmpleado),
    path('eliminarEmpleado/<int:id>/<int:id_poliza>', views.eliminarEmpleado),
]