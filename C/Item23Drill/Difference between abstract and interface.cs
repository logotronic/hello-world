using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AbstractsANDInterfaces
    {
        /// 
        /// Summary description for Employee.
        public abstract class Employee
        {
            //we can have fields and properties 
            //in the Abstract class
            protected String id;
            protected String lname;
            protected String fname;
            //properties
           
            public abstract String ID
            {
                get;
                set;
            }

            public abstract String FirstName
            {
                get;
                set;
            }

            public abstract String LastName
            {
                get;
                set;
            }
            //completed methods

            public String Update()
            {
                return "Employee " + id + " " +
                          lname + " " + fname +
                          " updated";
            }
            //completed methods


            public String Add()
            {
                return "Employee " + id + " " +
                          lname + " " + fname +
                          " added";
            }
            //completed methods


            public String Delete()
            {
                return "Employee " + id + " " +
                          lname + " " + fname +
                          " deleted";
            }
            //completed methods


            public String Search()
            {
                return "Employee " + id + " " +
                          lname + " " + fname +
                          " found";
            }


            public abstract String CalculateWage();

        }
    }

namespace AbstractsANDInterfaces
    {
        /// <span class="code-SummaryComment"><summary></span>


        /// Summary description for IEmployee.

        /// <span class="code-SummaryComment"></summary></span>

        public interface IEmployee
        {
            //cannot have fields. uncommenting 


            //will raise error!
            //        protected String id;
            //        protected String lname;
            //        protected String fname;


            //just signature of the properties 

            //and methods.

            //setting a rule or contract to be 

            //followed by implementations.


            String ID
            {
                get;
                set;
            }

            String FirstName
            {
                get;
                set;
            }

            String LastName
            {
                get;
                set;
            }

            // cannot have implementation


            // cannot have modifiers public 

            // etc all are assumed public

            // cannot have virtual


            String Update();

            String Add();

            String Delete();

            String Search();

            String CalculateWage();
        }
    }
}
}
