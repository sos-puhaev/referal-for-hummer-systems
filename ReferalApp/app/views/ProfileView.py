from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.views.generic import TemplateView
from ..models.user_models import User
from ..models.invite_cods import BindingInvite

class ProfileView(TemplateView):
    template_name = 'profile.html'

    def dispatch(self, request, *args, **kwargs):
        if not request.session.get('is_authenticated'):
            return HttpResponseRedirect(reverse('home_view'))
        
        phone_number = request.session.get('phone_number')

        try:
            user = User.objects.get(telephone=phone_number)
            return super().dispatch(request, user=user, *args, **kwargs)
        except User.DoesNotExist:
            return HttpResponseRedirect(reverse('home_view'))
    
    def post(self, request, *args, **kwargs):
        invait_value = request.POST.get('invait')
        phone_number = request.session.get('phone_number')

        try:
            check_invaite = User.objects.filter(personal_invite=invait_value)
            if check_invaite.exists():
                user = User.objects.get(telephone=phone_number)
                if user.activate_invait:
                    return JsonResponse({'message': "Вы уже активировали инвайт."})
                else:
                    user.activate_invait = True
                    user.telephone_invait = invait_value
                    binding_invite = BindingInvite.objects.create(telephone=phone_number, invite_cod=invait_value)
                    user.save()
                    binding_invite.save()
                    return JsonResponse({'message': "Инвайт активирован."})
            else:
                return JsonResponse({'message': 'Телефон с подобным инвайт кодом не найден.'})
        except:
            return JsonResponse({'message': 'Ошибка подключения!'})