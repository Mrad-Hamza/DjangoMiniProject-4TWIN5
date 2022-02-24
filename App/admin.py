from pyexpat.errors import messages

from django.contrib import admin

# Register your models here.
from App.models import Etudiant, Projet, Coach, MemberShipInProject


class Membership(admin.TabularInline):
    model=MemberShipInProject
    extra = 1


@admin.register(Projet)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('nom_projet', 'duree_projet',
                    'temps_alloue_createur', 'est_valide', 'createur')

    def set_to_valid(self, request, queryset):
        queryset.update(est_valide=True)

    def set_to_no_valid(self, request, queryset):
        row = queryset.filter(est_valide=False)
        if row.count() > 0:
            messages.error(request, "%s projet invalide" % row.count())
        else:
            row_update=queryset.update(est_valide=False)
            if row_update==1:
                message="1 project was updated"
            else:
                message="%s projects were updated" % row_update
            self.message_user(request, message)

    actions = ['set_to_valid','set_to_no_valid']
    set_to_valid.short_description = "Valider"
    set_to_no_valid.short_description = "Invalider"
    fieldsets = (('Informations generales', {'fields':('nom_projet', 'description', 'besoins', 'createur','superviseur',)}),
    ('Etat', {'fields':('est_valide',)}),
    ('Duréé', {'fields':('duree_projet', 'temps_alloue_createur',)}))
    inlines = (Membership,)
    list_filter = ('nom_projet','est_valide')
    list_per_page = 1
    search_fields = ['nom_projet']

admin.site.register(Etudiant)
admin.site.register(Coach)
