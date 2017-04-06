.PHOMY: build all run test build-test python python-mvn

MAIN_CLASS=ru.icc.cells.lod.ann.App

all: build

build: install

build-test:
	mvn install

install:
	mvn install -Dmaven.test.skip=true

run:
	mvn exec:java -Dexec.mainClass=$(MAIN_CLASS)

test:
	mvn test

python:
	bin/jython


python-mvn:
	mvn exec:java -Dexec.mainClass=org.python.util.jython \
		-Dpython.home=./jython -Dpython.executable=./target/jython
