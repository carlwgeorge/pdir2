import sys

import pdir


def test_pdir_module():
    import m
    result = pdir(m)
    if sys.version[0] == '2':
        assert result.repr_str == repr(result) == '\n'.join([
            '\x1b[0;33mmodule attribute:\x1b[0;m', (
                '    \x1b[0;36m__file__\x1b[0;m\x1b[1;30m, '
                '\x1b[0;m\x1b[0;36m__name__\x1b[0;m\x1b[1;30m, '
                '\x1b[0;m\x1b[0;36m__package__\x1b[0;m'),
            '\x1b[0;33mother:\x1b[0;m', (
                '    \x1b[0;36m__builtins__\x1b[0;m\x1b[1;30m, '
                '\x1b[0;m\x1b[0;36ma\x1b[0;m\x1b[1;30m, '
                '\x1b[0;m\x1b[0;36mb\x1b[0;m'),
            '\x1b[0;33mspecial attribute:\x1b[0;m',
            '    \x1b[0;36m__doc__\x1b[0;m', '\x1b[0;33mclass:\x1b[0;m',
            '    \x1b[0;36mOOO:\x1b[0;m \x1b[1;30mOOO today.\x1b[0;m',
            '\x1b[0;33mfunction:\x1b[0;m',
            '    \x1b[0;36mfunc:\x1b[0;m \x1b[1;30mThis is a function\x1b[0;m'
        ])
    else:
        assert result.repr_str == repr(result) == '\n'.join([
            '\x1b[0;33mmodule attribute:\x1b[0;m', (
                '    \x1b[0;36m__cached__\x1b[0;m\x1b[1;30m, '
                '\x1b[0;m\x1b[0;36m__file__\x1b[0;m\x1b[1;30m, '
                '\x1b[0;m\x1b[0;36m__loader__\x1b[0;m\x1b[1;30m, '
                '\x1b[0;m\x1b[0;36m__name__\x1b[0;m\x1b[1;30m, '
                '\x1b[0;m\x1b[0;36m__package__\x1b[0;m\x1b[1;30m, '
                '\x1b[0;m\x1b[0;36m__spec__\x1b[0;m'),
            '\x1b[0;33mother:\x1b[0;m', (
                '    \x1b[0;36m__builtins__\x1b[0;m\x1b[1;30m, '
                '\x1b[0;m\x1b[0;36ma\x1b[0;m\x1b[1;30m, '
                '\x1b[0;m\x1b[0;36mb\x1b[0;m'),
            '\x1b[0;33mspecial attribute:\x1b[0;m',
            '    \x1b[0;36m__doc__\x1b[0;m', '\x1b[0;33mclass:\x1b[0;m',
            '    \x1b[0;36mOOO:\x1b[0;m \x1b[1;30mOOO today.\x1b[0;m',
            '\x1b[0;33mfunction:\x1b[0;m',
            '    \x1b[0;36mfunc:\x1b[0;m \x1b[1;30mThis is a function\x1b[0;m'
        ])
    print(result)
    del m


def test_pdir_object():
    class T(object):
        def what(self):
            """doc line"""
            pass

    result = pdir(T())
    print(result)  # TODO: add real test.


def test_pdir_class():
    class T(object):
        pass

    result = pdir(T)
    if sys.version[0] == '2':
        assert result.repr_str == repr(result) == '\n'.join([
            '\x1b[0;33mabstract class:\x1b[0;m',
            '    \x1b[0;36m__subclasshook__\x1b[0;m',
            '\x1b[0;33mattribute access:\x1b[0;m', (
                '    \x1b[0;36m__delattr__\x1b[0;m\x1b[1;30m, '
                '\x1b[0;m\x1b[0;36m__getattribute__\x1b[0;m\x1b[1;30m, '
                '\x1b[0;m\x1b[0;36m__setattr__\x1b[0;m'),
            '\x1b[0;33mobject customization:\x1b[0;m', (
                '    \x1b[0;36m__format__\x1b[0;m\x1b[1;30m, '
                '\x1b[0;m\x1b[0;36m__hash__\x1b[0;m\x1b[1;30m, '
                '\x1b[0;m\x1b[0;36m__init__\x1b[0;m\x1b[1;30m, '
                '\x1b[0;m\x1b[0;36m__new__\x1b[0;m\x1b[1;30m, '
                '\x1b[0;m\x1b[0;36m__repr__\x1b[0;m\x1b[1;30m, '
                '\x1b[0;m\x1b[0;36m__sizeof__\x1b[0;m\x1b[1;30m, '
                '\x1b[0;m\x1b[0;36m__str__\x1b[0;m'),
            '\x1b[0;33mpickle:\x1b[0;m', (
                '    \x1b[0;36m__reduce__\x1b[0;m\x1b[1;30m, '
                '\x1b[0;m\x1b[0;36m__reduce_ex__\x1b[0;m'),
            '\x1b[0;33mspecial attribute:\x1b[0;m', (
                '    \x1b[0;36m__class__\x1b[0;m\x1b[1;30m, '
                '\x1b[0;m\x1b[0;36m__dict__\x1b[0;m\x1b[1;30m, '
                '\x1b[0;m\x1b[0;36m__doc__\x1b[0;m\x1b[1;30m, '
                '\x1b[0;m\x1b[0;36m__module__\x1b[0;m\x1b[1;30m, '
                '\x1b[0;m\x1b[0;36m__weakref__\x1b[0;m')
        ])
    else:
        assert result.repr_str == repr(result) == '\n'.join([
            '\x1b[0;33mabstract class:\x1b[0;m',
            '    \x1b[0;36m__subclasshook__\x1b[0;m',
            '\x1b[0;33mattribute access:\x1b[0;m', (
                '    \x1b[0;36m__delattr__\x1b[0;m\x1b[1;30m, '
                '\x1b[0;m\x1b[0;36m__dir__\x1b[0;m\x1b[1;30m, '
                '\x1b[0;m\x1b[0;36m__getattribute__\x1b[0;m\x1b[1;30m, '
                '\x1b[0;m\x1b[0;36m__setattr__\x1b[0;m'),
            '\x1b[0;33mclass customization:\x1b[0;m',
            '    \x1b[0;36m__init_subclass__\x1b[0;m',
            '\x1b[0;33mobject customization:\x1b[0;m', (
                '    \x1b[0;36m__format__\x1b[0;m\x1b[1;30m, '
                '\x1b[0;m\x1b[0;36m__hash__\x1b[0;m\x1b[1;30m, '
                '\x1b[0;m\x1b[0;36m__init__\x1b[0;m\x1b[1;30m, '
                '\x1b[0;m\x1b[0;36m__new__\x1b[0;m\x1b[1;30m, '
                '\x1b[0;m\x1b[0;36m__repr__\x1b[0;m\x1b[1;30m, '
                '\x1b[0;m\x1b[0;36m__sizeof__\x1b[0;m\x1b[1;30m, '
                '\x1b[0;m\x1b[0;36m__str__\x1b[0;m'),
            '\x1b[0;33mpickle:\x1b[0;m', (
                '    \x1b[0;36m__reduce__\x1b[0;m\x1b[1;30m, '
                '\x1b[0;m\x1b[0;36m__reduce_ex__\x1b[0;m'),
            '\x1b[0;33mrich comparison:\x1b[0;m', (
                '    \x1b[0;36m__eq__\x1b[0;m\x1b[1;30m, '
                '\x1b[0;m\x1b[0;36m__ge__\x1b[0;m\x1b[1;30m, '
                '\x1b[0;m\x1b[0;36m__gt__\x1b[0;m\x1b[1;30m, '
                '\x1b[0;m\x1b[0;36m__le__\x1b[0;m\x1b[1;30m, '
                '\x1b[0;m\x1b[0;36m__lt__\x1b[0;m\x1b[1;30m, '
                '\x1b[0;m\x1b[0;36m__ne__\x1b[0;m'),
            '\x1b[0;33mspecial attribute:\x1b[0;m', (
                '    \x1b[0;36m__class__\x1b[0;m\x1b[1;30m, '
                '\x1b[0;m\x1b[0;36m__dict__\x1b[0;m\x1b[1;30m, '
                '\x1b[0;m\x1b[0;36m__doc__\x1b[0;m\x1b[1;30m, '
                '\x1b[0;m\x1b[0;36m__module__\x1b[0;m\x1b[1;30m, '
                '\x1b[0;m\x1b[0;36m__weakref__\x1b[0;m')
        ])
    print(result)


def test_dir_without_argument():
    a = 1
    b = 2

    def whatever():
        """One line doc."""
        pass

    result = pdir()
    assert result.repr_str == repr(result) == '\n'.join([
        '\x1b[0;33mother:\x1b[0;m',
        '    \x1b[0;36ma\x1b[0;m\x1b[1;30m, \x1b[0;m\x1b[0;36mb\x1b[0;m',
        '\x1b[0;33mfunction:\x1b[0;m',
        '    \x1b[0;36mwhatever:\x1b[0;m \x1b[1;30mOne line doc.\x1b[0;m',
    ])
    print(result)
