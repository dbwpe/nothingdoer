#!/usr/bin/env python

from unittest import TestCase

from nothingdoer import NothingDoer


class TestNothingDoer(TestCase):

    def nd(self, *a, **kw):
        return NothingDoer(*a, **kw)

    def test_str(self):
        nd = self.nd()
        expected = '<NothingDoer callback=None>'
        self.assertEqual(expected, repr(nd))
        self.assertEqual(expected, str(nd))

    def test_getattr(self):
        nd = self.nd()
        self.assertEqual(nd, nd.anything)

    def test_getitem(self):
        nd = self.nd()
        self.assertEqual(nd, nd['anything'])

    def test_call(self):
        nd = self.nd()
        self.assertEqual(nd, nd())

    # this one's a little convoluted
    def test_callback(self):
        expected_arg = ('ok',)
        expected_kwarg = {'yea': 'sure'}

        class callable():
            def __call__(self, nd, *a, **kw):
                self.nd = nd
                self.called_arg = a
                self.called_kwarg = kw
        call = callable()

        nd = self.nd(callback=call)
        nd(*expected_arg, **expected_kwarg)
        self.assertEqual(nd, call.nd)
        self.assertEqual(expected_arg, call.called_arg)
        self.assertEqual(expected_kwarg, call.called_kwarg)
