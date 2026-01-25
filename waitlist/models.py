from django.db import models


class WaitlistEntry(models.Model):
    email = models.EmailField(unique=True, max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Waitlist Entry'
        verbose_name_plural = 'Waitlist Entries'
        ordering = ['-created_at']

    def __str__(self):
        return self.email
