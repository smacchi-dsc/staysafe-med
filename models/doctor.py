from django.contrib.auth.models import User


class Doctor(User):
    class Meta:
        proxy = True

    def __str__(self):
        return '{} {}'.format(
            self.first_name,
            self.last_name
        )

    @property
    def ssnid(self):
        return self.username
