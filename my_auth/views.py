
from django.views.generic import View

# Create your views here.
class UserControl(View):

    def post(self,request,*args,**kwargs):
        #get the operation
        slug = self.kwargs.get('slug')
        print(slug)

        if 'register' == slug:
            return self.register(request)

    def register(self,request):
        username = self.request.POST.get("username","")
        email = self.request.POST.get("email","")
        password1 = self.request.POST.get("password1","")
        password2 = self.request.POST.get("password2", "")

        print(username,email)
        print(password1,password2)