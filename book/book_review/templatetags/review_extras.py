from django import template

register = template.Library()

@register.filter
def star_rating(value):
    """Convert a numeric rating (1-5) into a star string."""
    try:
        value = int(value)  # Ensure it's an integer
        return "★" * value + "☆" * (5 - value)
    except ValueError:
        return "☆☆☆☆☆"  # Default to empty stars if invalid
