import io

class EasyStringIO(io.StringIO):
    def write(self, *args):
        for arg in args:
            io.StringIO.write(self, arg)
