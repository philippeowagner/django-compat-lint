def check_duplicate_username(line, filename, options):
    warnings = []
    if 'duplicate_username' in line:
        warnings.append("UserCreationForm.errors_messages['duplicate_username'] is no longer used. If you wish to customize that error message, override it on the form using the 'unique' key in Meta.errors_messages['username'] or, if you have a custom form field for 'username', using the the 'unique' key in its error_messages argument.")
    return warnings, [], []


def check_app_name(line, filename, options):
    warnings = []
    if 'app_name=' in line:
        warnings.append('AdminSite no longer takes an app_name argument and its app_name attribute has been removed. The application name is always admin (as opposed to the instance name which you can still customize using AdminSite(name="...").')
    return warnings, [], []


def check_cache_class(line, filename, options):
    errors = []
    if 'CacheClass' in line:
        errors.append("The CacheClass shim has been removed from all cache backends. These aliases were provided for backwards compatibility with Django 1.3. If you are still using them, please update your project to use the real class name found in the BACKEND key of the CACHES setting.")
    return [], errors, []


def check_complie_string(line, filename, options):
    errors = []
    if 'compile_string' in line:
        errors.append('Private API django.template.compile_string was removed.')
    return [], errors, []


def check_override_template(line, filename, options):
    errors = []
    if 'override_template_loaders' in line or 'override_with_test_loader' in line:
        errors.append('Private APIs override_template_loaders and override_with_test_loader in django.test.utils were removed. Override TEMPLATE_LOADERS with override_settings instead.')
    return [], errors, []


def check_future(line, filename, options):
    warnings = []
    if '{% load cycle from future %}' in line or '{% load firstof from future %}' in line:
        warnings.append('Django 1.6 introduced {% load cycle from future %} and {% load firstof from future %} syntax for forward compatibility of the cycle and firstof template tags. This syntax is now deprecated and will be removed in Django 2.0. You can simply remove the {% load ... from future %} tags.')
    return [], warnings, []


def check_patterns(line, filename, options):
    warnings = []
    if 'patterns(' in line:
        warnings.append('django.conf.urls.patterns() is deprecated and will be removed in Django 2.0. Update your urlpatterns to be a list of django.conf.urls.url() instances instead.')
    return warnings, [], []


def check_noargs(line, filename, options):
    warnings = []
    if 'NoArgsCommand' in line:
        warnings.append('The class NoArgsCommand is now deprecated and will be removed in Django 2.0. Use BaseCommand instead, which takes no arguments by default.')
    return warnings, [], []


def check_resolve_variable(line, filename, options):
    warnings = []
    if 'resolve_variable' in line:
        warnings.append('django.template.resolve_variable() has been informally marked as Deprecated for some time. Replace resolve_variable(path, context) with django.template.Variable(path).resolve(context).')
    return warnings, [], []


def check_webdesign(line, filename, options):
    warnings = []
    if 'django.contrib.webdesign' in line:
        warnings.append("django.contrib.webdesign provided the lorem template tag which is now included in the built-in tags. Simply remove 'django.contrib.webdesign' from INSTALLED_APPS and {% load webdesign %} from your templates.")
    return warnings, [], []


def check_error_message(line, filename, options):
    warnings = []
    if 'error_message=' in line:
        warnings.append("error_message argument to django.forms.RegexField provided backwards compatibility for pre-1.0 code, but its functionality is redundant. Use Field.error_messages['invalid'] instead.")
    return warnings, [], []


def check_has_changed(line, filename, options):
    warnings = []
    if '_has_changed' in line:
        warnings.append('django.forms.Field._has_changed() Rename this method to has_changed() by removing the leading underscore. The old name will still work until Django 2.0.')
    return warnings, [], []


def check_remove_tags(line, filename, options):
    warnings = []
    if 'remove_tags' in line or 'removetags' in line or 'strip_entities' in line:
        warnings.append('django.utils.html.remove_tags() as well as the template filter removetags have been deprecated as they cannot guarantee safe output. Their existence is likely to lead to their use in security-sensitive contexts where they are not actually safe. The unused and undocumented django.utils.html.strip_entities() function has also been deprecated.')
    return warnings, [], []


def check_is_admin_site(line, filename, options):
    warnings = []
    if 'is_admin_site' in line:
        warnings.append("is_admin_site argument to django.contrib.auth.views.password_reset() It's a legacy option that should no longer be necessary.")
    return warnings, [], []


def check_subfieldbase(line, filename, options):
    warnings = []
    if 'SubfieldBase' in line:
        warnings.appned('django.db.models.fields.subclassing.SubfieldBase has been deprecated and will be removed in Django 2.0. Historically, it was used to handle fields where type conversion was needed when loading from the database, but it was not used in .values() calls or in aggregates. It has been replaced with from_db_value(). Note that the new approach does not call the to_python() method on assignment as was the case with SubfieldBase.')
    return warnings, [], []


def check_checksums(line, filename, options):
    warnings = []
    if 'django.utils' in line and 'checksums' in line:
        warnings.append('The django.utils.checksums module has been deprecated and will be removed in Django 2.0. The functionality it provided (validating checksum using the Luhn algorithm) was undocumented and not used in Django. The module has been moved to the django-localflavor package (version 1.1+).')
    return warnings, [], []


def check_original_content_type_id(line, filename, options):
    warnings = []
    if 'original_content_type_id' in line:
        warnings.append('The original_content_type_id attribute on InlineAdminForm has been deprecated and will be removed in Django 2.0. Historically, it was used to construct the "view on site" URL. This URL is now accessible using the absolute_url attribute of the form.')
    return warnings, [], []


def check_base_loader(line, filename, options):
    warnings = []
    if 'BaseLoader' in line:
        warnings.appned("django.template.loader.BaseLoader was renamed to django.template.loaders.base.Loader. If you've written a custom template loader that inherits BaseLoader, you must inherit Loader instead.")
    return warnings, [], []


def check_test_template_loader(line, filename, options):
    warnings = []
    if 'TestTemplateLoader' in line:
        warnings.append('Private API django.test.utils.TestTemplateLoader is deprecated in favor of django.template.loaders.locmem.Loader.')
    return warnings, [], []


def check_redirect_view(line, filename, options):
    warnings = []
    if 'RedirectView.as_view' in line and 'permanent' not in line:
        warnings.append('Default value of RedirectView.permanent will change from True to False in Django 1.9. Set an explicit value.')
    return warnings, [], []



def check_django_18(line, filename, options):
    warnings = []
    info = []
    errors = []

    for check in (
            check_duplicate_username,
            check_app_name,
            check_cache_class,
            check_complie_string,
            check_override_template,
            check_future,
            check_patterns,
            check_noargs,
            check_resolve_variable,
            check_webdesign,
            check_error_message,
            check_has_changed,
            check_remove_tags,
            check_is_admin_site,
            check_subfieldbase,
            check_checksums,
            check_original_content_type_id,
            check_base_loader,
            check_test_template_loader,
            check_redirect_view,
        ):
        warn, err, inf = check(line, filename, options)
        warnings += warn
        info += inf
        errors += err
    return warnings, errors, info


rules = [{
    'long_option': '--django-18',
    'action': 'store_true',
    'dest': 'django_18',
    'help': 'Check for changes and deprecations in Django 1.8.',
    'callback': check_django_18,
    'enabled': lambda options: options.django_18,
}]
