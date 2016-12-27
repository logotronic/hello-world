using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Item23_number1
{
    class Value_vs_Reference
    {
        Point myPoint = new Point(0, 0);      // a new value-type variable
        Form myForm = new Form();              // a new reference-type variable

        Test(myPoint, myForm);                // Test is a method defined below

        void Test(Point p, Form f)

        {
            p.X = 100;                       // No effect on MyPoint since p is a copy
            f.Text = "Hello, World!";        // This will change myForm’s caption since
                                             // myForm and f point to the same object
            f = null;                        // No effect on myForm
        }

    }
}
