from django.shortcuts import render
from .models import *
from .forms import *

# Create your views here.
def main_page(request):
    return render(request, 'main.html')

def descript_page(request):
    return render(request, 'descript.html')

def book_litera(request):
    context={}
    if request.method == 'POST':
        form = BookState(request.POST)
        if form.is_valid():
            author = form.cleaned_data['author']
            name_father_Author = form.cleaned_data['name_father_Author']
            title = form.cleaned_data['title']
            publisher = form.cleaned_data['publisher']
            city = form.cleaned_data['city']
            year = form.cleaned_data['year']
            pages = form.cleaned_data['pages']
            context = {
                'author': author,
                'name_father_Author': name_father_Author,
                'title': title,
                'publisher': publisher,
                'city': city,
                'year': year,
                'pages': pages
            }
            Book.objects.create(author = author,
                                name_father_Author = name_father_Author,
                                title = title,
                                publisher = publisher,
                                city = city,
                                year = year,
                                pages = pages)
        return render(request, 'book_final.html', context)
    else:
        form = BookState()
        context['form'] = form
    return render(request, 'book.html', context)


def journal_litera(request):
    context={}
    if request.method == 'POST':
        form = JournalState(request.POST)
        if form.is_valid():
            author = form.cleaned_data['author']
            name_father_Author = form.cleaned_data['name_father_Author']
            title = form.cleaned_data['title']
            publisher = form.cleaned_data['publisher']
            number_tom = form.cleaned_data['number_tom']
            year = form.cleaned_data['year']
            page_start = form.cleaned_data['page_start']
            page_end = form.cleaned_data['page_end']
            context = {
                'author': author,
                'name_father_Author': name_father_Author,
                'title': title,
                'publisher': publisher,
                'number_tom': number_tom,
                'year': year,
                'page_start': page_start,
                'page_end': page_end
            }
            Journal.objects.create(author = author,
                                name_father_Author = name_father_Author,
                                title = title,
                                publisher = publisher,
                                number_tom = number_tom,
                                year = year,
                                page_start = page_start,
                                page_end = page_end)
        return render(request, 'journal_final.html', context)
    else:
        form = BookState()
        context['form'] = form
    return render(request, 'journal.html', context)


def conf_litera(request):
    context={}
    if request.method == 'POST':
        form = ConfState(request.POST)
        if form.is_valid():
            author = form.cleaned_data['author']
            name_father_Author = form.cleaned_data['name_father_Author']
            title = form.cleaned_data['title']
            publisher = form.cleaned_data['publisher']
            place = form.cleaned_data['place']
            date = form.cleaned_data['date']
            year = form.cleaned_data['year']
            city = form.cleaned_data['city']
            page_start = form.cleaned_data['page_start']
            page_end = form.cleaned_data['page_end']
            context = {
                'author': author,
                'name_father_Author': name_father_Author,
                'title': title,
                'publisher': publisher,
                'place': place,
                'date': date,
                'year': year,
                'city': city,
                'page_start': page_start,
                'page_end': page_end
            }
            Journal.objects.create(author = author,
                                name_father_Author = name_father_Author,
                                title = title,
                                publisher = publisher,
                                city = city,
                                place = place,
                                date = date,
                                year = year,
                                page_start = page_start,
                                page_end = page_end)
        return render(request, 'conf_final.html', context)
    else:
        form = BookState()
        context['form'] = form
    return render(request, 'conf.html', context)