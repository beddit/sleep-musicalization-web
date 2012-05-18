from django import template

register = template.Library()

@register.filter
def hoursminutes(seconds):
    if seconds is None:
        return seconds

    m, s = divmod(seconds, 60)
    h, m = divmod(m, 60)
    return "%d hours %d minutes" % (h, m)
