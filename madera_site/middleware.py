# -*- coding: utf-8 -*-

from .models import Profile

class CheckProfile:
    def process_request(self, request):
        if request.user.is_authenticated():
            try:
                request.user.get_profile()
            except Profile.DoesNotExist:
                Profile.objects.create(user=request.user)