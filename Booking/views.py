from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Booking
from django.core.mail import send_mail
from django.conf import settings
from django.shortcuts import render
from django.contrib import messages
from .models import Booking

# Create your views here.


def showbooking(request):
    template = loader.get_template("booking.html")
    return HttpResponse(template.render())


def booking_view(request):
    event_price = request.GET.get("event_price", "") 
    if event_price:
        event_price = event_price.replace("SR", "").strip()  # إزالة "SR" من السعر

    context = {
        "event_id": request.GET.get("event_id"),
        "event_name": request.GET.get("event_name"),
        "event_title": request.GET.get("event_title"),
        "event_description": request.GET.get("event_description"),
        "event_price": event_price, 
        "event_image": request.GET.get("event_image"),  # ← هذا مهم
    }
    return render(request, "booking.html", context)


def booking_submit(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        event = request.POST.get("event")
        event_title = request.POST.get("event_title")
        event_id = request.POST.get("event_id")
        date = request.POST.get("date")
        event_price = request.POST.get("event_price")

        # حفظ البيانات
        Booking.objects.create(
            name=name,
            email=email,
            event=event,
            event_title=event_title,
            event_id=event_id,
            date=date,
            event_price=event_price,
        )
        # إرسال البريد الإلكتروني إلى المستخدم
        subject = f"تم تأكيد حجزك لفعالية {event}"
        message = f"""
        <html>
            <body style="direction: rtl; font-family: Arial, sans-serif;">
                <p>مرحباً {name},</p>
                <p>تم تأكيد حجزك لفعالية <strong>{event}</strong>🎉</p>
                <p><strong>التفاصيل:</strong></p>
                <ul>
                    <li><strong>المدينة:</strong> {event}</li>
                    <li><strong>الفئة:</strong> {event_title}</li>
                    <li><strong>التاريخ:</strong> {date}</li>
                    <li><strong>السعر:</strong> {event_price} ريال</li>
                    
                <p>شكراً لك على حجزك معنا!</p>
                <p>إذا كان لديك أي استفسارات، لا تتردد في التواصل معنا.</p>
                <p>مع تحياتنا،</p>
                </ul>
            </body>
        </html>
        """
        from_email = settings.EMAIL_HOST_USER  # البريد الإلكتروني الذي سترسل منه
        recipient_list = [email]  # البريد الإلكتروني للمستقبل

        # إرسال البريد الإلكتروني
        send_mail(subject, message, from_email, recipient_list, html_message=message)

        # عرض رسالة نجاح في الموقع
        messages.success(
            request, "تم الحجز بنجاح! وتم إرسال رسالة تأكيد إلى بريدك الإلكتروني"
        )

        # إعادة التوجيه إلى صفحة الحجز الناجح
        return render(request, "Booking/booking_success.html")

    return redirect("home")  # إذا لم تكن الطريقة POST
