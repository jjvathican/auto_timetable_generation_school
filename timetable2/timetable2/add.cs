using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Data.SQLite;
using System.IO;
using System.Diagnostics;


namespace timetable2
{
    public partial class add : Form
    {
        string connection = @"Data Source=C:\Users\jj\PycharmProjects\projects\data.sqlite;Version=3;";
        public add()
        {
            InitializeComponent();
            viewfun("viewroom.py", "viewrom.html", webBrowser2);
            viewfun("viewsubject.py", "viewsub.html", webBrowser1);
            viewfun("viewteacher.py", "viewtea.html", webBrowser3);
            viewfun("viewteacher.py", "viewtea.html", webBrowser4);
            viewfun("viewroom.py", "viewrom.html", webBrowser5);
            viewfun("viewsubject.py", "viewsub.html", webBrowser6);
        }

        private void button2_Click(object sender, EventArgs e)
        {
            SQLiteConnection sqliteCon = new SQLiteConnection(connection);
            try
            {
                sqliteCon.Open();

                string query = "INSERT INTO teacher (teach_id,t_name) VALUES ('" + t_id.Text + "','" + t_name.Text + "')";

                SQLiteCommand command = new SQLiteCommand(query, sqliteCon);
                if (command.ExecuteNonQuery() == 1)
                {
                    MessageBox.Show("inserted");
                    t_id.Text = null;
                    t_name.Text = null;
                }
                
                sqliteCon.Close();
               

            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
                sqliteCon.Close();

            }
            viewfun("viewteacher.py", "viewtea.html", webBrowser3);
           
        }

        private void button1_Click(object sender, EventArgs e)
        {
            SQLiteConnection sqliteCon = new SQLiteConnection(connection);
            try
            {
                sqliteCon.Open();

                string query = "INSERT INTO room (room_id,r_name) VALUES ('" + r_id.Text + "','" + r_name.Text + "')";

                SQLiteCommand command = new SQLiteCommand(query, sqliteCon);
                
                if (command.ExecuteNonQuery()== 1)
                {
                    MessageBox.Show("inserted");
                    r_id.Text = null;
                    r_name.Text = null;
                }

                sqliteCon.Close();


            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
                sqliteCon.Close();
            }
            viewfun("viewroom.py", "viewrom.html", webBrowser2);
           
        }

        private void button3_Click(object sender, EventArgs e)
        {
            SQLiteConnection sqliteCon = new SQLiteConnection(connection);
            try
            {
                sqliteCon.Open();

                string query = "INSERT INTO subject (sub_id,s_name) VALUES ('" + s_id.Text + "','" + s_name.Text + "')";

                SQLiteCommand command = new SQLiteCommand(query, sqliteCon);

                if (command.ExecuteNonQuery() == 1)
                {
                    MessageBox.Show("inserted");
                    r_id.Text = null;
                    r_name.Text = null;
                }

                sqliteCon.Close();


            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
                sqliteCon.Close();
            }
            viewfun("viewsubject.py","viewsub.html",webBrowser1);
            
        }
        public void viewfun(String pname,String fname,WebBrowser ob)
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
                    sw.WriteLine("python "+pname );
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
            ob.Navigate(new Uri("file:///E:/"+fname));


        }
        private void add_Load(object sender, EventArgs e)
        {

        }

        private void tabPage3_Click(object sender, EventArgs e)
        {

        }

        private void hehe(object sender, TabControlEventArgs e)
        {
            //viewfun("viewroom.py", "viewrom.html", webBrowser2);
            //viewfun("viewsubject.py", "viewsub.html", webBrowser1);
            //viewfun("viewteacher.py", "viewtea.html", webBrowser3);
            //viewfun("viewteacher.py", "viewtea.html", webBrowser4);
            //viewfun("viewroom.py", "viewrom.html", webBrowser5);
            //viewfun("viewsubject.py", "viewsub.html", webBrowser6);
           
            
        }

        private void button4_Click(object sender, EventArgs e)
        {
            SQLiteConnection sqliteCon = new SQLiteConnection(connection);
            try
            {
                sqliteCon.Open();

                string query = "delete from teacher where teach_id='" + textBox2.Text + "'";
             
               
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

            viewfun("viewteacher.py", "viewtea.html", webBrowser4);
        }

        private void button5_Click(object sender, EventArgs e)
        {
            SQLiteConnection sqliteCon = new SQLiteConnection(connection);
            try
            {
                sqliteCon.Open();

                string query = "delete from room where room_id='" + textBox1.Text + "'";
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
            viewfun("viewroom.py", "viewrom.html", webBrowser5);
        }

        private void button6_Click(object sender, EventArgs e)
        {
            SQLiteConnection sqliteCon = new SQLiteConnection(connection);
            try
            {
                sqliteCon.Open();

                string query = "delete from subject where sub_id='" + textBox3.Text + "'";
                //Delete 1 records from admin
                //    username='" + textBox1.Text + "'and password='" + textBox2.Text + "'";
                SQLiteCommand command = new SQLiteCommand(query, sqliteCon);
                if (command.ExecuteNonQuery() == 1)
                {
                    MessageBox.Show("deleted");
                   

                }

                sqliteCon.Close();


            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
                sqliteCon.Close();

            }
            viewfun("viewsubject.py", "viewsub.html", webBrowser6);
        }
    }
}
