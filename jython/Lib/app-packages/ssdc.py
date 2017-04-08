from __future__ import print_function

from ru.icc.cells.ssdc import DataLoader
from java.io import File
from ru.icc.cells.ssdc.model import Tables
from ru.icc.cells.ssdc.model import CategoryTemplateManager
from ru.icc.cells.ssdc.writers import EvaluationExcelWriter

from org.kie.internal import KnowledgeBaseFactory
from org.kie.internal.builder import KnowledgeBuilder
from org.kie.internal.builder import KnowledgeBuilderFactory
from org.kie.internal.definition import KnowledgePackage
from org.kie.internal.io import ResourceFactory
from org.kie.internal.runtime import StatefulKnowledgeSession

from org.kie.api.event.rule import DebugAgendaEventListener
from org.kie.api.io import ResourceType

import os

CATMAN = CategoryTemplateManager.getInstance()
KB = KnowledgeBaseFactory.newKnowledgeBase()
DEBUG = True

# Load rules.

loader = DataLoader.getInstance()
DIR = "examples"
FILENAME = "T001.xlsx"
DSL_PATH = "crl/crl.dsl"


def printTable(t):
    for cell in t.getCells():
        print(cell.getText())


def loadRules():
    builder = KnowledgeBuilderFactory.newKnowledgeBuilder()
    dsl = ResourceFactory.newFileResource(DSL_PATH)
    builder.add(dsl, ResourceType.DSL)
    # builder.add(dslr, ResourceType.DSLR)

    if builder.hasErrors():
        raise RuntimeError("Cannot load rules!")
    pkgs = builder.getKnowledgePackages()
    KB.addKnowledgePackages(pkgs)


def fireRules(table, kb):
    session = kb.newStatefulKnowledgeSession()
    if (DEBUG):
        session.addEventListener(DebugAgendaEventListener())

    for cell in table.getCells():
        session.insert(cell)

    for cat in table.getLocalCategoryBox().getCategories():
        session.insert(cat)

    session.fireAllRules()


loadRules()

book = File(os.path.join(DIR, FILENAME))
loader.loadWorkbook(book)
loader.goToSheet(0)
tables = []
print("Tables -------------- ")
while True:
    t = loader.nextTable()
    if t is None:
        break
    tables.append(t)
    # printTable(t)

# print(tables)

for i, t in enumerate(tables):
    print("Processing {}".format(t))
    Tables.recoverCellBorders(t)

    if CATMAN.hasAtLeastOneCategoryTemplate():
        CATMAN.createCategories(t)
    fireRules(t, KB)

    t.update()
    print(t.trace())
    cf = t.toCanonicalForm()
    cf.print()
    out = EvaluationExcelWriter(
        File(os.path.join(DIR, "{}.out-".format(i) + FILENAME)))
    out.write(t)
