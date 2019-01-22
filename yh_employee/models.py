# import os

from django.core.validators import FileExtensionValidator
from django.db import models

from leaveManagementApp.models import Employee


class Document(models.Model):
    pass

# create document path
# def user_directory_path(instance, filename):
#     filename, file_extension = os.path.splitext(filename)
#     return 'documents/user_{0}/{1}_{2}{3}'.format(instance.employee.id, instance.label, uuid.uuid4(),
#                                                   file_extension)
#
# label = models.CharField(max_length=20)
# description = models.TextField()
#
# # pass the document path and the extensions validator to the file field
# attached_piece = models.FileField(upload_to=user_directory_path,
#                                   validators=[FileExtensionValidator(['pdf', 'doc', 'docx', 'jpg', 'jpeg', 'png'])])
# salaried = models.ForeignKey(Employee, on_delete=models.CASCADE)
