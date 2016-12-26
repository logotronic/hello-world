using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Item23_number1
{
    class Snowing : Weather
    {
        public string hightoday { get; set; }
        public Snowing() : base()
        {
            this.hightoday = "Lower than H2O freezing point";
        }

        public Snowing(double wind, double inperhour, string windchill)
            base(wind,inperhour,windchill)
        {
            this.hightoday=hightoday;
        }
        new public string toString()
        {
            return String.Format("Wind today is {0} per hour, snow rate at {1} inch per hour and really feels like {2}", wind, inperhour, windchill);
        }
        
        static void Main(string[] args)
        {
            
        }
    }
}
