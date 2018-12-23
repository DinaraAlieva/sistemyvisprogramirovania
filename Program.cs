using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
namespace zach
{
class Program
{
		static void Main(string[] args)
		{
			int n;
			Console.Write("Введите n: ");
			n = Convert.ToInt32(Console.ReadLine());
            double [] mas = new double[n];
			Random r = new Random();
			double  c = 0;
			for (int i = 0; i < n; i++)
			{
			    mas[i] = r.NextDouble() * 100;
				Console.Write(mas[i] + " ");
				if (mas[i] > c)
				c = mas[i];
				Console.Write(mas[i] + " "); 
			}
			Console.Write( "                         ");
			Console.Write(c + " max element");
			Console.ReadKey();
		}
	}
}
