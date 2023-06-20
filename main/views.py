from django.shortcuts import render
from .models import *
from django.shortcuts import render, get_object_or_404
from django.db.models import Q

# Create your views here.
def license_category_list(request):
    query = request.GET.get('q')
    
    categories = LicenseCategory.objects.all()
    
    if query:
        categories = categories.filter(
            Q(name__icontains=query)
        )
    
    context = {'categories': categories, 'query': query}
    return render(request, 'main/license_category_list.html', context)


def license_list(request, category_id=None):
    licenses = License.objects.all()
    category = None
    
    if category_id is not None:
        category = get_object_or_404(LicenseCategory, id=category_id)
        licenses = licenses.filter(category=category)
    
    query = request.GET.get('q')
    if query:
        licenses = licenses.filter(
            Q(name__icontains=query) | Q(license_number__icontains=query)
        )
    
    context = {
        'licenses': licenses,
        'category': category,
        'category_id': category_id,
        'query': query,
    }
    return render(request, 'main/license_list.html', context)