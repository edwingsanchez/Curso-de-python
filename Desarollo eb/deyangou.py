import django


def django_info():
    """Print Django version information."""
    print(f"Django version: {django.get_version()}")


if __name__ == "__main__":
    django_info()
