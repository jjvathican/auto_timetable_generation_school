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
    public partial class adminremove : Form
    {
        string connection = @"Data Source=C:\Users\jj\PycharmProjects\projects\data.sqlite;Version=3;";
        public adminremove()
        {
            InitializeComponent();
        }

        private void adminremove_Load(object sender, EventArgs e)
        {
            viewfun("viewadmin.py", "viewad.html", webBrowser3);
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

        private void button3_Click(object sender, EventArgs e)
        {
            SQLiteConnection sqliteCon = new SQLiteConnection(connection);
            try
            {
                sqliteCon.Open();

                string query = "delete from admin where admin_id='" + s_name.Text +"'";
                //Delete 1 records from admin
                //    username='" + textBox1.Text + "'and password='" + textBox2.Text + "'";
                SQLiteCommand command = new SQLiteCommand(query, sqliteCon);
                if (command.ExecuteNonQuery() == 1)
                {
                    MessageBox.Show("deleted");
                    s_name.Text = null;
                   
                }

                sqliteCon.Close();


            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
                sqliteCon.Close();

            }
            viewfun("viewadmin.py", "viewad.html", webBrowser3);
        }
    }
}
