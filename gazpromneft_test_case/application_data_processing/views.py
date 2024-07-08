from django.shortcuts import render
from .models import ApplicationData
from .forms import UploadFileForm
from .business_logic import get_application_data_from_file


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
                start_date, end_date = form.cleaned_data['start_date'], form.cleaned_data['end_date']
                application_data_date_range = get_application_data_from_file(uploaded_file.file.path, start_date, end_date)
                application_data = get_application_data_from_file(uploaded_file.file.path)
                items = zip(rows_name, application_data_date_range, application_data)
                return render(request, 'index.html', {'items': items, 'form': form, 'files': files})
            except ValueError as e:
                error_message = e
        else:
            error_message = form.errors.get('file')
    else:
        form = UploadFileForm()

    return render(request, 'index.html', {'form': form, 'files': files, 'data': None, 'error_message': error_message})
