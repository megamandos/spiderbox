import html
from .EasyStringIOModule import EasyStringIO
from .ElementModule import Element

class HtmlElement(Element):
    _protected = ['_tag', '_attributes', '_children']
    _void_tags = ['area', 'base', 'br', 'col', 'command', 'embed', 'hr', 'img', 'input', 'keygen', 'link', 'meta', 'param', 'source', 'track', 'wbr']


    def __init__(self, tag, children = [], **attributes):
        self._tag = tag
        self._attributes = attributes
        self._children = children


    def __getitem__(self, k):
        if type(k) is int:
            return self._children[k]

        elif type(k) is str:
            return self._attributes[k]

        else:
            raise ValueError('Unexpected key type "{0}" expecting str or int.'.format(type(k)))


    def __setitem__(self, k, v):
        if type(k) is int:
            if not isinstance(v, Element):
                raise TypeError('All children of an HtmlElement must be a subclass of Element or HtmlElement.')

            self._children[k] = v

        elif type(k) is str:
            if k in self.__class__.__dict__:
                object.__setattr__(self, k, v)

            else:
                if v is True:
                    v = 'true'

                elif v is False:
                    v = 'false'

                self._attributes[k] = v

        else:
            raise ValueError('Unexpected key type "{0}" expecting str or int.'.format(type(k)))


    def __getattr__(self, k):
        if k in self.__class__._protected:
            return object.__getattribute__(self, k)

        elif k in self._attributes:
            return self._attributes[k]

        else:
            raise AttributeError('{0} is not a valid attribute of {1}'.format(k, self.__class__.__name__))


    def __setattr__(self, k, v):
        if k in self.__class__._protected or k in self.__class__.__dict__:
            object.__setattr__(self, k, v)

        else:
            if v is True:
                v = 'true'

            elif v is False:
                v = 'false'

            self._attributes[k] = v


    def append(self, v):
        if not isinstance(v, Element):
            raise TypeError('All children of an HtmlElement must be a subclass of Element or HtmlElement.')

        self._children.append(v)


    def remove(self, k):
        if type(k) is int:
            if k < len(self._children):
                del self._children[k]

        elif type(k) is str:
            if k in self._attributes:
                del self._attributes[k]

        else:
            raise TypeError('Supplied argument must be type str or int.')


    def _render(self):
        buf = EasyStringIO()
        buf.write('<', self._tag)

        for attrName,attrValue in self._attributes.items():
            buf.write(' ', attrName, '="', html.escape(attrValue), '"')

        if self._tag in self.__class__._void_tags:
            buf.write('/>')

        else:
            buf.write('>')

            for child in self._children:
                buf.write(str(child))

            buf.write('</', self._tag, '>')

        return buf.getvalue()


    def __str__(self):
        return self._render()

