from django.shortcuts import render

# Create your views here.
def index_view(request):
    context = {
        "name": "John Doe",
        "age": 25,
        "is_single": True,
        "hobbies": ["Reading", "Gaming", "Coding"],
        "address": {
            "street": "Jl. Jend. Sudirman",
            "city": "Jakarta",
            "zip": "12345"
        }
    }
    # nations = ["Indonesia", "Australia", "Malaysia", "India", "Spain"]
    # nations = []
    return render(request, "index.html", context)
# { "nations": nations }
