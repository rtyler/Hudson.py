#!/usr/bin/env python

import sys

try:
    from xml.etree import cElementTree as ElementTree
except ImportError:
    from xml.etree import ElementTree


class Build(object):
    result = None
    builtOn = None
    keepLog = None
    number = None
    duration = None
    workspace = None
    hudsonVersion = None
    charset = None

    def _handle_result(self, e):
        module = sys.modules.get(__name__)
        self.result = getattr(module, e.text, UNKNOWN)

    def _handle_keepLog(self, e):
        self.keepLog = e.text == 'true'

    def _handle_number(self, e):
        self.number = int(e.text)

    def _handle_duration(self, e):
        self.duration = int(e.text)

    def _generic_handler(self, e):
        if e.getchildren():
            return
        setattr(self, e.tag, e.text)

    @classmethod 
    def from_xml(cls, xml):
        instance = cls()
        elem = ElementTree.fromstring(xml)
        for node in elem:
            method = '_handle_%s' % node.tag
            if hasattr(instance, method):
                getattr(instance, method)(node)
                continue
            instance._generic_handler(node)
        return instance


def from_string(xml):
    return Build.from_xml(xml)

SUCCESS = 1
FAILED = 2 
UNSTABLE = 3
ABORTED = 4
UNKNOWN = 5

