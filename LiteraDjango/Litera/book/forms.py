from django import forms


class BookState(forms.Form):
    author = forms.CharField(max_length=30, label='Введите только фамилию автора (Иванов):')
    name_father_Author = forms.CharField(max_length=4, label='Введите инициалы автора (И. И.):')
    title = forms.CharField(max_length=200, label='Введите название источника (Что я делал эти летом):')
    publisher = forms.CharField(max_length=20, label='Введите издателя источника (Полиграф):')
    city = forms.CharField(max_length=20, label='Введите город, в котором был издан источник (Спб):')
    year = forms.IntegerField(label='Введите год, в котором был издан источник (2000):')
    pages = forms.IntegerField(label='Введите количество страниц в выбранном вами источнике (256):')

class JournalState(forms.Form):
    author = forms.CharField(max_length=30, label='Введите только фамилию автора (Иванов):')
    name_father_Author = forms.CharField(max_length=4, label='Введите инициалы автора (И. И.):')
    title = forms.CharField(max_length=200, label='Введите наименование статьи (Что я изучил этим летом):')
    publisher = forms.CharField(max_length=50, label='Введите название журнала (Ежелетнее изучения всего):')
    number_tom = forms.IntegerField(label='Введите порядковый номер издания журнала (21):')
    year = forms.IntegerField(label='Введите год, в котором был издан источник (2000):')
    page_start = forms.IntegerField(label='Введите страницу на которой начинается статья (256):')
    page_end = forms.IntegerField(label='Введите страницу на которой заканчивается статья (287):')


class ConfState(forms.Form):
    author = forms.CharField(max_length=30, label='Введите только фамилию автора (Иванов):')
    name_father_Author = forms.CharField(max_length=4, label='Введите инициалы автора (И. И.):')
    title = forms.CharField(max_length=200, label='Введите наименование статьи (Что я изучил этим летом):')
    publisher = forms.CharField(max_length=150, label='Введите название темы конференции (Каждое лето мы изучаем что-то новое):')
    place = forms.CharField(max_length=20, label='Введите город, в котором проводилась конференция (Иркутск):')
    date = forms.DateField(label='Дата проведения конференции (21-22 сент. 2010 г.):')
    year = forms.IntegerField(label='Введите год, в котором был издан источник (2000):')
    city = forms.CharField(max_length=20, label='Введите город, в котором был издан источник (Спб):')
    page_start = forms.IntegerField(label='Введите страницу на которой начинается статья (256):')
    page_end = forms.IntegerField(label='Введите страницу на которой заканчивается статья (287):')