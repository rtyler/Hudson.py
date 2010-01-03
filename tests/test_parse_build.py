#!/usr/bin/env python

import unittest

from hudson import build

class BasicBuildTest(unittest.TestCase):
    def setUp(self):
        self.b = build.from_string(self.buildxml)

    def test_result(self):
        self.assertEquals(self.b.result, build.SUCCESS)
    
    def test_builtOn(self):
        self.assertEquals(self.b.builtOn, 'openSUSE')

    def test_keepLog(self):
        self.assertTrue(self.b.keepLog is False)

    def test_workspace(self):
        self.assertEquals(self.b.workspace, '/home/tyler/hudson/workspace/next')

    def test_hudsonVersion(self):
        self.assertEquals(self.b.hudsonVersion, '1.339')

    def test_charset(self):
        self.assertEquals(self.b.charset, 'UTF-8')

    def test_number(self):
        self.assertEquals(self.b.number, 10)

    def test_duration(self):
        self.assertEquals(self.b.duration, 88390)
    buildxml = '''<?xml version='1.0' encoding='UTF-8'?>
        <build>
        <actions>
            <hudson.model.CauseAction>
            <causes>
                <hudson.model.Cause_-UserCause>
                <authenticationName>anonymous</authenticationName>
                </hudson.model.Cause_-UserCause>
            </causes>
            </hudson.model.CauseAction>
            <hudson.plugins.git.util.BuildData>
            <buildsByBranchName>
                <entry>
                <string>origin/next</string>
                <hudson.plugins.git.util.Build>
                    <revision>
                    <sha1>
                        <byte-array>QnenrfUeJ2+HD+cl2B8VlS3QAlU=</byte-array>
                    </sha1>
                    <branches class="list">
                        <hudson.plugins.git.Branch>
                        <sha1 reference="../../../sha1"/>
                        <name>origin/next</name>
                        </hudson.plugins.git.Branch>
                    </branches>
                    </revision>
                    <hudsonBuildNumber>10</hudsonBuildNumber>
                </hudson.plugins.git.util.Build>
                </entry>
            </buildsByBranchName>
            <lastBuild reference="../buildsByBranchName/entry/hudson.plugins.git.util.Build"/>
            </hudson.plugins.git.util.BuildData>
            <hudson.tasks.junit.TestResultAction>
            <owner class="build" reference="../../.."/>
            <failCount>0</failCount>
            <skipCount>0</skipCount>
            <totalCount>2123</totalCount>
            <testData/>
            <descriptions class="java.util.concurrent.ConcurrentHashMap" serialization="custom">
                <unserializable-parents/>
                <java.util.concurrent.ConcurrentHashMap>
                <default>
                    <segmentMask>15</segmentMask>
                    <segmentShift>28</segmentShift>
                    <segments>
                    <java.util.concurrent.ConcurrentHashMap_-Segment>
                        <sync class="java.util.concurrent.locks.ReentrantLock$NonfairSync" serialization="custom">
                        <java.util.concurrent.locks.AbstractQueuedSynchronizer>
                            <default>
                            <state>0</state>
                            </default>
                        </java.util.concurrent.locks.AbstractQueuedSynchronizer>
                        <java.util.concurrent.locks.ReentrantLock_-Sync>
                            <default/>
                        </java.util.concurrent.locks.ReentrantLock_-Sync>
                        </sync>
                        <loadFactor>0.75</loadFactor>
                    </java.util.concurrent.ConcurrentHashMap_-Segment>
                    <java.util.concurrent.ConcurrentHashMap_-Segment>
                        <sync class="java.util.concurrent.locks.ReentrantLock$NonfairSync" serialization="custom">
                        <java.util.concurrent.locks.AbstractQueuedSynchronizer>
                            <default>
                            <state>0</state>
                            </default>
                        </java.util.concurrent.locks.AbstractQueuedSynchronizer>
                        <java.util.concurrent.locks.ReentrantLock_-Sync>
                            <default/>
                        </java.util.concurrent.locks.ReentrantLock_-Sync>
                        </sync>
                        <loadFactor>0.75</loadFactor>
                    </java.util.concurrent.ConcurrentHashMap_-Segment>
                    <java.util.concurrent.ConcurrentHashMap_-Segment>
                        <sync class="java.util.concurrent.locks.ReentrantLock$NonfairSync" serialization="custom">
                        <java.util.concurrent.locks.AbstractQueuedSynchronizer>
                            <default>
                            <state>0</state>
                            </default>
                        </java.util.concurrent.locks.AbstractQueuedSynchronizer>
                        <java.util.concurrent.locks.ReentrantLock_-Sync>
                            <default/>
                        </java.util.concurrent.locks.ReentrantLock_-Sync>
                        </sync>
                        <loadFactor>0.75</loadFactor>
                    </java.util.concurrent.ConcurrentHashMap_-Segment>
                    <java.util.concurrent.ConcurrentHashMap_-Segment>
                        <sync class="java.util.concurrent.locks.ReentrantLock$NonfairSync" serialization="custom">
                        <java.util.concurrent.locks.AbstractQueuedSynchronizer>
                            <default>
                            <state>0</state>
                            </default>
                        </java.util.concurrent.locks.AbstractQueuedSynchronizer>
                        <java.util.concurrent.locks.ReentrantLock_-Sync>
                            <default/>
                        </java.util.concurrent.locks.ReentrantLock_-Sync>
                        </sync>
                        <loadFactor>0.75</loadFactor>
                    </java.util.concurrent.ConcurrentHashMap_-Segment>
                    <java.util.concurrent.ConcurrentHashMap_-Segment>
                        <sync class="java.util.concurrent.locks.ReentrantLock$NonfairSync" serialization="custom">
                        <java.util.concurrent.locks.AbstractQueuedSynchronizer>
                            <default>
                            <state>0</state>
                            </default>
                        </java.util.concurrent.locks.AbstractQueuedSynchronizer>
                        <java.util.concurrent.locks.ReentrantLock_-Sync>
                            <default/>
                        </java.util.concurrent.locks.ReentrantLock_-Sync>
                        </sync>
                        <loadFactor>0.75</loadFactor>
                    </java.util.concurrent.ConcurrentHashMap_-Segment>
                    <java.util.concurrent.ConcurrentHashMap_-Segment>
                        <sync class="java.util.concurrent.locks.ReentrantLock$NonfairSync" serialization="custom">
                        <java.util.concurrent.locks.AbstractQueuedSynchronizer>
                            <default>
                            <state>0</state>
                            </default>
                        </java.util.concurrent.locks.AbstractQueuedSynchronizer>
                        <java.util.concurrent.locks.ReentrantLock_-Sync>
                            <default/>
                        </java.util.concurrent.locks.ReentrantLock_-Sync>
                        </sync>
                        <loadFactor>0.75</loadFactor>
                    </java.util.concurrent.ConcurrentHashMap_-Segment>
                    <java.util.concurrent.ConcurrentHashMap_-Segment>
                        <sync class="java.util.concurrent.locks.ReentrantLock$NonfairSync" serialization="custom">
                        <java.util.concurrent.locks.AbstractQueuedSynchronizer>
                            <default>
                            <state>0</state>
                            </default>
                        </java.util.concurrent.locks.AbstractQueuedSynchronizer>
                        <java.util.concurrent.locks.ReentrantLock_-Sync>
                            <default/>
                        </java.util.concurrent.locks.ReentrantLock_-Sync>
                        </sync>
                        <loadFactor>0.75</loadFactor>
                    </java.util.concurrent.ConcurrentHashMap_-Segment>
                    <java.util.concurrent.ConcurrentHashMap_-Segment>
                        <sync class="java.util.concurrent.locks.ReentrantLock$NonfairSync" serialization="custom">
                        <java.util.concurrent.locks.AbstractQueuedSynchronizer>
                            <default>
                            <state>0</state>
                            </default>
                        </java.util.concurrent.locks.AbstractQueuedSynchronizer>
                        <java.util.concurrent.locks.ReentrantLock_-Sync>
                            <default/>
                        </java.util.concurrent.locks.ReentrantLock_-Sync>
                        </sync>
                        <loadFactor>0.75</loadFactor>
                    </java.util.concurrent.ConcurrentHashMap_-Segment>
                    <java.util.concurrent.ConcurrentHashMap_-Segment>
                        <sync class="java.util.concurrent.locks.ReentrantLock$NonfairSync" serialization="custom">
                        <java.util.concurrent.locks.AbstractQueuedSynchronizer>
                            <default>
                            <state>0</state>
                            </default>
                        </java.util.concurrent.locks.AbstractQueuedSynchronizer>
                        <java.util.concurrent.locks.ReentrantLock_-Sync>
                            <default/>
                        </java.util.concurrent.locks.ReentrantLock_-Sync>
                        </sync>
                        <loadFactor>0.75</loadFactor>
                    </java.util.concurrent.ConcurrentHashMap_-Segment>
                    <java.util.concurrent.ConcurrentHashMap_-Segment>
                        <sync class="java.util.concurrent.locks.ReentrantLock$NonfairSync" serialization="custom">
                        <java.util.concurrent.locks.AbstractQueuedSynchronizer>
                            <default>
                            <state>0</state>
                            </default>
                        </java.util.concurrent.locks.AbstractQueuedSynchronizer>
                        <java.util.concurrent.locks.ReentrantLock_-Sync>
                            <default/>
                        </java.util.concurrent.locks.ReentrantLock_-Sync>
                        </sync>
                        <loadFactor>0.75</loadFactor>
                    </java.util.concurrent.ConcurrentHashMap_-Segment>
                    <java.util.concurrent.ConcurrentHashMap_-Segment>
                        <sync class="java.util.concurrent.locks.ReentrantLock$NonfairSync" serialization="custom">
                        <java.util.concurrent.locks.AbstractQueuedSynchronizer>
                            <default>
                            <state>0</state>
                            </default>
                        </java.util.concurrent.locks.AbstractQueuedSynchronizer>
                        <java.util.concurrent.locks.ReentrantLock_-Sync>
                            <default/>
                        </java.util.concurrent.locks.ReentrantLock_-Sync>
                        </sync>
                        <loadFactor>0.75</loadFactor>
                    </java.util.concurrent.ConcurrentHashMap_-Segment>
                    <java.util.concurrent.ConcurrentHashMap_-Segment>
                        <sync class="java.util.concurrent.locks.ReentrantLock$NonfairSync" serialization="custom">
                        <java.util.concurrent.locks.AbstractQueuedSynchronizer>
                            <default>
                            <state>0</state>
                            </default>
                        </java.util.concurrent.locks.AbstractQueuedSynchronizer>
                        <java.util.concurrent.locks.ReentrantLock_-Sync>
                            <default/>
                        </java.util.concurrent.locks.ReentrantLock_-Sync>
                        </sync>
                        <loadFactor>0.75</loadFactor>
                    </java.util.concurrent.ConcurrentHashMap_-Segment>
                    <java.util.concurrent.ConcurrentHashMap_-Segment>
                        <sync class="java.util.concurrent.locks.ReentrantLock$NonfairSync" serialization="custom">
                        <java.util.concurrent.locks.AbstractQueuedSynchronizer>
                            <default>
                            <state>0</state>
                            </default>
                        </java.util.concurrent.locks.AbstractQueuedSynchronizer>
                        <java.util.concurrent.locks.ReentrantLock_-Sync>
                            <default/>
                        </java.util.concurrent.locks.ReentrantLock_-Sync>
                        </sync>
                        <loadFactor>0.75</loadFactor>
                    </java.util.concurrent.ConcurrentHashMap_-Segment>
                    <java.util.concurrent.ConcurrentHashMap_-Segment>
                        <sync class="java.util.concurrent.locks.ReentrantLock$NonfairSync" serialization="custom">
                        <java.util.concurrent.locks.AbstractQueuedSynchronizer>
                            <default>
                            <state>0</state>
                            </default>
                        </java.util.concurrent.locks.AbstractQueuedSynchronizer>
                        <java.util.concurrent.locks.ReentrantLock_-Sync>
                            <default/>
                        </java.util.concurrent.locks.ReentrantLock_-Sync>
                        </sync>
                        <loadFactor>0.75</loadFactor>
                    </java.util.concurrent.ConcurrentHashMap_-Segment>
                    <java.util.concurrent.ConcurrentHashMap_-Segment>
                        <sync class="java.util.concurrent.locks.ReentrantLock$NonfairSync" serialization="custom">
                        <java.util.concurrent.locks.AbstractQueuedSynchronizer>
                            <default>
                            <state>0</state>
                            </default>
                        </java.util.concurrent.locks.AbstractQueuedSynchronizer>
                        <java.util.concurrent.locks.ReentrantLock_-Sync>
                            <default/>
                        </java.util.concurrent.locks.ReentrantLock_-Sync>
                        </sync>
                        <loadFactor>0.75</loadFactor>
                    </java.util.concurrent.ConcurrentHashMap_-Segment>
                    <java.util.concurrent.ConcurrentHashMap_-Segment>
                        <sync class="java.util.concurrent.locks.ReentrantLock$NonfairSync" serialization="custom">
                        <java.util.concurrent.locks.AbstractQueuedSynchronizer>
                            <default>
                            <state>0</state>
                            </default>
                        </java.util.concurrent.locks.AbstractQueuedSynchronizer>
                        <java.util.concurrent.locks.ReentrantLock_-Sync>
                            <default/>
                        </java.util.concurrent.locks.ReentrantLock_-Sync>
                        </sync>
                        <loadFactor>0.75</loadFactor>
                    </java.util.concurrent.ConcurrentHashMap_-Segment>
                    </segments>
                </default>
                <null/>
                <null/>
                </java.util.concurrent.ConcurrentHashMap>
            </descriptions>
            </hudson.tasks.junit.TestResultAction>
        </actions>
        <number>10</number>
        <result>SUCCESS</result>
        <duration>88390</duration>
        <charset>UTF-8</charset>
        <keepLog>false</keepLog>
        <builtOn>openSUSE</builtOn>
        <workspace>/home/tyler/hudson/workspace/next</workspace>
        <hudsonVersion>1.339</hudsonVersion>
        <scm class="hudson.plugins.git.GitChangeLogParser"/>
        <culprits/>
        </build>'''


if __name__ == '__main__':
    unittest.main()

