using System;
using System.IO;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace FileTransfer
{
    public class FileMove
    {
        static void Main()
        {
            string movee = @"C:\Users\Logan\Desktop\Folder A";
            string destination = @"C:\Users\Logan\Desktop\Folder B";

            DateTime rightnow = DateTime.Now;

            foreach (string file in Directory.EnumerateFiles(movee))
            {
                DateTime creation = File.GetLastWriteTime(file);
                string item = Path.GetFileName(file);
                string destiny = System.IO.Path.Combine(destination, item);
                if (creation > rightnow.AddHours(-24) && creation <= rightnow)
                {
                    System.IO.File.Copy(file, destiny);
                }
            }
        }
    }
}
