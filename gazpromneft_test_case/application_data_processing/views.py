from django.shortcuts import render
from .models import ApplicationData
from .forms import UploadFileForm
from .business_logic import get_application_data_from_file


def format_application_data(application_data: tuple) -> list:
    return [str(data).replace("0", "-") if data == 0 else data for data in application_data]


def index(request):
    files = ApplicationData.objects.all()
    error_message = None
    rows_name = ("Загруженных заявок",
                 "Дубли",
                 "На создание",
                 "На расширение",
                 "Обработка завершена",
                 "Возвращена на уточнение",
                 "Отправлена в обработку",
                 "Пакетов",
                 "Пользователей"
                 )

    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            try:
                uploaded_file = form.save()
                file_path = uploaded_file.file.path
                start_date, end_date = form.cleaned_data['start_date'], form.cleaned_data['end_date']
                application_data_date_range = get_application_data_from_file(file_path,
                                                                             start_date,
                                                                             end_date)
                application_data = get_application_data_from_file(file_path)
                ApplicationData.update_application_data(uploaded_file.id, application_data_date_range, start_date,
                                                        end_date)  # Сохраняем промежуточные результаты в БД
                application_data_date_range_format = format_application_data(application_data_date_range)
                application_data_format = format_application_data(application_data)
                application_data_date_range_str = ['+' + str(data) if data != '-' else data for data in
                                                   application_data_date_range_format]
                items = zip(rows_name, application_data_date_range_str, application_data_format)
                return render(request, 'index.html', {'items': items, 'form': form, 'files': files})
            except ValueError as e:
                error_message = e
        else:
            error_message = form.errors.get('file')
    else:
        form = UploadFileForm()

    return render(request, 'index.html', {'form': form, 'files': files, 'data': None, 'error_message': error_message})
