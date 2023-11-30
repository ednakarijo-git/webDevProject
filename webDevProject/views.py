from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Membership


def home(request):
    return render(request, 'index.html')


def request_membership(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        status = "0"

        membership = Membership(name=name, email=email, subject=subject, message=message, status=status)
        membership.save()
        messages.success(request, 'Membership requested successfully')
        return redirect('home-url')
    return render(request, 'index.html')


def membership_requests(request):
    memberships = Membership.objects.all()
    return render(request, 'membership-requests.html', {'memberships': memberships})


def delete(request, id):
    membership = Membership.objects.get(id=id)
    membership.delete()
    messages.success(request, 'Membership deleted successfully')
    return redirect('membership_requests_url')


def status(request, id):
    membership = Membership.objects.get(id=id)
    if membership.status == "0":
        membership.status = "1"
    else:
        membership.status = "0"
    membership.save()
    messages.success(request, 'Membership status changed successfully')
    return redirect('membership_requests_url')
