#!/usr/bin/env python

try:
    from xml.etree import cElementTree as ElementTree
except ImportError:
    from xml.etree import ElementTree

class XmlObject(object):
    def _generic_handler(self, e):
        if e.getchildren():
            return
        setattr(self, e.tag, e.text)

    @classmethod
    def from_element(cls, elem):
        instance = cls()
        for node in elem:
            method = '_handle_%s' % node.tag
            if hasattr(instance, method):
                getattr(instance, method)(node)
                continue
            instance._generic_handler(node)
        return instance

class TestSuite(XmlObject):
    file = None
    name = None
    duration = None
    stdout = None
    stderr = None
    cases = None

    def _handle_duration(self, e):
        self.duration = float(e.text)

    def _handle_cases(self, e):
        self.cases = []
        children = e.getchildren()
        if not children:
            return
        self.cases = [TestCase.from_element(c) for c in children]

class TestCase(XmlObject):
    duration = None
    className = None
    testName = None
    skipped = None
    failedSince = None

    def _handle_duration(self, e):
        self.duration = float(e.text)

    def _handle_skipped(self, e):
        self.skipped = e.text == 'true'

    def _handle_failedSince(self, e):
        self.failedSince = int(e.text)

def from_string(xml):
    elem = ElementTree.fromstring(xml)
    rc = {}
    for node in elem:
        if node.tag == 'duration':
            rc['duration'] = float(node.text)
            continue
        if node.tag == 'suites':
            rc['suites'] = [TestSuite.from_element(e) for e in node.getchildren()]
    return rc
