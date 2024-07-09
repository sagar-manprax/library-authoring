"""
Otp API Configuration
"""


from django.apps import AppConfig
from edx_django_utils.plugins import PluginURLs, PluginSettings
from django.conf import settings

from openedx.core.djangoapps.plugins.constants import ProjectType, SettingsType

class AppConfig(AppConfig):
    """
    Application Configuration for app
    """
    name = 'app'
    label='app'
    plugin_app = {
        PluginURLs.CONFIG: {
            ProjectType.LMS: {
                PluginURLs.NAMESPACE: 'app',
                PluginURLs.REGEX: '^api/mx/',
                PluginURLs.RELATIVE_PATH: 'urls',
            }
        }
    }