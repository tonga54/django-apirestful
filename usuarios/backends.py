from usuarios.models import Usuario


class EmailBackend(object):

    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = Usuario.objects.get(email = username)
        except Usuario.MultipleObjectsReturned:
            user = Usuario.objects.filter(email=username).order_by('id').first()
        except Usuario.DoesNotExist:
            return None

        if getattr(user, 'is_active') and user.check_password(password):
            return user
        return None

    def get_user(self, user_id):
        try:
            return Usuario.objects.get(pk=user_id)
        except Usuario.DoesNotExist:
            return None