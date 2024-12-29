from django import template

register = template.Library()

@register.filter(name='get_field_label')
def get_field_label(field_name):
    """Map field names to user-friendly labels."""
    field_labels = {
        'password2': 'Confirm Password',
        'password1': 'Password',
        'email': 'Email Address',
        'username': 'Username',
    }
    return field_labels.get(field_name, field_name)
