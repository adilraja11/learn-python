from django.shortcuts import render

# Create your views here.
def index_view(request):
    # nations = ["Indonesia", "Australia", "Malaysia", "India", "Spain"]
    nations = []
    return render(request, "index.html", { "nations": nations })
