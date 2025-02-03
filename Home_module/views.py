from django.core.paginator import Paginator
from django.shortcuts import render
from django.views.generic import TemplateView, View
from Home_module.models import Settings, Services, Customers, Gallery, Staff

# Create your views here.


class HomeView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['services'] = Services.objects.all()
        context['customers'] = Customers.objects.all()
        context['settings'] = Settings.objects.get(id=2)
        gallery_list = Gallery.objects.all()
        paginator = Paginator(gallery_list, 9)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context['gallery'] = page_obj
        context['staff'] = Staff.objects.all()

        return context


def site_header_components(request):
    settings = Settings.objects.get(id=2)
    return render(request, 'site_header_components.html', {
        'settings': settings,
    })


def site_footer_components(request):
    footer_setting = Settings.objects.all()
    return render(request, 'site_footer_components.html', {
        'footer_setting': footer_setting,
    })

