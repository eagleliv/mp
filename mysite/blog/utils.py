from django.core.paginator import Paginator
from django.shortcuts import render

def pagi_nator(request, num_com, comments = '', details = ''):
    pagi = Paginator(comments, num_com)
    page_number = request.GET.get('page', 1)
    page = pagi.get_page(page_number)
    is_paginated = page.has_other_pages()

    if page.has_previous():
        prev_url = '?page={}'.format(page.previous_page_number())
    else:
        prev_url = ''

    if page.has_next():
        next_url = '?page={}'.format(page.next_page_number())
    else:
        next_url = ''

    context = {'comments': page, 'details': details, 'prev_url': prev_url, 'next_url': next_url}
    
    if request.POST:
        return context
    elif details == '':
        return render(request, 'blog/blog.html', context = {'comments': page, 'prev_url': prev_url, 'next_url': next_url})
    else:
        return render(request, 'blog/blog_details.html', context = context)
