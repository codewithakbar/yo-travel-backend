from django.shortcuts import get_object_or_404, render

from home.forms import BookingForm, ContactForm

from .models import PriceExludesInlines, PriceIncludesInlines, TurImagesInlines, TurPaketlar, Manzillar

def index(request):

    context = {
        "tur_paketla": TurPaketlar.objects.all()[:8],
        "manzillar": Manzillar.objects.all().order_by("?")
    }
    return render(request, "index.html", context=context)


def tur(request):

    context = {
        "tur_paketla": TurPaketlar.objects.all().order_by("-id"),
    }

    return render(request, "tour.html", context=context)


def about(request):

    return render(request, "about.html")


def contact(request):

    session_key = request.session.session_key
    if not session_key:
        request.session.save()
        session_key = request.session.session_key

    form_submissions_count = request.session.get(f'form_submissions_{session_key}', 0)

    if request.method == 'POST':
        if form_submissions_count < 6:
            form = ContactForm(request.POST)
            if form.is_valid():
                contact = form.save(commit=False)
                contact.save()

                form_submissions_count += 1
                request.session[f'form_submissions_{session_key}'] = form_submissions_count
    else:
        form = ContactForm() if form_submissions_count < 6 else None
    context = {
        "form": form,
    }
    return render(request, "contact.html", context=context)





def tur_detail(request, slug):
    tur_paket = get_object_or_404(TurPaketlar, slug=slug)

    session_key = request.session.session_key
    if not session_key:
        request.session.save()
        session_key = request.session.session_key

    form_submissions_count = request.session.get(f'form_submissions_{session_key}', 0)

    if request.method == 'POST':
        if form_submissions_count < 6:
            form = BookingForm(request.POST, tur_paket=tur_paket)
            if form.is_valid():
                booking = form.save(commit=False)
                booking.tour = tur_paket
                booking.save()




                form_submissions_count += 1
                request.session[f'form_submissions_{session_key}'] = form_submissions_count
    else:
        form = BookingForm(tur_paket=tur_paket) if form_submissions_count < 6 else None

    includes = PriceIncludesInlines.objects.filter(tur=tur_paket)
    excludes = PriceExludesInlines.objects.filter(tur=tur_paket)
    images = TurImagesInlines.objects.filter(product=tur_paket)

    context = {
        "tur_paket": tur_paket,
        "includes": includes,
        "excludes": excludes,
        "images": images,
        "form": form,
        "form_submissions_count": form_submissions_count,
    }

    return render(request, "tour-details.html", context=context)
