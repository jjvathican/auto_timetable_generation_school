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
    public partial class admin : Form
    {
        string connection = @"Data Source=C:\Users\jj\PycharmProjects\projects\data.sqlite;Version=3;";
        public admin()
        {
            InitializeComponent();
        }

        private void label5_Click(object sender, EventArgs e)
        {

        }

        private void button3_Click(object sender, EventArgs e)
        {
               SQLiteConnection sqliteCon = new SQLiteConnection(connection);
            try
            {
                sqliteCon.Open();

                string query = "INSERT INTO admin (username,password) VALUES ('" + s_name.Text + "','" + textBox1.Text + "')";

                SQLiteCommand command = new SQLiteCommand(query, sqliteCon);
                if (command.ExecuteNonQuery() == 1)
                {
                    MessageBox.Show("inserted");
                    s_name.Text = null;
                    textBox1.Text = null;
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

        private void admin_Load(object sender, EventArgs e)
        {
            viewfun("viewadmin.py", "viewad.html", webBrowser3);
        }

        private void webBrowser3_DocumentCompleted(object sender, WebBrowserDocumentCompletedEventArgs e)
        {

        }
    }
}
