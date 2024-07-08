from django.db import models


class ApplicationData(models.Model):

    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    unique_application_numbers = models.IntegerField(null=True)
    unique_duplicate_numbers = models.IntegerField(null=True)
    unique_add_status_numbers = models.IntegerField(null=True)
    unique_extension_numbers = models.IntegerField(null=True)
    processing_complete_numbers = models.IntegerField(null=True)
    returned_for_clarification_status_numbers = models.IntegerField(null=True)
    sent_for_processing_status_numbers = models.IntegerField(null=True)
    unique_id_packages = models.IntegerField(null=True)
    unique_request_author = models.IntegerField(null=True)

    def __str__(self):
        return f"Файл загружен в {self.uploaded_at}"

