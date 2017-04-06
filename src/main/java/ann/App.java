package ru.icc.cells.lod.ann;
import org.python.util.PythonInterpreter;
import org.python.core.*;

public class App
{
    public static void main( String[] args )
        throws PyException
    {
        System.out.println( "Starting python interpreter..." );
        PythonInterpreter interp =
            new PythonInterpreter();

        System.out.println("done");

        interp.exec("import sys");
        interp.exec("print sys");

        interp.set("a", new PyInteger(42));
        interp.exec("print a");
        interp.exec("x = 2+2");
        PyObject x = interp.get("x");

        System.out.println("x: "+x);

        System.out.println("Done with interpretation.");

    }

}
