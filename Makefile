.PHOMY: build all run test build-test

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
