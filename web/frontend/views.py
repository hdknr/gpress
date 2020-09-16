from django.views.static import serve
from django.conf import settings


ROOT = settings.FRONTEND_PATH


def publish(request, path):
    if path.endswith('/') or path == '':
        path = path + 'index.html'
    print(ROOT, path)
    return serve(request, path, document_root=ROOT) 
