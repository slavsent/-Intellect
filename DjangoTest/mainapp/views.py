import logging
import datetime

from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.http import FileResponse, JsonResponse
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, TemplateView, UpdateView, View
from dateutil import parser
from django.utils.timezone import make_aware

from mainapp import forms as mainapp_forms
from mainapp import models as mainapp_models

logger = logging.getLogger(__name__)


class MainPageView(TemplateView):
    template_name = "mainapp/index.html"


class NewsPageView(TemplateView):
    template_name = "mainapp/news.html"

    def get_context_data(self, **kwargs):
        # Get all previous data
        context = super().get_context_data(**kwargs)
        # Create your own data
        context["news_title"] = "Громкий новостной заголовок"
        context["news_preview"] = "Предварительное описание, которое заинтересует каждого"
        context["range"] = range(5)
        context["datetime_obj"] = datetime.datetime.now()
        return context


class NewsWithPaginatorView(NewsPageView):
    def get_context_data(self, page, **kwargs):
        context = super().get_context_data(page=page, **kwargs)
        context["page_num"] = page
        return context


class CoursesPageView(TemplateView):
    template_name = "mainapp/courses_list.html"


class ContactsPageView(TemplateView):
    template_name = "mainapp/contacts.html"


class DocSitePageView(TemplateView):
    template_name = "mainapp/doc_site.html"


class LogView(TemplateView):
    template_name = "mainapp/log_view.html"

    def get_context_data(self, **kwargs):
        context = super(LogView, self).get_context_data(**kwargs)
        log_slice = []
        with open(settings.LOG_FILE, "r") as log_file:
            for i, line in enumerate(log_file):
                if i == 1000:  # first 1000 lines
                    break
                log_slice.insert(0, line)  # append at start
            context["log"] = "".join(log_slice)
        return context


class LogDownloadView(UserPassesTestMixin, View):
    def test_func(self):
        return self.request.user.is_superuser

    def get(self, *args, **kwargs):
        return FileResponse(open(settings.LOG_FILE, "rb"))


class QuotesListView(LoginRequiredMixin, ListView):
    model = mainapp_models.Quotes
    login_url = 'authapp:login'
    redirect_field_name = 'redirect_to'
    paginate_by = 5
    logger.debug(f"A list of quotes is being created")

    def get_queryset(self):
        from_date = self.request.GET.get('dateFrom')
        to_date = self.request.GET.get('dateTo')
        logger.debug(f"Selecting quotes by filter")
        if from_date and to_date:
            logger.debug(f"Selecting quotes by filter, if there are dates from and to")
            return super().get_queryset().filter(
                time_quote__range=(make_aware(parser.parse(from_date)), make_aware(parser.parse(to_date + ' 23:59:59'))),
                deleted=False)
        elif from_date:
            logger.debug(f"Selecting quotes by filter, if there is only a date from")
            return super().get_queryset().filter(
                time_quote__gte=(parser.parse(from_date)), deleted=False)
        elif to_date:
            logger.debug(f"Selecting quotes by filter, if there is only a date before")
            return super().get_queryset().filter(time_quote__lte=make_aware(parser.parse(to_date + ' 23:59:59')),
                                                 deleted=False)
        else:
            logger.debug(f"Quotes Selection full list")
            return super().get_queryset().filter(deleted=False)


class QuotesUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = mainapp_models.Quotes
    fields = ['simbol', 'time_quote', 'open', 'high', 'low', 'close', 'volume']
    login_url = 'authapp:login'
    redirect_field_name = 'redirect_to'
    success_url = reverse_lazy("mainapp:quotes")
    permission_required = ("mainapp.change_quotes",)
    logger.debug(f"Changing the quotes")


class QuotesDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = mainapp_models.Quotes
    login_url = 'authapp:login'
    redirect_field_name = 'redirect_to'
    success_url = reverse_lazy("mainapp:quotes")
    permission_required = ("mainapp.delete_quotes",)
    logger.debug(f"Deleting quotes")
