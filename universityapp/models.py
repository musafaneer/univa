from django.db import models

class Student(models.Model):
    UNDERGRAD = 'UG'
    MASTER = 'MS'
    DOCTORATE = 'DR'
    DEGREE_LEVELS = [
        (UNDERGRAD, 'Undergraduate'),
        (MASTER, 'Master'),
        (DOCTORATE, 'Doctorate'),
    ]

    user = models.OneToOneField('auth.User', on_delete=models.CASCADE)
    degree_level = models.CharField(max_length=2, choices=DEGREE_LEVELS, default=UNDERGRAD)
    enrollment_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user.get_full_name()