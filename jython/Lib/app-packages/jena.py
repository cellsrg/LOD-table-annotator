from __future__ import print_function
from six import *
from java.lang import System

from org.apache.jena.rdf.model import Model
from org.apache.jena.rdf.model import ModelFactory
from org.apache.jena.rdf.model import RDFNode
from org.apache.jena.rdf.model import Resource
from org.apache.jena.rdf.model import Statement
from org.apache.jena.rdf.model import StmtIterator
from org.apache.jena.util import FileManager
# from net.rootdev.javardfa.jena import RDFaReader
# from org.apache.jena.query import Query

# from java.lang import Class

import os.path

# data = os.path.abspath("data/data.ttl")
data = os.path.abspath("data/document.ttl")
# data = os.path.abspath("data/document.jsonld")
# data = os.path.abspath("data/document.xhtml")

# Class.forName("net.rootdev.javardfa.jena.RDFaReader")
model = FileManager.get().loadModel(data)  # , None, "TURTLE")
# model = ModelFactory.createDefaultModel()
# model.read(data, "TURTLE")

print(System.out)


def print_graph(model):
    for stmt in model.listStatements():
        # print(stmt)   # This works too, next two lines
        # could be commented out
        s, p, o = stmt.getSubject(), stmt.getPredicate(), stmt.getObject()
        print(s, p, o)


model.write(System.out, "TURTLE")
