from django.contrib import admin
from .models import About_pwares
from .models import Pwares_ratings
from .models import Pwares_services
from .models import Pwares_portfolio
from .models import Pwares_testimonials
from .models import Pwares_updates
from .models import Pwares_contacts
# Register your models here.

admin.site.register(About_pwares)
admin.site.register(Pwares_ratings)
admin.site.register(Pwares_services)
admin.site.register(Pwares_portfolio)
admin.site.register(Pwares_testimonials)
admin.site.register(Pwares_updates)
admin.site.register(Pwares_contacts)
