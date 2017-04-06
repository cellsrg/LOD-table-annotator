.PHOMY: build all run test build-test python python-mvn \
		run-mvn

MAIN_CLASS=ru.icc.cells.lod.ann.App

all: build

build: install

build-test:
	mvn install

install:
	mvn install -Dmaven.test.skip=true

run-mvn:
	mvn exec:java -Dexec.mainClass=$(MAIN_CLASS)

run:
	java -jar target/ann-0.1-jar-with-dependencies.jar

test:
	mvn test

python:
	jython/bin/jython


python-mvn:
	mvn exec:java -Dexec.mainClass=org.python.util.jython \
		-Dpython.home=./jython -Dpython.executable=./target/jython
