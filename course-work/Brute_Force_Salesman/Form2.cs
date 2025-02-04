using System;
using System.Collections.Generic;
using System.Drawing;
using System.Linq;
using System.Threading.Tasks;
using System.Windows.Forms;
namespace Brute_Force_Salesman
{
    public partial class Form2 : Form
    {
        private Label label1;
        private Label label2;
        private Label label3;
        private ListView listview1;
        private ListView listview2;
        private TextBox textBox;
        private Button button;
        private Button submitButton;
        private int quantity = 0;
        private List<int> myList = new List<int>();
        private int[,] arr;
        private int n;
        private int minDistF = int.MaxValue;
        private int minDistG = int.MaxValue;
        private bool flag = false;
        private string[,] arr2;
        private int minG;
        private string[] greedyResults = Array.Empty<string>();
        private string[] bruteResults = Array.Empty<string>();
        public Form2()
        {
            InitializeComponent();
            this.BackColor = Color.White;
        }
        private void InitCompon()
        {
            textBox = new TextBox
            {
                Location = new Point(650, 50),
                Font = new Font("Arial", 15, FontStyle.Bold),
                Width = 100,
                Height = 30
            };
            submitButton = new Button
            {
                Text = "Ընդունել",
                Location = new Point(690, 400),
                Width = 150,
                Height = 40,
                Font = new Font("Arial", 15, FontStyle.Bold),
                BackColor = Color.DarkOrange,
                ForeColor = Color.White,
                
            };
            Controls.Add(submitButton);
            submitButton.Click += SubmitButton_Click;
            button = new Button
            {
                Location = new Point(750, 50),
                Text = "Հաստատել",
                Font = new Font("Arial", 10, FontStyle.Bold),
                BackColor = Color.DarkOrange,
                ForeColor = Color.White,
                Width = 100,
                Height = 30
            };
            button.Click += NumericInputValueChanged;
            label1 = new Label
            {
                Location = new Point(570, 10),
                Text = "Մուտքագրել քաղաքների քանակը",
                Font = new Font("Arial", 15, FontStyle.Bold),
                Width = 372,
                Height = 35,
                BackColor = Color.LightSlateGray,
                ForeColor  = Color.White,
                TextAlign = ContentAlignment.MiddleCenter
            };
            label2 = new Label
            {
                Location = new Point(10, 10),
                Text = "Լուծումը՝ լրիվ որոնման ալգորիթմով",
                Font = new Font("Arial", 15, FontStyle.Bold),
                Width = 550,
                Height = 33,
                BackColor = Color.MidnightBlue,
                ForeColor = Color.White,
                TextAlign = ContentAlignment.MiddleCenter
            };
            label3 = new Label
            {
                Location = new Point(950, 10),
                Text = "Լուծումը՝ ժլատ ալգորիթմով",
                Font = new Font("Arial", 15, FontStyle.Bold),
                Width = 550,
                Height = 35,
                BackColor = Color.MidnightBlue,
                ForeColor = Color.White,
                TextAlign = ContentAlignment.MiddleCenter
            };
            listview1 = new ListView
            {
                View = View.Details,
                FullRowSelect = true,
                GridLines = true,
                Width = 550,
                Height = 300,
                Location = new Point(10, 100),
                Font = new Font("", 20, FontStyle.Bold),
            };
            listview2 = new ListView
            {
                View = View.Details,
                FullRowSelect = true,
                GridLines = true,
                Width = 550,
                Height = 300,
                Location = new System.Drawing.Point(950, 100),
                Font = new Font("", 20, FontStyle.Bold)
            };
            listview1.Columns.Add("         ԵՐԹՈՒՂԻ", 300);
            listview1.Columns.Add("ԵՐԿԱՐՈՒԹՅՈՒՆ", 300);
            listview2.Columns.Add("         ԵՐԹՈՒՂԻ", 300);
            listview2.Columns.Add("ԵՐԿԱՐՈՒԹՅՈՒՆ", 300);
            Controls.Add(label1);
            Controls.Add(label2);
            Controls.Add(label3);
            Controls.Add(listview1);
            Controls.Add(listview2);
            Controls.Add(textBox);
            Controls.Add(button);
            Text = "TSP";
            label1.BringToFront();
            label2.BringToFront();
            label3.BringToFront();
            listview1.BringToFront();
            listview2.BringToFront();
            textBox.BringToFront();
            button.BringToFront();
            submitButton.BringToFront();
        }
        private int CalculateTotalSeconds(DateTime dt1, DateTime dt2)
        {
            int hourDifference = dt2.Hour - dt1.Hour;
            int minuteDifference = dt2.Minute - dt1.Minute;
            int secondDifference = dt2.Second - dt1.Second;
            if (secondDifference<0)
            {
                secondDifference += 60;
                minuteDifference -= 1;
            }
            if(minuteDifference<0)
            {
                minuteDifference += 60;
                hourDifference -= 1;
            }
            int totalSeconds = hourDifference * 3600 + minuteDifference * 60 + secondDifference;
            return totalSeconds;
        }
        private void NumericInputValueChanged(object sender, EventArgs e)
        {
            
            if (!string.IsNullOrEmpty(textBox.Text) && int.TryParse(textBox.Text, out n) && n>=3)
            {
                arr = new int[n, n];
                DialogResult result = MessageBox.Show("Ուզո՞ւմ եք գեներացնել քաղաքների միջև հեռավորությունները պատահական ձևով", "Մատրիցայի ներմուծում", MessageBoxButtons.YesNo, MessageBoxIcon.Question );
                if (result == DialogResult.Yes)
                {
                    flag = false;
                    Random random = new Random();
                    for (int i = 0; i < n; i++)
                    {
                        for (int j = 0; j < n; j++)
                        {
                            arr[i, j] = (i == j) ? 0 : random.Next(1, 31);
                        }
                    }
                    Display(arr,arr2, n, flag);
                    Application.DoEvents();
                    listview1.Items.Clear();  
                    listview2.Items.Clear();
                    RunAnalysis();
                    button1.Enabled = true;
                }
                else 
                {
                    arr2 = new string[n, n];
                    for (int i = 0; i < n; i++)
                    {
                        for (int j = 0; j < n; j++)
                            if (i != j)
                            {
                                arr2[i, j] = null;
                            }
                            else
                            {
                                arr2[i, j] = "0";
                            }
                    }
                    flag = true;
                    Display(arr,arr2, n, flag);
                    MessageBox.Show("Խնդրում ենք ներմուծել արժեքները և սեղմել ընդունել կոճակը վերջում", "Օգտվողի ներմուծվող արժեքներ", MessageBoxButtons.OK, MessageBoxIcon.Information);
                }
                submitButton.Left = 690;
            }
            else
            {
                MessageBox.Show("Ներմուծեք քաղաքների վավեր քանակ", "Զգուշացում", MessageBoxButtons.OK, MessageBoxIcon.Warning);
            }
        }
        private async void RunAnalysis()
        {
            DateTime dtGreedyStart = DateTime.Now;
            await Task.Run(() => FindShortestGreedy(arr, n));
            DateTime dtGreedyEnd = DateTime.Now;
            greedyResults = new[]
            {
                $"Սկիզբ: {dtGreedyStart}",
                $"Ավարտ: {dtGreedyEnd}",
                $"Տևողություն: {CalculateTotalSeconds(dtGreedyStart, dtGreedyEnd)} վրկ",
                $"Քանակ: {n}",
                $"Փոքրագույն: {minG}"
            };
            pictureBox1.Invalidate();
            DateTime dtBruteStart = DateTime.Now;
            bruteResults = new[] { $"Սկիզբ: {dtBruteStart}" };
            pictureBox1.Invalidate();
            await Task.Run(() => FindShortestBrute(arr, n));
            DateTime dtBruteEnd = DateTime.Now;
            bruteResults = new[]
            {
                $"Սկիզբ: {dtBruteStart}",
                $"Ավարտ: {dtBruteEnd}",
                $"Տևողություն: {CalculateTotalSeconds(dtBruteStart, dtBruteEnd)} վրկ",
                $"Քանակ: {quantity}",
                $"Փոքրագույն: {minDistF}"
            };
            pictureBox1.Invalidate();
        }
        private void pictureBox1_Paint(object sender, PaintEventArgs e)
        {
            Graphics obj = e.Graphics;
            Font textFont = new Font("Arial", 16, FontStyle.Italic);
            Brush textBrush = new SolidBrush(Color.Black);
            int rectX = 10, rectY = 450, rectWidth = 550, rectHeight = 230;
            obj.FillRectangle(new SolidBrush(Color.White), rectX, rectY, rectWidth, rectHeight);
            obj.FillRectangle(new SolidBrush(Color.White), rectX + rectWidth + 390, rectY, rectWidth, rectHeight); 
            int textX = rectX + rectWidth + 400, textY = rectY + 10;
            foreach (var line in greedyResults)
            {
                obj.DrawString(line, textFont, textBrush, textX, textY);
                textY += 40;
            }
            textX = rectX + 10;
            textY = rectY + 10;
            foreach (var line in bruteResults)
            {
                obj.DrawString(line, textFont, textBrush, textX, textY);
                textY += 40;
            }
        }
        private void SubmitButton_Click(object sender, EventArgs e)
        {
            bool isValid = true;  
            foreach (Control control in Controls)
            {
                if (control is TextBox textBox && textBox.Tag != null)
                {
                    string tag = textBox.Tag.ToString();
                    if (tag.StartsWith("txt_"))
                    {
                        string[] indices = tag.Split('_');
                        int i = int.Parse(indices[1]);
                        int j = int.Parse(indices[2]);
                        if (i == j && int.TryParse(textBox.Text, out int val1) && val1 != 0)
                        {
                            MessageBox.Show($"Անկյունագծի արժեքները չեն կարող փոփոխվել, քանի որ քաղաքի հեռավորությունը իրենից 0 է", "", MessageBoxButtons.OK, MessageBoxIcon.Warning);
                            isValid = false;
                            break;
                        }
                        else if (string.IsNullOrWhiteSpace(textBox.Text))
                        {
                            MessageBox.Show($"Ունեք բացթողնված վանդակներ", "Զգուշացում", MessageBoxButtons.OK, MessageBoxIcon.Warning);
                            isValid = false;
                            break;
                        }
                        else if (i != j && int.TryParse(textBox.Text, out int val2) && val2 <= 0)
                        {
                            MessageBox.Show($"Քաղաքից քաղաք հեռավորությունները պետք է լինեն մեծ 0-ից", "Զգուշացում", MessageBoxButtons.OK, MessageBoxIcon.Warning);
                            isValid = false;
                            break;
                        }
                        else if (int.TryParse(textBox.Text, out int val3))
                        {
                            arr[i, j] = val3;
                        }
                        else
                        {
                            MessageBox.Show($"Ներմուծեք վավեր տվյալներ", "Զգուշացում", MessageBoxButtons.OK, MessageBoxIcon.Warning);
                            isValid = false;
                            break;
                        }
                    }
                }
            }
            if (isValid)
            {
                Application.DoEvents();
                listview1.Items.Clear();
                listview2.Items.Clear();
                RunAnalysis();
                button1.Enabled = true;
            }
        }
        private void Display(int[,] arr, string[,] arr2, int n, bool flag)
        {
            foreach (Control control in Controls.OfType<TextBox>().ToList())
            {
                if(control.Tag!=null && control.Tag.ToString().StartsWith("txt_")){
                    Controls.Remove(control);
                    control.Dispose();
                } 
            }
            int startX = 600;
            int startY = 100;
            int GridWidth = 300;
            int GridHeight = 300;
            int buttonWidth = GridWidth / n;
            int buttonHeight = GridHeight / n;
            if (flag)
            {
                for (int i = 0; i < n; i++)
                {
                    for (int j = 0; j < n; j++)
                    {
                        TextBox mtext = new TextBox
                        {
                            Text = arr2[i,j],
                            Width = buttonWidth - 2,
                            Height = buttonHeight - 2,
                            BackColor = Color.DarkRed,
                            ForeColor = Color.White,
                            Location = new Point(startX + j * buttonWidth, startY + i * buttonHeight),
                            Font = new Font("Arial", Math.Max(8, buttonHeight / 2)),
                            TextAlign = HorizontalAlignment.Center,
                            Tag = $"txt_{i}_{j}",
                            Multiline = true
                        };
                        Controls.Add(mtext);
                        mtext.BringToFront();
                    }
                }
            }
            else 
            {
                for (int i = 0; i < n; i++)
                {
                    for (int j = 0; j < n; j++)
                    {
                        TextBox mtext = new TextBox
                        {
                            Text = arr[i, j].ToString(),
                            Width = buttonWidth - 2,
                            Height = buttonHeight - 2,
                            BackColor = Color.DarkRed,
                            ForeColor = Color.White,
                            Location = new Point(startX + j * buttonWidth, startY + i * buttonHeight),
                            Font = new Font("Arial", Math.Max(8, buttonHeight / 2)),
                            TextAlign = HorizontalAlignment.Center,
                            Tag = $"txt_{i}_{j}",
                            Multiline = true
                        };
                        Controls.Add(mtext);
                        mtext.BringToFront();

                    }
                }
            }
        }
        private int DistanceCalc(int[,] arr, int[] cities, int n, int stCity)
        {
            int distance = 0;
            for (int i = 0; i < n - 1; ++i)
            {
                distance += arr[cities[i], cities[i + 1]];
            }
            distance += arr[cities[n - 1], stCity];
            return distance;
        }
        private void FindShortestGreedy(int[,] arr, int n)
        {
            minG = int.MaxValue;
            myList.Clear();
            for (int i = 0; i < n; i++)
            {
                bool[] visited = new bool[n];
                int[] route = new int[n + 1];
                int totalDistance = 0;
                int currentCity = i;
                visited[currentCity] = true;
                route[0] = currentCity;
                for (int k = 1; k < n; k++)
                {
                    int nextCity = -1;
                    minDistG = int.MaxValue;
                    for (int j = 0; j < n; j++)
                    {
                        if (!visited[j] && arr[currentCity, j] < minDistG)
                        {
                            minDistG = arr[currentCity, j];
                            nextCity = j;
                        }
                    }
                    if (nextCity != -1)
                    {
                        visited[nextCity] = true;
                        route[k] = nextCity;
                        totalDistance += minDistG;
                        currentCity = nextCity;
                    }
                }
                totalDistance += arr[currentCity, route[0]];
                if (minG > totalDistance)
                {
                    minG = totalDistance;
                }
                myList.Add(totalDistance);
                route[n] = route[0];
                string sequence = "";
                for (int i1 = 0; i1 < n; i1++)
                {
                    sequence += (route[i1] + 1).ToString();
                    sequence += " ";
                };
                sequence += (route[0] + 1).ToString();
                AddToListView(sequence, totalDistance, listview2);
            }
            quantity = listview2.Items.Count;
            for (int i1 = 0; i1 < quantity; ++i1)
            {
                if (string.Compare(listview2.Items[i1].SubItems[1].Text, Convert.ToString(minG)) == 0)
                    listview2.Items[i1].ForeColor = Color.Red;
            }
        }
        private void FindShortestBrute(int[,] arr, int n)
        {
            minDistF = int.MaxValue;
            int[] cities = new int[n];
            for (int i = 0; i < n; ++i)
            {
                cities[i] = i;
            }
            int[] bestRoute = new int[n + 1];
            while (true)
            {
                int stCity = cities[0];
                int currDistance = DistanceCalc(arr, cities, n, stCity);
                if (currDistance < minDistF)
                {
                    minDistF = currDistance;
                    Array.Copy(cities, bestRoute, n);
                    bestRoute[n] = stCity;
                }
                string route = "";
                for (int i = 0; i < cities.Length; ++i)
                {
                    route += (cities[i] + 1).ToString();
                    route += "  ";
                }
                route += (cities[0] + 1).ToString();
                AddToListView(route, currDistance, listview1);
                int iIndex = n - 2;
                while (iIndex >= 0 && cities[iIndex] > cities[iIndex + 1])
                {
                    iIndex--;
                }
                if (iIndex == -1)
                    break;
                int jIndex = n - 1;
                while (cities[iIndex] > cities[jIndex])
                {
                    jIndex--;
                }
                (cities[iIndex], cities[jIndex]) = (cities[jIndex], cities[iIndex]);
                int startIdx = iIndex + 1, endIdx = n - 1;
                while (startIdx < endIdx)
                {
                    (cities[startIdx], cities[endIdx]) = (cities[endIdx], cities[startIdx]);
                    startIdx++;
                    endIdx--;
                }
            }
            quantity = listview1.Items.Count;
            for (int i1 = 0; i1 < quantity; ++i1)
            {
                if (string.Compare(listview1.Items[i1].SubItems[1].Text, Convert.ToString(minDistF)) == 0)
                    listview1.Items[i1].ForeColor = Color.Red;
            }
        }
        private void AddToListView(string sequence, int distance, ListView listView)
        {
            var item = new ListViewItem(sequence);
            item.SubItems.Add(distance.ToString());
            listView.Items.Add(item);
        }
        private void Form2_Load(object sender, EventArgs e)
        {
            pictureBox1.Left = 0;
            pictureBox1.Top = 0;
            pictureBox1.Width = 1550;
            pictureBox1.Height = 870;
            pictureBox1.Paint += pictureBox1_Paint;
            InitCompon();
            button1.Enabled = false;
            submitButton.Left = -200;
        }
        private void button1_Click(object sender, EventArgs e)
        {
            Form3 form = new Form3(minDistF, myList);
            form.Show();
        }
        private void button2_Click(object sender, EventArgs e)
        {
            Form1 form = new Form1();
            form.Show();
        }
        private void button3_Click(object sender, EventArgs e)
        {
            DialogResult result = MessageBox.Show("Ցանկանո՞ւմ եք դուրս գալ ծրագրից", "Ավարտ", MessageBoxButtons.YesNo, MessageBoxIcon.Question);
            if (result == DialogResult.Yes)
            {
                Application.Exit();
            }
        }
        private void pictureBox1_Click(object sender, EventArgs e)
        {
        }
    }
}