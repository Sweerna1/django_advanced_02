from django.shortcuts import render, redirect
from .models import Store
from .forms import StoreModelForm

# Create your views here.
def store_list(request):
    context = {
        "stores": Store.objects.all()
    }
    return render(request, 'store_list.html', context)

def store_detail(request, store_slug):
	store = Store.objects.get(slug=store_slug)
	context = {
		"store": store,
	}
	return render(request, 'detail.html', context)


def create_store(request):
	form = StoreModelForm()
	if request.method == "POST":
		form = StoreModelForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('list')
	context = {
		"form":form,
	}
	return render(request, 'create.html', context)

