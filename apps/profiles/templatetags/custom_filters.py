from django import template

register = template.Library()

@register.filter
def get_field_name(form_fields, field_name):
    if form_fields.get(field_name):
        return form_fields[field_name].label
    return field_name