from django.conf import settings
from django import forms
from django.utils.encoding import smart_unicode
from django.utils.translation import ugettext_lazy as _

from recaptcha.client import captcha

from captcha.widgets import ReCaptcha


class ReCaptchaField(forms.CharField):

    default_error_messages = {
        'captcha_invalid': _(u'The text you entered did not match, please try '
                              'again.')
    }

    def __init__(self, *args, **kwargs):
        public_key = kwargs.pop('public_key', None) \
                    or getattr(settings, 'RECAPTCHA_PUBLIC_KEY', None)

        self.private_key = kwargs.pop('private_key', None) \
                    or getattr(settings, 'RECAPTCHA_PRIVATE_KEY', None)

        use_ssl = kwargs.pop('use_ssl', False) \
                    or getattr(settings, 'RECAPTCHA_USE_SSL', False)

        self.widget = ReCaptcha(public_key = public_key, use_ssl = use_ssl)
        self.required = True
        super(ReCaptchaField, self).__init__(*args, **kwargs)

    def clean(self, values):
        super(ReCaptchaField, self).clean(values[1])
        recaptcha_challenge_value = smart_unicode(values[0])
        recaptcha_response_value = smart_unicode(values[1])
        check_captcha = captcha.submit(recaptcha_challenge_value,
            recaptcha_response_value, self.private_key, {})
        if not check_captcha.is_valid:
            raise forms.util.ValidationError(
                    self.error_messages['captcha_invalid'])
        return values[0]

