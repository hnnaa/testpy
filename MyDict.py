# coding:utf-8


class MyDict(dict):
    def __init__(self, **kw):
        super().__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError("attr to key,not exists key")

    def __setattr__(self, key, value):
        self[key] = value
