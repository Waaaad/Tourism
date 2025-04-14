from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.templatetags.static import static
# Create your views here.


def list(request):
    city = [ 
        {
            "id": 1,
            "name": "الدمام",
            "title": "أماكن تراثية وتاريخية",
            "description": "مهرجان أفلام السعودية",
            "image": static("explore-img/فعاليات الدمام.png"),  # ← هذا المسار الصح
            "link": "#",
            "button": "أحجز الان",
            "price": "250 SR",
        },
        {
            "id": 2,
            "name": "الرياض",
            "title": "الرياضة",
            "description": "الجائزة الكبرى لمجلس الملاكمة العالمي",
            "image": static("explore-img/ملاكمة.png"),
            "link": "#",
            "button": "أحجز الان",
            "price": "150 SR",
        },
        {
            "id": 3,
            "name": "جدة",
            "title": "أماكن تراثية وتاريخية",
            "description": "مهرجان أفلام السعودية",
            "image": static("explore-img/جده.png"),
            "link": "#",
            "button": "أحجز الان",
            "price": "300 SR",
        },
        {
            "id": 4,
            "name": "الرياض",
            "title": "مغامرة",
            "description": "بوليفارد وورلد",
            "image": static("explore-img/بوليفارد رياض.png"),
            "link": "#",
            "button": "أحجز الان",
            "price": "50 SR",
        },
        {
            "id": 5,
            "name": "الجوف",
            "title": " أماكن تراثية وتاريخية",
            "description": "بحيرة دومة الجندل",
            "image": static("explore-img/بحيرة دومة.png"),
            "link": "#",
            "button": "أحجز الان",
            "price": "50 SR",
        },
        {
            "id": 6,
            "name": "تبوك",
            "title": "أماكن تراثية وتاريخية",
            "description": "أملج",
            "image": static("explore-img/املج.jpg"),
            "link": "#",
            "button": "أحجز الان",
            "price": "50 SR",
        },
    ]
    
    

    context = {"city": city}

    template = loader.get_template("explore.html")
    return HttpResponse(template.render(context, request))
