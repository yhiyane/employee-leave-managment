from django.urls import path

from . import views

# map urls with views
urlpatterns = [
    # Employee Urls Crud
    path('', views.index, name='employee.index'),
    path('<int:id>', views.show, name='employee.show'),
    path('create', views.create, name='employee.create'),
    path('update/<int:id>', views.update, name='employee.update'),
    path('delete/<int:id>', views.delete, name='employee.delete'),

    # Document Import Export Urls
    # path('import/', views.import_salaried_index, name='employee.import_salaried_index'),
    # path('export/xls/', views.export_salaried_xls, name='employee.export_xls'),
    # path('export/csv/', views.export_salaried_csv, name='employee.export_csv'),

    # Document Edit Urls
    # path('<int:salaried_id>/documents', views.index_document, name='employee.documents.index'),
    # path('<int:salaried_id>/documents/delete/<int:document_id>', views.delete_document,
    #      name='employee.documents.delete'),
    # path('<int:salaried_id>/documents/create', views.create_document, name='employee.documents.create'),
    # path('<int:salaried_id>/documents/update/<int:document_id>', views.update_document,
    #      name='employee.documents.update'),

]
