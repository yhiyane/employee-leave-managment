from django.core.paginator import Paginator


def paginate(request, paginator: Paginator):
    page = request.GET.get('page')
    items_page = paginator.get_page(page)
    index = items_page.number - 1
    max_index = len(paginator.page_range)
    start_index = index - 5 if index >= 5 else 0
    end_index = index + 5 if index <= max_index - 5 else max_index
    return {
        'page_range': paginator.page_range[start_index:end_index],
        'page_items': items_page,
    }
