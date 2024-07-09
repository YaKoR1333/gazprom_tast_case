import datetime

from django.db import models


class ApplicationData(models.Model):
    file = models.FileField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    start_date = models.DateTimeField(null=True)
    end_date = models.DateTimeField(null=True)
    unique_application_numbers = models.IntegerField(null=True)
    unique_duplicate_numbers = models.IntegerField(null=True)
    unique_add_status_numbers = models.IntegerField(null=True)
    unique_extension_numbers = models.IntegerField(null=True)
    processing_complete_numbers = models.IntegerField(null=True)
    returned_for_clarification_status_numbers = models.IntegerField(null=True)
    sent_for_processing_status_numbers = models.IntegerField(null=True)
    unique_id_packages = models.IntegerField(null=True)
    unique_request_author = models.IntegerField(null=True)

    @staticmethod
    def update_application_data(row_id: int, application_data_tuple: tuple, start_date: datetime, end_date: datetime) -> None:
        application_data = ApplicationData.objects.get(id=row_id)
        application_data.unique_application_numbers, \
            application_data.unique_duplicate_numbers, \
            application_data.unique_add_status_numbers, \
            application_data.unique_extension_numbers, \
            application_data.processing_complete_numbers, \
            application_data.returned_for_clarification_status_numbers, \
            application_data.sent_for_processing_status_numbers, \
            application_data.unique_id_packages, \
            application_data.unique_request_author = application_data_tuple

        application_data.start_date, application_data.end_date = start_date, end_date

        application_data.save()

    def __str__(self):
        return f"Файл загружен в {self.uploaded_at}"
