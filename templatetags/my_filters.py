from django import template
register = template.Library()

@register.inclusion_tag('block/navbar.html')
def show_navbar(section):
    return {'section': section}

@register.inclusion_tag('block/top.html')
def show_top():
    return {}

@register.inclusion_tag('block/write_us.html')
def write_us():
    return {}

@register.inclusion_tag('block/footer.html')
def show_footer():
    return {}