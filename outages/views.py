from django.shortcuts import render

# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import (
    ListView, DetailView,
    CreateView, UpdateView, DeleteView
)
from outages.models import Outage


def error_404_view(request, exception):
    return render(request, 'outages/404.html')


class HomeView():
    """ Default home page or index page"""
    model = Outage
    context_object_name = 'home'
    template_name = "outages/test.html"


class OutageListView(ListView):
    """ List View containing ONLY Active Pending Resolved . Queryset based on status """
    model = Outage
    context_object_name = 'outages_all'
    template_name = 'outages/outage_all.html'

    def get_queryset(self):
        return Outage.objects.exclude(status='closed')


class OutageActiveListView(ListView):
    """ List View containing ONLY Active. Queryset based on status """
    model = Outage
    context_object_name = 'outages_active'
    template_name = 'outages/outage_activelist.html'

    def get_queryset(self):
        return Outage.objects.filter(status='active')


class OutagePendingListView(ListView):
    """ List View containing ONLY Pending. Queryset based on status """
    model = Outage
    context_object_name = 'outages_pending'
    template_name = 'outages/outage_pendinglist.html'

    def get_queryset(self):
        return Outage.objects.filter(status='pending')


class OutageResolvedListView(ListView):
    """ List View containing ONLY Resolved. Queryset based on status """
    model = Outage
    context_object_name = 'outages_resolved'
    template_name = 'outages/outage_resolvedlist.html'

    def get_queryset(self):
        return Outage.objects.filter(status='resolved')


class OutageClosedListView(LoginRequiredMixin, ListView):
    """ List View containing ONLY Closed. Queryset based on status """
    model = Outage
    context_object_name = 'outages_closed'
    template_name = 'outages/outage_closedlist.html'

    def get_queryset(self):
        return Outage.objects.filter(status='closed')

    # Need to add LoginRequiredMixin to parent
    # def get(self, *args, **kwargs):
    #     """ Login will be required """
    #     if self.request.user != self.get_object().user:
    #         return HttpResponse(
    #             'You don\'t have permission to access this ITEM'
    #         )
    #     return super(OutageClosedView, self).get(*args, **kwargs)


class OutageDetailView(DetailView):
    """ Detail View of the outage. """
    model = Outage
    context_object_name = 'outage_detail'
    template_name = 'outages/outage_detail.html'

    def get(self, request, *args, **kwargs):
        detail = get_object_or_404(Outage, pk=kwargs['pk'])
        context = {'detail': detail}
        return render(request, 'outages/outage_detail.html', context)

# class OutageCreateView(LoginRequiredMixin, PageTitleMixin, CreateView):
#     fields = (
#         'isp_provider',
#         'issue_type',
#         'service_area',
#         'start_date',
#         'ccp_account_reference',
#         'status',
#     )
#     model = models.Outage
#     page_title = 'Add an outage'
#
#     def get_initial(self):
#         initial = super().get_initial()
#         initial['employee'] = self.request.user.pk
#         return initial
#
#
# class OutageUpdateView(LoginRequiredMixin, PageTitleMixin, UpdateView):
#     fields = (
#         'isp_provider',
#         'issue_type',
#         'service_area',
#         'start_date',
#         'ccp_account_reference',
#         'status',
#     )
#     model = models.Outage
#
#     def get_page_title(self):
#         obj = self.get_object()
#         return 'Updated {}'.format(obj.name)
#
#
# # In Progress
# class OutageDeleteView(LoginRequiredMixin, DeleteView):
#     model = models.Outage
#
#     def get_queryset(self):
#         if not self.request.user.is_superuser:
#             return self.model.objects.filter(outage=self.request.user)
#         return self.model.objects.all()

