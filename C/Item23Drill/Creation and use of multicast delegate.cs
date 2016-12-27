using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Item23_number1
{
    class Creation_and_use_of_multicast_delegate
    {
        // Define a custom delegate that has a string parameter and returns void.
        delegate void CustomDel(string s);

    class TestClass
    {
        // Define two methods that have the same signature as CustomDel.
        static void Hello(string s)
        {
            System.Console.WriteLine("  Hello, {0}!", s);
        }

        static void Goodbye(string s)
        {
            System.Console.WriteLine("  Goodbye, {0}!", s);
        }

        static void Main()
        {
            // Declare instances of the custom delegate.
            CustomDel hiDel, byeDel, multiDel, multiMinusHiDel;

            // In this example, you can omit the custom delegate if you 
            // want to and use Action<string> instead.
            //Action<string> hiDel, byeDel, multiDel, multiMinusHiDel;

            // Create the delegate object hiDel that references the
            // method Hello.
            hiDel = Hello;

            // Create the delegate object byeDel that references the
            // method Goodbye.
            byeDel = Goodbye;

            // The two delegates, hiDel and byeDel, are combined to 
            // form multiDel. 
            multiDel = hiDel + byeDel;

            // Remove hiDel from the multicast delegate, leaving byeDel,
            // which calls only the method Goodbye.
            multiMinusHiDel = multiDel - hiDel;

            Console.WriteLine("Invoking delegate hiDel:");
            hiDel("A");
            Console.WriteLine("Invoking delegate byeDel:");
            byeDel("B");
            Console.WriteLine("Invoking delegate multiDel:");
            multiDel("C");
            Console.WriteLine("Invoking delegate multiMinusHiDel:");
            multiMinusHiDel("D");
        }
    }
}
}
