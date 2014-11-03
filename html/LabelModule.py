from .HtmlElementModule import HtmlElement
from .TextElementModule import TextElement

class Label(HtmlElement):
    def __init__(self, value, **attributes):
        HtmlElement.__init__(self, 'label', **attributes)
        self.append(TextElement(value))
