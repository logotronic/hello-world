using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Item23_number1
{
   // A class can have many interfaces
   // An interface can't have concrete code
   public interface ShapeItem
     {
      double area();
     }

     class Rectangle : Shape
     {
       private double length;
       private double width;

         public Rectangle(double num1, double num2)
            {
              length = num1;
              width = num2;
            }

         public override double area()
           {
             return length * width;
           }
        }
}
