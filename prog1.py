#подключаем библиотеки 
import math
#Импортируем один из пакетов Matplotlib
import pylab
#Импортируем пакет со вспомогательными функциями
from matplotlib import mlab
lag= input("Хотите построить график sinx или cosx   ")
if lag=='sinx':
  #Рисуем график функции y = sin(x)
  def func (x):
  #  """sin(x)"""
   return math.sin (x)
  #Указываем X наименьее и наибольшее вводится
  xmin =float(input("xmin: "))
  xmax =float(input("xmax: "))
  dx =float(input("dx: "))
  #Создадим список координат по оси 
  #X на отрезке [-xmin; xmax], включая концы
  xlist = mlab.frange (xmin, xmax, dx)
   # Вычислим значение функции в заданных точках
  ylist = [func (x) for x in xlist]
   #Нарисуем одномерный график
  pylab.plot (xlist, ylist)
#Покажем окно с нарисованным графиком
  pylab.show()
else:
  print("ну к")
  def func (x):
  #  """cos(x)"""
   return math.cos (x)
  #Указываем X наименьее и наибольшее вводится
  xmin =float(input("xmin: "))
  xmax =float(input("xmax: "))
  dx =float(input("dx: "))
  #Создадим список координат по оси 
  #X на отрезке [-xmin; xmax], включая концы
  xlist = mlab.frange (xmin, xmax, dx)
   # Вычислим значение функции в заданных точках
  ylist = [func (x) for x in xlist]
   #Нарисуем одномерный график
  pylab.plot (xlist, ylist)

   #Покажем окно с нарисованным графиком
  pylab.show()

print("ffff")