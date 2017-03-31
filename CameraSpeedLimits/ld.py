'''
Created on 31 Mar 2017

@author: Federico Cerutti <federico.cerutti@acm.org>
'''

from rdflib import URIRef, BNode, Literal, Graph, Namespace
from rdflib.namespace import RDF, RDFS, XSD, OWL

from Misc.datacheck import isfloat

#Tuple of the form: (*camera id*:string, *camera lat*:string, *camera long*: string,
# *OSM derived road name*:string, *speed limit*:string) 
def toLD( data, debug=False ):
    assert isinstance(data, tuple), "Expecting tuple" 
    assert len(data) == 5, "Expecting 5 values"
    assert isinstance(data[0], basestring), "First element of list needs to be a string"
    assert isinstance(data[1], basestring), "Second element of list needs to be a string"
    assert isinstance(data[2], basestring), "Third element of list needs to be a string"
    assert isinstance(data[3], basestring), "Fourth element of list needs to be a string"
    assert isinstance(data[4], basestring), "Fifth element of list needs to be a int"
    assert isfloat(data[1]), "Second element of list needs to represent a float number"
    assert isfloat(data[2]), "Third element of list needs to represent a float number"
    
    cameraid=data[0]
    cameralat=data[1]
    cameralong=data[2]
    addrstreet=data[3]
    speedlimit=data[4]
    
    toappend = ""
    if (float(cameralat) > 0):
        if(cameralat[0] != "+"):
            toappend += "+" + cameralat
        else:
            toappend += cameralat
    else:
            toappend += cameralat
    
    if (float(cameralong) > 0):
        if(cameralong[0] != "+"):
            toappend += "+" + cameralong
        else:
            toappend += cameralong
    else:
        toappend += cameralong
    
    g = Graph()
    traffic = Namespace("https://dais-ita.org/traffic/")
    pos = Namespace("http://www.w3.org/2003/01/geo/wgs84_pos#")
    osm = Namespace("https://raw.github.com/doroam/planning-do-roam/master/Ontology/tags.owl#")
    osmaddr = Namespace("https://raw.github.com/doroam/planning-do-roam/master/Ontology/tags.owl#k_addr:")        
    
    cameranode = URIRef(traffic + "camera" + cameraid )
    locationnode = URIRef(traffic + "location" + toappend )
    addressnode = URIRef(traffic + "address" + toappend )
     
     
    g.add( ( cameranode, RDF.type, traffic.Camera ) )
    g.add( ( cameranode, RDF.type, OWL.NamedIndividual))
    g.add( ( cameranode, RDFS.label, Literal(cameraid, datatype=XSD.string) ) )
    g.add( ( cameranode, pos.location, locationnode) )
    g.add( ( locationnode, RDF.type, pos.Point) )
    g.add( ( locationnode, RDF.type, OWL.NamedIndividual) )
    g.add( ( locationnode, pos.lat, Literal(cameralat, datatype=XSD.string) ) )
    g.add( ( locationnode, pos.long, Literal(cameralong, datatype=XSD.string) ) )
    g.add( ( cameranode, osm.has_address, addressnode ) )
    g.add( ( addressnode, RDF.type, osm.address))
    g.add( ( addressnode, RDF.type, OWL.NamedIndividual))
    g.add( ( addressnode, osmaddr.street, Literal(addrstreet, datatype=XSD.string) ) )
    g.add( ( addressnode, traffic.speedLimit, Literal(speedlimit, datatype=XSD.string) ) )
    
    
    if (debug):
        print g.serialize(format='turtle')

    return g


def toJsonLD( data ):
    g = toLD(data)
    return g.serialize(format='json-ld', indent=4)