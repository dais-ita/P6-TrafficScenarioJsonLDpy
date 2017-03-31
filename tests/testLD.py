'''
Created on 31 Mar 2017

@author: Federico Cerutti <federico.cerutti@acm.org>
'''
import unittest
import CameraSpeedLimits.ld
from rdflib import Graph
from rdflib.compare import isomorphic


class TestToLD(unittest.TestCase):

    def testStringData(self):
        self.assertRaises(AssertionError, CameraSpeedLimits.ld.toLD, "test")

    def testEmptyData(self):
        self.assertRaises(AssertionError, CameraSpeedLimits.ld.toLD, ())
        
    def testFirst(self):
        self.assertRaises(AssertionError, CameraSpeedLimits.ld.toLD, (0, 0, 0, 0, 0))
        
    def testSecond(self):
        self.assertRaises(AssertionError, CameraSpeedLimits.ld.toLD, ("0", 0, 0, 0, 0))
        
    def testSecondNotFloat(self):
        self.assertRaises(AssertionError, CameraSpeedLimits.ld.toLD, ("0", "a", 0, 0, 0))

    def testThird(self):
        self.assertRaises(AssertionError, CameraSpeedLimits.ld.toLD, ("0", "0.1", 0, 0, 0))
        
    def testThirdNotFloat(self):
        self.assertRaises(AssertionError, CameraSpeedLimits.ld.toLD, ("0", "0", "a", 0, 0))
        
    def testFourth(self):
        self.assertRaises(AssertionError, CameraSpeedLimits.ld.toLD, ("0", "0.1", "0.1", 0, 0))
        
    def testFifth(self):
        self.assertRaises(AssertionError, CameraSpeedLimits.ld.toLD, ("0", "0.1", "0.1", "0", 0))
        
    def testSimpleCase(self):        
        g = Graph()
        g.parse("simplecase.owl")
        
        data = ('01460', '51.6301', '-0.0782', '?-1', '40 mph') 

                
#         d = graph_diff(to_canonical_graph(g), to_canonical_graph(toLD([cameraid, cameralat, cameralong, addrstreet, speedlimit])))
#         print "in both"
#         print d[0].serialize(format="turtle")
#         
#         print "in file"
#         print d[1].serialize(format="turtle")
#         
#         print "in function"
#         print d[2].serialize(format="turtle")
        
        self.assertTrue(isomorphic(g, CameraSpeedLimits.ld.toLD(data)), "simple test case from example failed")
        


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()