class BooleanAttribute:
    def __init__(self, name, values = None):
        self._name = name
        if values is not None:
            if type(values) is not tuple or len(values) != 2:
                raise ValueError('Value must be a two item tuple.')

        self._values = values


    def __get__(self, obj, type=None):
        if self._values is not None:
            if self._name not in obj._attributes:
                return None

            if obj._attributes[self._name] in self._values:
                if obj._attributes[self._name] == self._values[0]:
                    return True

                else:
                    return False

            raise ValueError('{0} is set to an unexpected value "{1}", I was expecting either "{2}" or "{3}".'.format(self._name, obj._attributes[self._name], *self._values))

        else:
            return self._name in obj._attributes


    def __set__(self, obj, value):
        if self._values is not None:
            if value is True:
                obj._attributes[self._name] = self._values[0]

            elif value is False:
                obj._attributes[self._name] = self._values[1]

            elif value in self._values:
                obj._attributes[self._name] = value

            else:
                raise ValueError('Cannot set {0} to {1}, only {2} or {3} are acceptable.'.format(self._name, value, self._values[0], self._values[1]))

        else:
            if value is True:
                obj._attributes[self._name] = self._name

            else:
                del obj._attributes[self._name]
