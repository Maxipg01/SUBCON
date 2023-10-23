from django.urls import path
from . import views

app_name = 'cuentas'

urlpatterns = [
    path('', views.login_view, name='login'),
    path('registro/', views.registro_view, name='registro'),
    path('menu/', views.menu_view, name='menu'),
    path('menu/<int:usuario_id>/', views.menu_view, name='menu'),
    path('actualizar/', views.actualizar_view, name='actualizar'),
    path('exito/', views.exito_view, name='exito'),
    path('pedidos/', views.pedidos_view, name = 'pedidos'),
    path('pedidos/<int:usuario_id>/', views.pedidos_view, name='pedidos'),
    path('pedidos_4C/', views.pedidos4C_view, name='pedidos4C'),
    path('pedidos_4C/<int:usuario_id>/', views.pedidos4C_view, name='pedidos4C'),
    path('exportar-pdf/', views.exportar_pdf, name='exportar_pdf'),
    path('exportar-txt/', views.exportar_txt, name='exportar_txt'),
    path('enviar-correo/', views.enviar_correo, name='enviar_correo'),
    path('eliminar_producto/<int:producto_id>/', views.eliminar_producto, name='eliminar_producto'),
    path('finalizar_pedido/', views.finalizar_pedido, name='finalizar_pedido'),
    path('finalizar_pedido4C/', views.finalizar_pedido4C, name='finalizar_pedido4C'),
    path('auditoria/', views.auditoria, name='auditoria'),
    path('recuperar-datos/', views.recuperar_datos, name='recuperar_datos'),
    path('resumen_HEB/', views.resumenHEB, name='resumen_HEB'),
    path('auditoriaBebidas/', views.auditoriaBebidas, name='auditoriaBebidas'),
    path('recuperar-datos-Bebidas/', views.recuperar_datos_Bebidas, name='recuperar_datos_Bebidas'),
    path('resumen_HEB_Bebidas/', views.resumenHEB_Bebidas, name='resumen_HEB_Bebidas'),
    path('auditoria_4C/', views.auditoria_4C, name='auditoria_4C'),
    path('recuperar-datos-4C/', views.recuperar_datos_4C, name='recuperar_datos_4C'),
    path('resumen_4C/', views.resumen_4C, name='resumen_4C'),
    path('auditoria_4C_Bebidas/', views.auditoria_4C_Bebidas, name='auditoria_4C_Bebidas'),
    path('recuperar-datos-4C-Bebidas/', views.recuperar_datos_4C_Bebidas, name='recuperar_datos_4C_Bebidas'),
    path('resumen_4C_Bebidas/', views.resumen_4C_Bebidas, name='resumen_4C_Bebidas'),

]
