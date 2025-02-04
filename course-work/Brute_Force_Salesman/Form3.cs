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
    public partial class Form3 : Form
    {
        private ListView listview;
        private Button button;
        public Form3(int minDist, List<int> list)
        {
            InitializeComponent();
            myInit();
            ListViewItem row1 = new ListViewItem(minDist.ToString());
            row1.SubItems.Add(list[0].ToString());
            double diff = Math.Abs(list[0]-minDist);
            if (diff == 0)
            {
                row1.SubItems.Add("0");
            }
            else 
            {
                row1.SubItems.Add((diff * 100 / minDist).ToString("#.###"));
            }
            listview.Items.Add(row1);
            for (int i = 1; i < list.Count; i++) {
                ListViewItem item = new ListViewItem("");
                item.SubItems.Add(list[i].ToString());
                diff = Math.Abs(list[i]-minDist);
                if (diff == 0)
                {
                    item.SubItems.Add("0");
                }
                else
                {
                    item.SubItems.Add((diff * 100 / minDist).ToString("#.###"));
                }
                listview.Items.Add(item);
            }
        }
        private void myInit() 
        {
            listview = new ListView
            {
                View = View.Details,
                FullRowSelect = true,
                GridLines = true,
                Width = 1000,
                Height = 400,
                Location = new Point(350, 100),
                Font = new Font("", 19, FontStyle.Bold)
            };
            button = new Button
            {
                Text = "ԱՐԴՅՈՒՆՔՆԵՐԻ ՎԵՐԼՈՒԾՈՒԹՅՈՒՆ",
                Font = new Font("Arial", 20, FontStyle.Bold), 
                Location = new Point(590, 10),
                Width = 550, 
                Height = 60, 
                BackColor = Color.MidnightBlue, 
                ForeColor = Color.White,
                FlatStyle = FlatStyle.Flat, 
                TextAlign = ContentAlignment.MiddleCenter 
            };
            listview.Columns.Add("ԼՐԻՎ ՈՐՈՆՄԱՆ ԱԼԳՈՐԻԹՄ", 400);
            listview.Columns.Add("ԺԼԱՏ ԱԼԳՈՐԻԹՄ", 300);
            listview.Columns.Add("ՏԱՐԲԵՐՈՒԹՅՈՒՆ(%)", 300);
            Controls.Add(listview);
            Controls.Add(button);
            listview.BringToFront();
            button.BringToFront();
        }
        private void Form3_Load_1(object sender, EventArgs e)
        {
            pictureBox1.Left = 0;
            pictureBox1.Top = 0;
            pictureBox1.Width = 1550;
            pictureBox1.Height = 870;
        }
        private void button1_Click(object sender, EventArgs e)
        {
            this.Close();
            listview.Clear();
        }
    }
}
