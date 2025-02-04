using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Brute_Force_Salesman
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }
        private void Form1_Load(object sender, EventArgs e)
        {
            pictureBox1.Left = 0;
            pictureBox1.Top = 0;
            pictureBox1.Width = 1550;
            pictureBox1.Height = 870;
            InitComp();
            
        }
        private void InitComp()
        {
            label1.Text = "Կուրսային աշխատանք";
            label1.Font = new Font("Sylfaen", 40, FontStyle.Bold | FontStyle.Italic);
            label1.Location = new Point(500, 103);
            label1.BackColor = Color.Lavender;

            label3.Text =
                "\n  " +
                "Թեմա՝          Լրիվ որոնման և ժլատ ալգորիթմներով շրջիկ գործակալի \n" +
                "                               խնդրի լուծման համեմատական վերլուծություն \n" +
                "  Բաժին՝         ԻԿՄ\n  " +
                "Կուրս՝          4-րդ\n  " +
                "Ուսանող՝    Լիլիթ Ասատրյան\n" +
                "  Ղեկավար՝   Ռ. Մազմանյան\n  ";
            label3.Font = new Font("Sylfaen", 25, FontStyle.Bold);
            label3.Location = new Point(250, 250);
            label3.BackColor = Color.Lavender;
            button1.Text = "Ծրագրի կատարում";
            button1.Font = new Font("Sylfaen", 18, FontStyle.Bold);
            button1.Location = new Point(700, 700);
            button1.BackColor = Color.Lavender;


        }
        private void button1_Click(object sender, EventArgs e)
        {
            Form2 form = new Form2();
            form.Show();
        }
        private void label1_Click(object sender, EventArgs e)
        {
        }
        private void label3_Click(object sender, EventArgs e)
        {
        }

        private void pictureBox1_Click(object sender, EventArgs e)
        {
        }
    }
}
