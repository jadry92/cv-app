
# Django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import FormView
from django.http import HttpResponse

# Models
from cv.models import CV

# Form
from ai.forms import AskForm


class AskView(LoginRequiredMixin, FormView):
    template_name = "semantic_kernel/ask.html"
    form_class = AskForm
    success_url = reverse_lazy("sk:ask")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cv = CV.objects.filter(user=self.request.user).first()
        context["text"] = cv.get_cv_str()
        return context

    def form_valid(self, form):
        context = self.get_context_data()
        context["text"] = form.cleaned_data["text"]
        return self.render_to_response(context)

    def form_invalid(self, form):
        return super().form_invalid(form)


def foo(request):
    return HttpResponse(f"Hello,{request.user.username}")

