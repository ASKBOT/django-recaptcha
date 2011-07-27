Inspired by
===========
Marco Fucci @ http://www.marcofucci.com/tumblelog/26/jul/2009/integrating-recaptcha-with-django/

Usage
=====
Register your site at recaptcha.net, obtain public and private keys.

Decide whether you want to put your recaptcha keys in the django's
``settings.py`` or initialize the field at run time.

If you wish to use ``settings.py`` - then add::

    RECAPTCHA_PUBLIC_KEY = '...'#the public key
    RECAPTCHA_PRIVATE_KEY = '...'#the private key

Otherwise, add the keys as parameters ``public_key`` and ``private_key``
to the field, as shown in the second example below.

Add ``ReCaptchaField`` to some form::

    from django import forms
    from captcha.fields import ReCaptchaField

    class MyForm(forms.Form):
        recaptcha = ReCaptchaField()#use settings.py
        #.. or, if using run time configuration:
        recaptcha = ReCaptchaField(public_key = '...', private_key = '...')

SSL support
===========
This version requires a custom version of the python-recaptcha library to provide ssl support for submit.
You can get the required version here:

http://github.com/bltravis/python-recaptcha

Add a new setting to your Django project settings file (eg.):

RECAPTCHA_USE_SSL = True

or initialize the field with ``use_ssl = True``

If you don't add this setting, the code is written to default to **NOT** use SSL.
