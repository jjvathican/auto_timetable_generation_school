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
    public partial class Form1 : Form
    {
        string connection = @"Data Source=C:\Users\jj\PycharmProjects\projects\data.sqlite;Version=3;";
        public Form1()
        {
            InitializeComponent();
           
        }

      

      private void Form1_Load(object sender, EventArgs e)
        {
            groupBox1.Enabled = false;
            groupBox3.Enabled = false;
            viewfun("data2view.py", "viewdata.html", webBrowser1);
        }

      private void label1_Click(object sender, EventArgs e)
      {

      }

      private void button1_Click(object sender, EventArgs e)
      {
          add f1 = new add();
          f1.Show();
      }

      private void button4_Click(object sender, EventArgs e)
      {
          
          SQLiteConnection sqliteCon = new SQLiteConnection(connection);
            try
            {
                sqliteCon.Open();
                string query = "select * from admin where username='" + textBox1.Text + "'and password='" + textBox2.Text + "'";
                
                SQLiteCommand command = new SQLiteCommand(query, sqliteCon);
                command.ExecuteNonQuery();
                SQLiteDataReader dr = command.ExecuteReader();
                int count = 0;

                while (dr.Read())
                {
                    //MessageBox.Show(dr.GetString(1));
                    count++;
                }
                sqliteCon.Close();
                if (count == 1)
                {

                    MessageBox.Show("welcome");
                    groupBox1.Enabled = true;
                    groupBox3.Enabled = true;
                }
                else
                {
                    MessageBox.Show("wrong  username or password ");
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message);
                sqliteCon.Close();
            }
           
      }

      private void button2_Click(object sender, EventArgs e)
      {
          setup f1 = new setup();
          f1.Show();
      }

      private void button3_Click(object sender, EventArgs e)
      {
          generate f2 = new generate();
          f2.Show();
      }

      private void button5_Click(object sender, EventArgs e)
      {
         
          view f1 = new view();
          f1.Show();

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

      private void button6_Click(object sender, EventArgs e)
      {
          viewfun("data2view.py", "viewdata.html", webBrowser1);
      }

      private void button7_Click(object sender, EventArgs e)
      {
          admin f1 = new admin();
          f1.Show();
      }

      private void button8_Click(object sender, EventArgs e)
      {
          adminremove f1 =new adminremove();
          f1.Show();
      }

      private void button9_Click(object sender, EventArgs e)
      {
          webBrowser1.Print();
      }

      private void button10_Click(object sender, EventArgs e)
      {
          SQLiteConnection sqliteCon = new SQLiteConnection(connection);
          try
          {
              sqliteCon.Open();

              string query = "delete from data2view ";


              //Delete 1 records from admin
              //    username='" + textBox1.Text + "'and password='" + textBox2.Text + "'";
              SQLiteCommand command = new SQLiteCommand(query, sqliteCon);
              if (command.ExecuteNonQuery() == 1)
              {
                  MessageBox.Show("deleted data2view table");
                  
              }

              string query1 = "update  sqlite_sequence set seq=0 where name='data2view'";
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
       //   SQLiteConnection sqliteCon = new SQLiteConnection(connection);
          try
          {
              sqliteCon.Open();

              string query = "delete from data2 ";


              //Delete 1 records from admin
              //    username='" + textBox1.Text + "'and password='" + textBox2.Text + "'";
              SQLiteCommand command = new SQLiteCommand(query, sqliteCon);
              if (command.ExecuteNonQuery() == 1)
              {
                  MessageBox.Show("deleted data2 table");

              }

              string query1 = "update  sqlite_sequence set seq=0 where name='data2'";
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
          viewfun("data2view.py", "viewdata.html", webBrowser1);
      }
    }
}
