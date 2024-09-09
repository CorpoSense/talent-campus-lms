# This uses "templatetags". See :https://docs.djangoproject.com/en/5.1/howto/custom-template-tags/
import json
from django import template
from django.conf import settings
from django.templatetags.static import static

register = template.Library()

def get_manifest():
    # Load the manifest file from './static'
    # manifest_path = settings.BASE_DIR / settings.STATIC_ROOT.split('/')[-1] / '.vite' / 'manifest.json'
    # Load the manifest file from './dist'
    manifest_path = settings.BASE_DIR / settings.STATICFILES_DIRS[0] / '.vite' / 'manifest.json'
    with open(manifest_path) as f:
        manifest = json.load(f)
    return manifest

@register.simple_tag
def vite_asset_js(path):
    manifest = get_manifest()
    # Return the correct static file path
    return static(manifest['index.html'][path])

@register.simple_tag
def vite_asset_css(path, index=0):
    manifest = get_manifest()
    return static(manifest['index.html'][path][index])