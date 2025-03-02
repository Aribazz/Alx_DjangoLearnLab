from django.views.generic import TemplateView 
from django.contrib.auth.mixin import UserPassesTestMixin

class AdminView(UserPassesTestMixin,TemplateView):
    template_name = "relationship_app/admin_view.html"

def test_func(self):
    return self.request.user.userprofile.role == "Admin"
