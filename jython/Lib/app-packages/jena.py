from __future__ import print_function
from six import *
from java.lang import System

from org.apache.jena.rdf.model import Model
from org.apache.jena.rdf.model import RDFNode
from org.apache.jena.rdf.model import Resource
from org.apache.jena.rdf.model import Statement
from org.apache.jena.rdf.model import StmtIterator
from org.apache.jena.util import FileManager
import os.path

data = os.path.abspath("data/data.ttl")

model = FileManager.get().loadModel(data, None, "TURTLE");
it = model.listStatements();

for stmt in it:
    s,p,o = stmt.getSubject(), stmt.getPredicate(), stmt.getObject()
    print(s,p,o)

model.write(System.out, "TURTLE")
