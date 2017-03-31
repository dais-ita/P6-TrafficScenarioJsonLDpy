'''
Created on 31 Mar 2017

@author: geryo
'''
import unittest
import AnalysisVideos.ld
from rdflib import Graph
from rdflib.compare import isomorphic, graph_diff

class Test(unittest.TestCase):


    def testAnalysisSimplecCase(self):
        g = Graph()
        g.parse("simpleanalysis.owl")
        testcase = [[('435e3065', 144, 123.0, 24.0, -0.016143799, 0.84008789), ('5b06b4e3', 144, 223.0, 126.0, -0.034576416, -1.7939911), ('435e3065', 145, 123.0, 27.0, 0.0065307617, -0.91390991)]]
        
#         d = graph_diff(g, AnalysisVideos.ld.toLD(testcase))
#         print "in both"
#         print d[0].serialize(format="turtle")
#          
#         print "in file"
#         print d[1].serialize(format="turtle")
#          
#         print "in function"
#         print d[2].serialize(format="turtle")
        
        self.assertTrue(isomorphic(g, AnalysisVideos.ld.toLD(testcase)))


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testAnalysisSimplecCase']
    unittest.main()