from django.views.generic import ListView, DetailView
from apps.profiles.models import Profile


class EmployeeListView(ListView):
    model = Profile
    template_name = "profile_list.html"
    context_object_name = "profiles"
    paginate_by = 1

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Ini List Pekerja'
        return context

class EmployeeDetailView(DetailView):
    model = Profile
    template_name = "profile_detail.html"
    context_object_name = "profile"
    slug_field = "id"
    slug_url_kwarg = "id"