from .ElementModule import Element

class TextElement(Element):
    def __init__(self, content):
        self._content = content

    def _render(self):
        return self._content
