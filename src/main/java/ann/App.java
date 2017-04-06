package ru.icc.cells.lod.ann;
import org.python.util.PythonInterpreter;
import org.python.core.*;

public class App
{
    public static void main( String[] args )
        throws PyException
    {
        PythonInterpreter interp =
            new PythonInterpreter();

        interp.exec("import sys");
        interp.exec("sys.path.insert(0,\"jython/Lib\")");
        interp.exec("import appsite");


    }

}
