'''
Created on 31 Mar 2017

@author: Federico Cerutti <federico.cerutti@acm.org>
'''

from rdflib import URIRef, BNode, Literal, Graph, Namespace
from rdflib.namespace import RDF, RDFS, XSD, OWL

#List of lists of tuples of the form: [ [ (*car  
#id*:string,*frame number*:int, *camera position x*:int,*camera position  
#y*:int, *pixel velocity x:*float*, pixel velocity y:*float) ... ] ... ]
def toLD( data , debug = False):
    g = Graph()
    traffic = Namespace("https://dais-ita.org/traffic/")
    
    assert isinstance(data, list), "Expecting list"
    assert len(data) == 1, "Expecting one element"
        
    cars = {}
        
    for entry in data[0]:
        assert isinstance(entry, tuple), "Expecting lists"
        assert len(entry) == 6, "Expecting 6 values"
        assert isinstance(entry[0], basestring), "First element of list needs to be a string"
        assert isinstance(entry[1], int), "Second element of list needs to be a integer"
        assert isinstance(entry[2], float), "Third element of list needs to be a float"
        assert isinstance(entry[3], float), "Fourth element of list needs to be a float"
        assert isinstance(entry[4], float), "Fifth element of list needs to be a float"
        assert isinstance(entry[5], float), "Sixth element of list needs to be a float"
        
        carid = entry[0]
        carframe = entry[1]
        carposX = entry[2]
        carposY = entry[3]
        carvelX = entry[4]
        carvelY = entry[5]
        
        if carid not in cars:
            cars[carid]= 1
        else:
            cars[carid]+=1
        
        carnode = URIRef(traffic + "car" + carid )
        
        if (cars[carid] == 1):
            g.add( ( carnode, RDF.type, traffic.Car ) )
            g.add( ( carnode, RDF.type, OWL.NamedIndividual))
            g.add( ( carnode, RDFS.label, Literal(carid, datatype=XSD.string)))
        
        carmovnode = URIRef(traffic + "car" + carid + "mov" + str(cars[carid] ))
        
        g.add( ( carmovnode, RDF.type, traffic.CarMovement ) )
        g.add( ( carmovnode, RDF.type, OWL.NamedIndividual))
        
        g.add( ( carnode, traffic.has_movement, carmovnode ) )
        
        g.add( ( carmovnode, traffic.frameNumber, Literal(carframe, datatype=XSD.int)))
        g.add( ( carmovnode, traffic.posXinCamera, Literal(carposX, datatype=XSD.float)))
        g.add( ( carmovnode, traffic.posYinCamera, Literal(carposY, datatype=XSD.float)))
        g.add( ( carmovnode, traffic.pixelXSpeed, Literal(carvelX, datatype=XSD.float)))
        g.add( ( carmovnode, traffic.pixelYSpeed, Literal(carvelY, datatype=XSD.float)))
    
    if (debug):
        g.serialize(format='turtle')
    
    return g


def toJsonLD( data ):
    g = toLD(data)
    return g.serialize(format='json-ld', indent=4)