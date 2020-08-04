from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.generic import View

from .forms import PostForm, PostFormFromModel

# Create your views here.


class InfoView(View):
    template_name = 'blogs/info.html'

    def get(self, request):
        return render(request, self.template_name)


def get_post_data(request):
    if request.method == "POST":
        form = PostFormFromModel(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/info/')
    else:
        form = PostFormFromModel()
    return render(request, 'blogs/create_post.html', {'form': form})



