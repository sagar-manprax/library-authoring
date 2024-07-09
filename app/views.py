from django.http import (JsonResponse)
from rest_framework.decorators import api_view
from time import time
from django.conf import settings
import jwt
from lms.djangoapps.mobile_api.decorators import mobile_view
from django.contrib.sites.models import Site
from openedx.core.djangoapps.site_configuration.models import SiteConfiguration

@api_view(['GET','POST'])
@mobile_view()
def import_library(request):
    return JsonResponse(data={"message":"Testing"})