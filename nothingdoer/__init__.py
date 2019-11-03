import logging


class NothingDoer(object):
    """NothingDoer does nothing. (except stdlib logging and maybe call a callback)
    It's (somewhat) drop-in-able to replace things to do nothing instead.
    You may sub-class this thing to implement __eq__ or similar for your needs.
    """
    def __init__(self, callback=None):
        """Do (mostly) nothing.
        When a NothingDoer(callback=callable) is called,
        callable will be called with the NothingDoer as its first arg,
        and all other args and kwargs are passed through.
        NothingDoer(callback=callable)() will return callable's return.
        By default, the NothingDoer instance itself is returned.
        :param callback: optional function or other callable object
        """
        self._callback = callback
        self._logger = logging.getLogger(__name__)

    def __repr__(self):
        return '<{} callback={}>'.format(
            self.__class__.__name__,
            self._callback,
        )

    __str__ = __repr__

    def __getattr__(self, attr):
        self._logger.debug('"{}" is a {}'.format(
            attr,
            self.__class__.__name__,
        ))
        return self

    __getitem__ = __getattr__

    def __call__(self, *a, **kw):
        self._logger.debug('call args: {}; kwargs: {}'.format(a, kw))
        if self._callback:
            return self._callback(self, *a, **kw)
        return self
