using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Navigation;
using System.Windows.Shapes;
using System.Collections.Generic;
using System.Windows.Forms;

namespace Competence
{
    /// <summary>
    /// Логика взаимодействия для MainWindow.xaml
    /// </summary>
    public partial class MainWindow : Window
    {
        public MainWindow()
        {
            InitializeComponent();
             //List<string> kompet = new List<string>();
            //kompet.Add(komp1.SelectedItem.ToString());
        }
// string[] kompet1, kompet2, kompet3, kompet4, kompet5, kompet6, kompet7;

        List<string> kompet = new List<string>();
        List<string> kompett2 = new List<string>();
        List<string> kompett3 = new List<string>();
        //List<string> kompet = new List<string>();
        private void comboBox_SelectionChanged(object sender, SelectionChangedEventArgs e)
        {
            int i = 0;
            
            komp1.Items.Clear();
            //textBox.Clear(); 
            if (comboBox.SelectedIndex == 0) 
            {
                komp1.Items.Add("ОК-1"); komp1.Items.Add("ОК-2"); komp1.Items.Add("ОК-3"); komp1.Items.Add("ОК-4"); komp1.Items.Add("ОК-5");
                //kompet.Add(listBox1.SelectedItem.ToString());
            }
            
            if (comboBox.SelectedIndex == 1)
            {
                komp1.Items.Add("ОПК-2"); komp1.Items.Add("ОПК-3");
                //kompett2.Add(listBox1.SelectedItem.ToString());
            }
            if (comboBox.SelectedIndex == 2)
            {
                komp1.Items.Add("ПК-23");
                //kompett3.Add(listBox1.SelectedItem.ToString());
            }
            // komp[i] = komp1.SelectedItem.ToString();
            //textBox_Copy.Text += kompet[0];
            
        }
        
        private void listBox_SelectionChanged(object sender, SelectionChangedEventArgs e)
        {
            
            textBox.Text = komp1.SelectedItem.ToString();
            if (komp1.SelectedIndex == 0)
            {
                kompet.Add(listBox1.SelectedItem.ToString());

            }
            if (komp1.SelectedIndex == 1)
            {
                kompett2.Add(listBox1.SelectedItem.ToString());

            }
            if (komp1.SelectedIndex == 2)
            {
                kompett3.Add(listBox1.SelectedItem.ToString());

            }
            // textBox_Copy.Text = listBox_com.SelectedItem.ToString();
        }

        private void listBox1_SelectionChanged(object sender, SelectionChangedEventArgs e)
        {
            textBox2.Text = listBox1.SelectedItem.ToString(); 
        }

        private void ListBoxItem_Selected(object sender, RoutedEventArgs e)
        {
           // textBox_Copy.Text = listBox_com.SelectedItem.ToString();
        }

        private void comboBox1_SelectionChanged(object sender, SelectionChangedEventArgs e)
        {

        }

        public void zakrep_komp(string path) {
           // List<string> kompet = new List<string>();
           // kompet.Add(komp1.SelectedItem.ToString());
        }


    }
}
