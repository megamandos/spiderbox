from .HtmlElementModule import HtmlElement
from .TextElementModule import TextElement
from .BooleanAttributeModule import BooleanAttribute

class Option(HtmlElement):
    selected = BooleanAttribute('selected')
    disabled = BooleanAttribute('disabled')

    def __init__(self, label, value):
        HtmlElement.__init__(self, 'option', value=value)
        self.append(TextElement(label))
