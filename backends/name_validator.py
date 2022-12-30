from rest_framework.validators import ValidationError

def name_valid(value):
    not_required = ['not', 'fuck', 'dick', 'sex', 'pusy', 'transgender', 'gay', 'pornhub', 'lesbian']
    if value in not_required:
        raise ValidationError("name can't support our privacy policy ")
    if len(value) < 4:
        raise ValidationError('name is too short 4-8 charecter length ')
    if len(value):
        raise ValidationError('name is too long 4-8 charecter length')

    return value
