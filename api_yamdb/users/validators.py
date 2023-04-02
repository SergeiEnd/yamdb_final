from re import match

from django.core.exceptions import ValidationError


def validate_username(value):
    if value != 'me' and match(r'[\w]', value):
        return value
    raise ValidationError('Некорректный username')
