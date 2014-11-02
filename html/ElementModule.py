class Element:
    def _render(self):
        raise NotImplementedError('No render method implemented for this class.')

    def __str__(self):
        return self._render()
