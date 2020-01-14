# comment

class Config:
    """Provides object-style access and utilities to basic objects like list and dict"""

    def __init__(self, obj=None):
        self._obj = obj

    def __call__(self, *args, **kwargs):
        return self._obj

    def _return_item(self, item):
        ret_item = self._obj[item]
        if self._is_sequence(ret_item):
            return Config(ret_item)
        else:
            return ret_item

    def __getitem__(self, item):
        return self._return_item(item)

    def __getattr__(self, item):
        return self._return_item(item)

    # def __setattr__(self, key, value):
    #     if key in self.__dict__:
    #         super().__setattr__(key, value)
    #     else:
    #         self._obj[key] = value

    def __delattr__(self, item):
        if item in self.__dict__:
            super().__delattr__(item)
        else:
            del self._obj[item]

    def __dir__(self):
        obj_dir = [i for i in self._obj] if hasattr(self._obj, 'keys') else []
        return obj_dir + super().__dir__()

    def __repr__(self):
        return repr(self._obj)

    # https://stackoverflow.com/questions/1835018/how-to-check-if-an-object-is-a-list-or-tuple-but-not-string
    @classmethod
    def _is_sequence(cls, arg):
        return (not hasattr(arg, "strip") and
                (hasattr(arg, "__getitem__") or
                hasattr(arg, "__iter__")))
