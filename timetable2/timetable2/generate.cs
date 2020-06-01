using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.IO;
using System.Diagnostics;
using System.Data.SQLite;

namespace timetable2
{
    public partial class generate : Form
    {
        string connection = @"Data Source=C:\Users\jj\PycharmProjects\projects\data.sqlite;Version=3;";
        public generate()
        {
            InitializeComponent();
        }
        public void viewfun(String pname, String fname, WebBrowser ob)
        {
            Process p = new Process();
            ProcessStartInfo info = new ProcessStartInfo();
            info.WindowStyle = System.Diagnostics.ProcessWindowStyle.Normal;
            info.FileName = "cmd.exe";
            info.CreateNoWindow = true;
            info.RedirectStandardInput = true;
            info.RedirectStandardOutput = true;
            info.UseShellExecute = false;
            p.StartInfo = info;
            p.Start();
            //p.WaitForExit();

            using (StreamWriter sw = p.StandardInput)
            {
                if (sw.BaseStream.CanWrite)
                {
                    sw.WriteLine("cd /d C:/Users/jj/PycharmProjects/projects");
                    sw.WriteLine("python " + pname);
                    // String s = listBox2.SelectedItem.ToString();
                    // s = s.Substring(0, s.IndexOf("."));
                    //MessageBox.Show(s);
                    //sw.WriteLine("java " + s);
                    //sw.WriteLine("use mydb;");
                }
            }
            String line = "";
            while (!p.StandardOutput.EndOfStream)
            {
                line = line + p.StandardOutput.ReadToEnd();

                // do something with line
            }
            ob.Navigate(new Uri("file:///E:/" + fname));


        }
        private void button1_Click(object sender, EventArgs e)
        {
            String period = textBox1.Text;
            String time = textBox2.Text;
            String days = textBox6.Text;

            Process p = new Process();
            ProcessStartInfo info = new ProcessStartInfo();
            info.WindowStyle = System.Diagnostics.ProcessWindowStyle.Normal;
            info.FileName = "cmd.exe";
            info.CreateNoWindow = true;
            info.RedirectStandardInput = true;
            info.RedirectStandardOutput = true;
            info.UseShellExecute = false;
            p.StartInfo = info;
            p.Start();
            //p.WaitForExit();

            using (StreamWriter sw = p.StandardInput)
            {
                if (sw.BaseStream.CanWrite)
                {
                    sw.WriteLine("cd /d C:/Users/jj/PycharmProjects/projects");
                    sw.WriteLine("python mainfile.py "+period+" "+time+" "+days);

                }
            }
            String line = "";
            while (!p.StandardOutput.EndOfStream)
            {
                line = line + p.StandardOutput.ReadToEnd();

                // do something with line
            }
           // MessageBox.Show(line);
            viewfun("viewoutdata.py", "viewout.html", webBrowser1);
        }

        private void generate_Load(object sender, EventArgs e)
        {
           
            SQLiteConnection sqliteCon = new SQLiteConnection(connection);
            try
            {
                sqliteCon.Open();

                string query = "delete from outdata";
                //Delete 1 records from admin
                //    username='" + textBox1.Text + "'and password='" + textBox2.Text + "'";
                SQLiteCommand command = new SQLiteCommand(query, sqliteCon);
                if (command.ExecuteNonQuery() == 1)
                {
                   // MessageBox.Show("deleted");
           
                   
                }

              
                string query1 = "update  sqlite_sequence set seq=0 where name='outdata'";
                //Delete 1 records from admin
                //    username='" + textBox1.Text + "'and password='" + textBox2.Text + "'";
                SQLiteCommand command1 = new SQLiteCommand(query1, sqliteCon);
                if (command1.ExecuteNonQuery() == 1)
                {
                  //   MessageBox.Show(" set to 1");


                }

                sqliteCon.Close();

            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
                sqliteCon.Close();

            }
            viewfun("viewoutdata.py", "viewout.html", webBrowser1);
        
        }

    
    }
}
