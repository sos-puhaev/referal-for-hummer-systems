from django.http import JsonResponse
from django.shortcuts import redirect
from django.views.generic import TemplateView
from ..models.user_models import User
import random
import string
from django.urls import reverse
from django.contrib.sessions.models import Session

class HomeView(TemplateView):
    template_name = 'home.html'

    def post(self, request, *args, **kwargs):
        form_type = request.POST.get('formType')

        if form_type == 'phoneForm':
            phone_number = request.POST.get('tel')

            try:
                user = User.objects.get(telephone=phone_number)
                if user.status_auth:
                    request.session['is_authenticated'] = True
                    request.session['phone_number'] = phone_number
                    return JsonResponse({'auth': True})
                else:
                    random_number = random.randint(1000, 9999)
                    user.temporary_code = random_number
                    user.save()
                    return JsonResponse({'cod': user.temporary_code})
            except User.DoesNotExist:
                random_number = random.randint(1000, 9999)
                user = User.objects.create(telephone=phone_number, status_auth=False, temporary_code=random_number)
                return JsonResponse({'cod': user.temporary_code})
            
        elif form_type == 'confirmationForm':
            auth_cod = request.POST.get('auth_cod')
            phone_number = request.POST.get('telephone')

            try:
                user = User.objects.get(telephone=phone_number)
                if user.temporary_code == auth_cod:
                    user.status_auth = True
                    user.personal_invite = self.generate_code()
                    user.save()
                    request.session['is_authenticated'] = True
                    request.session['phone_number'] = phone_number
                    return JsonResponse({'auth': True})
                else:
                    return JsonResponse({'error': 'Неверный код подтверждения.'})
            except User.DoesNotExist:
                return JsonResponse({'error': 'Пользователь с таким номером телефона не найден.'})
            
        else:
            return JsonResponse({'error': 'Неизвестный тип формы.'})
        
    def generate_code(self):
        characters = string.ascii_letters + string.digits
        code = ''.join(random.choice(characters) for _ in range(6))
        return code
        