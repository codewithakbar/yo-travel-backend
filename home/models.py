from django.db import models
from django.utils.translation import gettext_lazy as _

from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel

from ckeditor.fields import RichTextField



class Manzillar(MPTTModel):

    title = models.CharField(max_length=255, verbose_name="Manzil Nomi", null=True, blank=True)
    image = models.ImageField(upload_to='manzillar/%Y/%m/%d', null=True, blank=True, verbose_name="Manzil Surati")
    slug = models.SlugField(null=True, blank=True, unique=True)

    parent = TreeForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='children')

    def __str__(self) -> str:
        return self.image.path

    class Meta:
        verbose_name = "Manzil Qoshish"
        verbose_name_plural = "Manzillar Qoshish"


class TurPaketlar(MPTTModel):

    title = models.CharField(max_length=255, verbose_name="Tur Nomi")
    image = models.ImageField(upload_to='tur_paket/%Y/%m/%d', verbose_name="Tur Surati")
    price = models.DecimalField(max_digits=11,decimal_places=0, default=0, blank=True, null=True, verbose_name="Tur Narxi")
    location = models.CharField(max_length=255, verbose_name="Tur Manzili")
    kuni = models.IntegerField(default=0)
    desc = RichTextField()
    slug = models.SlugField(null=True, unique=True)

    parent = TreeForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='children')

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = "Tur Paket Qoshish"
        verbose_name_plural = "Tur Paketlar Qoshish"

class Booking(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    date = models.DateField()
    tour = models.CharField(max_length=255)
    # tour = models.ForeignKey(to=TurPaketlar, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.full_name} - {self.tour}"

    class Meta:
        verbose_name = "Bron Qilgan Foydalanuvchi"
        verbose_name_plural = "Bron Qilganlar"


class Contact(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    mavzu = models.CharField(max_length=255)
    # comment = RichTextField()
    comment = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.full_name} - {self.comment}"

    class Meta:
        verbose_name = "Aloqaga Chiqqan Foydalanuvchi"
        verbose_name_plural = "Aloqaga Chiqqanlar"


class PriceIncludesInlines(models.Model):
    tur = models.ForeignKey(to=TurPaketlar, related_name='tur_narxiga_kiruvchi', on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=232)

    class Meta:
        verbose_name = _('Tur Narxiga kiradi')
        verbose_name_plural = _('Tur Narxiga kiradi')


class PriceExludesInlines(models.Model):
    tur = models.ForeignKey(to=TurPaketlar, related_name='tur_narxiga_chiquvchi', on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=232)

    class Meta:
        verbose_name = _('Tur Narxiga kirmaydi')
        verbose_name_plural = _('Tur Narxiga kirmaydi')


class TurImagesInlines(models.Model):
    product = models.ForeignKey(TurPaketlar, default=None, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='tur_images/%Y/%m/%d', blank=True, null=True)

    class Meta:
        verbose_name = _('Tur Qoshimcha Surati')
        verbose_name_plural = _('Turga Qoshimcha Suratlari')

