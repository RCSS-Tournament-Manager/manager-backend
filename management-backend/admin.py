from django.contrib import admin

# from .models import CustomUser, RegistrationInvite


# @admin.register(CustomUser)
# class CustomUserAdmin(admin.ModelAdmin):
#     list_display = ["email", "is_approved"]
#     actions = ["approve_users"]

#     def approve_users(self, request, queryset):
#         queryset.update(is_approved=True)

#     approve_users.short_description = "Approve selected users"


# @admin.register(RegistrationInvite)
# class RegistrationInviteAdmin(admin.ModelAdmin):
#     list_display = ["email", "key", "message", "is_approved", "created_at"]
#     actions = ["approve_invites"]

#     def approve_invites(self, request, queryset):
#         for invite in queryset:
#             user, created = CustomUser.objects.get_or_create(
#                 email=invite.email, username=invite.email
#             )
#             user.is_approved = True
#             user.save()
#         queryset.update(is_approved=True)

#     approve_invites.short_description = "Approve selected invites"


# admin.site.register(CustomUser, CustomUserAdmin)
# admin.site.register(RegistrationInvite, RegistrationInviteAdmin)
