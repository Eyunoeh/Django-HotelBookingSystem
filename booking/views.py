from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import CheckIn, CheckOut
from django.shortcuts import render
from django.contrib import messages
from django.shortcuts import redirect
from time import sleep


def home_page(request):
    sleep(2)
    return render(request, 'booking/landing-page.html')


def book_now(request):
    sleep(2)
    return redirect('book')


def book(request):
    template = loader.get_template('booking/checkIN.html')
    return HttpResponse(template.render({}, request))


def thankyouPage(request):
    code = request.session['code']
    return render(request, 'booking/thankyou.html', {"code": code})


def checkIns(request):
    import random
    record_checkins = CheckIn.objects.values_list('code', flat=True)
    record_checkouts = CheckOut.objects.values_list('code', flat=True)

    if request.method == 'POST':
        f_name = request.POST['f_name']
        l_name = request.POST['l_name']
        address = request.POST['address']
        contact_num = request.POST['c_number']
        email = request.POST['c_email']
        guest_num = request.POST['g_number']
        check_in = request.POST['check_in']
        check_out = request.POST['check_out']
        while True:
            generated_code = ""
            rand_code = random.randrange(111111, 999999)
            str_rand_code = str(rand_code)
            generated_code += str_rand_code
            if generated_code not in record_checkins not in record_checkouts:
                check_n = CheckIn(first_name=f_name, last_name=l_name, address=address,
                                  contact_number=contact_num, email=email, guest_number=guest_num,
                                  checkIns=check_in, checkOut=check_out, code=generated_code)
                check_n.save()

                sleep(2)
                break

        chk_code = CheckIn.objects.get(code=generated_code)
        cd = chk_code.code
        request.session['code'] = cd
        return redirect('thankyou')


def checkout(request):
    template = loader.get_template('booking/CheckOut.html')
    return HttpResponse(template.render({}, request))


def update_delete_data(request):
    if request.method == 'POST':
        try:
            primary_key = request.POST.get('code')
            check_in = CheckIn.objects.get(code=primary_key)
            check_out = CheckOut(first_name=check_in.first_name, last_name=check_in.last_name,
                                 address=check_in.address, contact_number=check_in.contact_number,
                                 email=check_in.email, guest_number=check_in.guest_number, checkIns=check_in.checkIns,
                                 checkOut=check_in.checkOut, code=check_in.code)
            check_out.save()
            from time import sleep
            check_in.delete()
            sleep(3)
            messages.success(request, 'Record was deleted successfully.')
            return HttpResponseRedirect(reverse('checkout'))
        except CheckIn.DoesNotExist:
            messages.error(request, 'Invalid code.')
            from time import sleep
            sleep(2)
            return HttpResponseRedirect(reverse('checkout'))
