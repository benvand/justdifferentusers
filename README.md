justdifferentusers
==================

Small pluggable app to extend Django user model. Allows for adding new fields to user model by subclassing 
django.contrib.auth.models.AbstractUser.

To use this app:
INSTALLED_APPS +=  ('justdifferentusers', )
AUTH_USER_MODEL = 'justdifferent.IQUser'



  !!! To use this guy we need to put:
        AUTH_USER_MODEL = 'justdifferent.IQUser'
  !!! in our settings.py

    Above is the (current) preferred method for extending the Django user 
    model. We inherit from AbstractUser (as opposed to AbstractBaseUser)
    because we don't hate Django users we just think they should be 
    bigger. And that's fine.
    The previous method was to attach a profile with USER_PROFILE_METHOD
    but this was deprecated in 1.5
    
    We let the Django user model provide the following attributes:
        username, first_name, last_name, email, password, groups, 
        user_permissions, is_staff, is_active, is_superuser, last_login, 
        date_joined
    And the following methods:
        is_anonymous(), is_authenticated(), get_full_name(), 
        set_password(raw_password), check_password(raw_password), 
        set_unusable_password(), has_usable_password(), 
        get_group_permissions(obj=None), get_all_permissions(obj=None), 
        has_module_perms(package_name), get_profile()
        
    Then add our extensions as model fields in the models.py
    
    I have left some in as demo fields. These are not depended upon.
