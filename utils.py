## JSONIC: the decorator

class jsonic(object):
    def __init__(self, *decorator_args, **decorator_kwargs):
        self.decorator_args = decorator_args
        self.decorator_kwargs = decorator_kwargs
    def __call__(self, fn):
        def jsoner(obj, **kwargs):
            dic = {}
            key = None
            thedic = None
            recurse_limit = 2
            thefields = obj._meta.get_all_field_names()
            kwargs.update(self.deckeywords)
            for field in thefields:
                if field in kwargs:
                    key = field
                    thedic = kwargs[key]
                    if isinstance(thedic, dict):
                        recurse_limit = 1
                    else:
                        recurse_limit = 0
                    break
            for field in thefields:
                if field == key:
                    continue
                try:
                    dic[field] = getattr(obj, field)
                except:
                    pass
            if key:
                for field in thedic:
                    try:
                        dic[field] = getattr(obj, field)
                    except:
                        pass
            if recurse_limit > 0:
                for field in thedic:
                    try:
                        dic[field] = jsoner(getattr(obj, field), **thedic)
                    except:
                        pass
            return dic
        return jsoner