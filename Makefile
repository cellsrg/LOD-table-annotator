.PHOMY: build all run test

MAIN_CLASS=ru.icc.cells.lod.ann.App

all: build

build:
	mvn install

run:
	mvn mvn exec:java -Dexec.mainClass=$(MAIN_CLASS)
