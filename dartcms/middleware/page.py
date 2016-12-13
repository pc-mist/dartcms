# coding: utf-8
from dartcms import get_model
from django.http.response import Http404


class PageMiddleware(object):

    def process_request(self, request):
        request_path = request.path.strip('/')
        path_parts = request_path.split('/')

        PageModule = get_model('pages', 'PageModule')
        module_slug = path_parts[0]

        try:
            request.page_module = PageModule.objects.get(slug=module_slug)
        except PageModule.DoesNotExist:
            return

        Page = get_model('pages', 'Page')

        path = '/' if request_path == '' else '/%s/' % request.path.strip('/')
        page = None

        try:
            page = Page.objects.get(url=path, redirect_url='')
        except Page.DoesNotExist:
            while path_parts:
                path_parts.pop()
                if path_parts:
                    path = '/%s/' % '/'.join(path_parts)
                    try:
                        page = Page.objects.get(url=path, redirect_url='')
                        break
                    except Page.DoesNotExist:
                        continue

        if page:
            request.page = page
            request.page_children = page.children.filter(is_enabled=True, is_in_menu=True)

    def process_view(self, request, **kwargs):
        namespaces = request.resolver_match.namespaces

        if 'dartcms' in namespaces or 'admin' in namespaces:
            return

        if hasattr(request, 'page_module') and not hasattr(request, 'page'):
            raise Http404
