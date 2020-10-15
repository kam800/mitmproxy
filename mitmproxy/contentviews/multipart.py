from mitmproxy.net import http
from mitmproxy.coretypes import multidict
from . import base


class ViewMultipart(base.View):
    name = "Multipart Form"

    @staticmethod
    def _format(v):
        yield [("highlight", "Form data:\n")]
        for message in base.format_dict(multidict.MultiDict(v)):
            yield message

    def __call__(self, data, **metadata):
        headers = metadata.get("headers", {})
        v = http.multipart.decode(headers, data)
        if v:
            return "Multipart form", self._format(v)

    def should_render(self, content_type):
        return content_type == "multipart/form-data"
