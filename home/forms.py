from django import forms
from .models import Booking, Contact, TurPaketlar

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['full_name', 'email', 'phone', 'date', 'tour']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'contacts-name input-wrapper', 'placeholder': 'F.I.O'}),
            'email': forms.EmailInput(attrs={'class': 'contacts-email input-wrapper', 'placeholder': 'Email pochta'}),
            'phone': forms.TextInput(attrs={'class': 'contacts-phone input-wrapper', 'placeholder': 'Telefon raqam'}),
            'date': forms.DateInput(attrs={'type': 'date'}),
            'tour': forms.TextInput(attrs={'class': 'contacts-tour input-wrapper', 'placeholder': 'Tour', 'readonly': 'readonly'}),
        }

    def __init__(self, *args, tur_paket=None, **kwargs):
        super(BookingForm, self).__init__(*args, **kwargs)
        self.fields['tour'].initial = tur_paket
        self.fields['tour'].widget = forms.HiddenInput()


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['full_name', 'email', 'phone', 'mavzu', 'comment']
        widgets = {
            'full_name': forms.TextInput(attrs={'placeholder': 'F.I.O'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email pochta'}),
            'phone': forms.TextInput(attrs={'placeholder': 'Telefon raqam'}),
            'mavzu': forms.DateInput(attrs={'placeholder': 'Mavzu nima haqida?'}),
            'comment': forms.Textarea(attrs={'placeholder': 'Sizni qiynayatgan savolni shu yerga yozing'}),
        }