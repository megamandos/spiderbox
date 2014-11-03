from .HtmlElementModule import HtmlElement
from .BooleanAttributeModule import BooleanAttribute

class Input(HtmlElement):
    checked = BooleanAttribute('checked')
    autofocus = BooleanAttribute('autofocus')
    required = BooleanAttribute('required')
    disabled = BooleanAttribute('disabled')
    readonly = BooleanAttribute('readonly')
    multiple = BooleanAttribute('multiple')
    autocomplete = BooleanAttribute('autocomplete', ('on', 'off'))

    def __init__(self, name, type = 'text', **attributes):
        HtmlElement.__init__(self, 'input', name = name, type = 'text', **attributes)
