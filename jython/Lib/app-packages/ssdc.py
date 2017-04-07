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
CATMAN = CategoryTemplateManager.getInstance()
KB = KnowledgeBaseFactory.newKnowledgeBase();

# Load rules.


loader=DataLoader.getInstance()
DIR="examples"
FILENAME="T001.xlsx"

book=File(os.path.join(DIR, FILENAME))
loader.loadWorkbook(book)
loader.goToSheet(0)
tables = []
while True:
    t = loader.nextTable()
    if t is None:
        break
    tables.append(t)

print(tables)

for i,t in enumerate(tables):
    print ("Processing {}".format(t))
    Tables.recoverCellBorders(t)

    if CATMAN.hasAtLeastOneCategoryTemplate():
        CATEGORY_TEMPLATE_MANAGER.createCategories(t)
        fireRules(t, KB)

    t.update()
    print(t.trace())
    cf=t.toCanonicalForm()
    cf.print()
    out = EvaluationExcelWriter(File(os.path.join(DIR,"{}.out-".format(i)+FILENAME)))
    out.write(t)
