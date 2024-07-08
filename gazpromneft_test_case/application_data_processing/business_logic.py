import pandas as pd


def get_application_data_from_file(file_path: str, datetime_start: str = None, datetime_end: str = None) -> tuple:
    """Отдаёт данные из exel файла по следующим данным:
    количество уникальных номеров заявок,
    количество уникальных номеров заявок с состоянием "Дубликат",
    количество заявок с состоянием "ДОБАВЛЕНИЕ",
    количество заявок с состоянием "РАСШИРЕНИЕ",
    количество заявок со статусом "Обработка завершена",
    количество заявок со статусом "Возвращена на уточнение",
    количество заявок со статусом "Отправлена в обработку",
    количество уникальных ID пакетов,
    количество уникальных Авторов заявки.

    Структура таблицы:
    Номер заявки - 0,
    Состояние заявки - 1,
    Согласование - 2,
    Статус заявки - 3,
    Автор заявки - 4,
    Имя файла - 5,
    Дата создания заявки - 6,
    Дата окончания обработки - 7,
    Время от создания заявки до конца обработки (в часах) - 8,
    Полное наименование изначальное - 9,
    Полное наименование после обработки - 10,
    Код материала - 11,
    Похожие материалы полученные из КП - 12,
    БЕИ - 13,
    НТД - 14,
    ID пакета -15
    """
    xls = pd.ExcelFile(file_path)

    df = pd.read_excel(xls, 'Data')

    df['Дата создания заявки'] = pd.to_datetime(df['Дата создания заявки'],
                                                errors='coerce',
                                                dayfirst=True,
                                                format="mixed")

    df.iloc[:, 3] = df.iloc[:, 3].str.lower()  # Приводим все данные в 4 столбце к нижнему регистру
    df.iloc[:, 1] = df.iloc[:, 1].str.lower()  # Приводим все данные в 2 столбце к нижнему регистру

    duplicate_condition_df = df[df.iloc[:, 1].str.contains('дубликат')]
    add_condition_df = df[df.iloc[:, 1].str.contains('добавление')]
    extension_condition_df = df[df.iloc[:, 1].str.contains('расширение')]
    processing_complete_status_df = df[df.iloc[:, 3].str.contains('обработка завершена')]
    returned_for_clarification_status_df = df[df.iloc[:, 3].str.contains('возвращена на уточнение')]
    sent_for_processing_status_df = df[df.iloc[:, 3].str.contains('отправлена в обработку')]

    if datetime_start and datetime_end:
        def get_data_in_time_range(input_df: pd.DataFrame) -> pd.DataFrame:
            """Определяет какое количество данных в дата фрейме попадает в заданный временной диапазон"""
            return input_df[(input_df.iloc[:, 6]
                             >= start_date) &
                            (input_df.iloc[:, 6]
                             <= end_date)]

        start_date = pd.to_datetime(datetime_start,
                                    errors='coerce',
                                    dayfirst=True,
                                    format="mixed")

        end_date = pd.to_datetime(datetime_end,
                                  errors='coerce',
                                  dayfirst=True,
                                  format="mixed")

        df = get_data_in_time_range(df)

        duplicate_condition_df = get_data_in_time_range(duplicate_condition_df)

        add_condition_df = get_data_in_time_range(add_condition_df)

        extension_condition_df = get_data_in_time_range(extension_condition_df)

        processing_complete_status_df = get_data_in_time_range(processing_complete_status_df)

        returned_for_clarification_status_df = get_data_in_time_range(returned_for_clarification_status_df)

        sent_for_processing_status_df = get_data_in_time_range(sent_for_processing_status_df)

    unique_application_numbers = df.iloc[:, 0].nunique()
    unique_duplicate_numbers = duplicate_condition_df.iloc[:, 0].nunique()
    unique_add_status_numbers = add_condition_df.iloc[:, 0].nunique()
    unique_extension_numbers = extension_condition_df.iloc[:, 0].nunique()
    processing_complete_numbers = processing_complete_status_df.iloc[:, 0].nunique()
    returned_for_clarification_status_numbers = returned_for_clarification_status_df.iloc[:, 0].nunique()
    sent_for_processing_status_numbers = sent_for_processing_status_df.iloc[:, 0].nunique()
    unique_id_packages = df.iloc[:, -1].nunique()
    unique_request_author = df.iloc[:, 4].nunique()

    data_tuple = (unique_application_numbers,
                  unique_duplicate_numbers,
                  unique_add_status_numbers,
                  unique_extension_numbers,
                  processing_complete_numbers,
                  returned_for_clarification_status_numbers,
                  sent_for_processing_status_numbers,
                  unique_id_packages,
                  unique_request_author)

    return data_tuple
