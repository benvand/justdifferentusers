justdifferentusers
==================

Small pluggable app to extend Django user model. Allows for adding new fields to user model by subclassing <br />
django.contrib.auth.models.AbstractUser.<br />
<br />
To use this app:<br />
<br />
path/to/project/project/settings.py<br />
```python
INSTALLED_APPS +=  ('justdifferentusers', )
AUTH_USER_MODEL = 'justdifferent.IQUser'
```

The (current) preferred method for extending the Django user<br />
model. We inherit from AbstractUser (as opposed to AbstractBaseUser)<br />
because we don't hate Django users we just think they should be <br />
bigger. And that's fine.<br />
The previous method was to attach a profile with USER_PROFILE_METHOD<br />
but this was deprecated in 1.5<br />

We let the Django user model provide the following attributes:<br />
>    username, first_name, last_name, email, password, groups, <br />
    user_permissions, is_staff, is_active, is_superuser, last_login,<br /> 
    date_joined<br />
    
And the following methods:<br />
>    is_anonymous(), is_authenticated(), get_full_name(), <br />
    set_password(raw_password), check_password(raw_password), <br />
    set_unusable_password(), has_usable_password(), <br />
    get_group_permissions(obj=None), get_all_permissions(obj=None), <br />
    has_module_perms(package_name), get_profile()<br />
    <br />
    
<Then add our extensions as model fields in the models.py<br />
<br />
I have left some in as demo fields. These are not depended upon.<br />
