from django.http import HttpResponse,HttpResponseNotFound,HttpResponsePermanentRedirect,HttpResponseRedirect
from django.http import  HttpResponseForbidden,HttpResponseBadRequest, JsonResponse
from django.core.serializers.json import DjangoJSONEncoder
from django.shortcuts import render
def index(request):
    data = {"header": "Hello Django", "message": "Welcome to Python"}
    return render(request,"index.html", context = data)
# # Create your views here.
# def index(request,id):
#         people = ["Farkhat", "Vadim","Rim"]
#         if id in range(0, len(people)):
#              return HttpResponse(people[id])
#         else:
#              return HttpResponseNotFound("Not Found")
# def access(request, age):
#      if age not in range(1,111):
#           return HttpResponseBadRequest("Некорректные данные")
#      if(age > 17):
#           return HttpResponse("Доступ аразрешен")
#      else:
#           return HttpResponseForbidden("Доступ заблоктрован: недостаточно лет")
# def index(request):
#      return JsonResponse({"name": "Tom", "age": 38})
# def index(request):
#      bob = Person("VADIM", 18)
#      return JsonResponse(bob, safe=False, encoder=PersonEncoder)
# class Person:
#     def __init__(self, name, age):
#         self.name = name 
#         self.age = age
# class PersonEncoder(DjangoJSONEncoder):
#     def default(self, obj):
#         if isinstance(obj, Person):
#             return {"name": obj.name, "age": obj.age}
#         return super().default(obj)

# def set(request):
#     Username = request.GET.get("username", "Undefined")
#     response = HttpResponse(f"Hello {Username}")
#     response.set_cookie("username", Username)
#     return response
# def get(request):
#     Username = request.COOKIES["username"]
#     return HttpResponse(F"Hello {Username}")


# def about(request,name,age):
#     return HttpResponse(f"""
#                         <h2>О пользователе</h2>
#                         <p>Имя: {name}</p>
#                         <p>Возвраст: {age}</p>
#     """)

# def contact(request):
#     return HttpResponse("<h2>СЕРЕЖА ВОППЕР: +79898883344<h2>")
#     # return HttpResponse("<h2>Контакты<h2>")

# def products(request, id):
#     return HttpResponse(f"Tovar {id}")

# def new(request):
#     return HttpResponse("Новые товары")

# def top(request):
#     return HttpResponse("Популярные товары")

# def comments (request, id):
#     return HttpResponse(f"Комментарии о товаре {id}")

# def questions(request, id):
#     return HttpResponse (f"Вопросы о товаре {id}")

# def user(request):
#     age = request.GET.get("age",0)
#     name = request.GET.get("name","Undefined")
#     return HttpResponse(f"<h2>Имя: {name} Возраст: {age}</h2>")
# def about(request,id):
#     people = ["Farkhat", "Vadim","Rim"]
#     return HttpResponse("About")
# def contact(request):
#     return HttpResponseRedirect("/about")
# def details(request):
#     return HttpResponsePermanentRedirect("/")

