from urllib.parse import urlparse, urljoin

from flask import request, url_for, abort
from werkzeug.utils import redirect


def is_safe_url(target):

    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    return test_url.scheme in ('http', 'https') and ref_url.netloc == test_url.netloc


def if_url_is_safe_redirect(target_url, route_func_name_to_redirect_to=None, url_to_redirect_to=None):
    if not is_safe_url(target_url):
        abort(404)

    elif route_func_name_to_redirect_to:
        return redirect(url_for(route_func_name_to_redirect_to))
    else:
        return redirect(url_to_redirect_to)
