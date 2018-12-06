#---------Imports
from numpy import arange, sin, pi
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from tkinter import *
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from BD import  *
#---------End of imports

def GraficoVdiaDolar():


    window = Tk()
    window.title('Variação Dolar')
    label = Label(window, text="Variação do dia dolar").grid(column=0, row=0)

    fig = plt.Figure()
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.get_tk_widget().grid(column=0,row=1)

    ax = fig.add_subplot(111)

    xl = []
    yl = []
    for elemento in consultar_dolar_variacao_dia():
        xl.append(elemento[0])
        yl.append(elemento[1])
    ax.plot(range(len(yl)), yl)

    window.mainloop()


def GraficoVdiaEURO():


    window = Tk()
    window.title('Variação EURO')
    label = Label(window, text="Variação do dia euro").grid(column=0, row=0)

    fig = plt.Figure()
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.get_tk_widget().grid(column=0,row=1)

    ax = fig.add_subplot(111)


    #https://matplotlib.org/tutorials/introductory/sample_plots.html

    #x = np.arange(0, 4*np.pi, 0.01)        # x-array
    xl = []
    yl = []
    for elemento in consultar_euro_variacao_dia():
        xl.append(elemento[0])
        yl.append(elemento[1])
    ax.plot(range(len(yl)), yl)
    #ax.hist(np.random.normal(0, 0.1, 1000), 50)


    #--------- Animation
    #def animate(i):
        #line.set_ydata(np.sin(x+i/10.0))  # update the data
        #return line,

    #line, = ax.plot(x, np.sin(x))
    #ani = animation.FuncAnimation(fig, animate, np.arange(1, 200), interval=25, blit=False)

    window.mainloop()



def GraficoVdiaBTC():


    window = Tk()
    window.title('Variação dolar BTC')
    label = Label(window, text="Variação do dia bitcoin").grid(column=0, row=0)

    fig = plt.Figure()
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.get_tk_widget().grid(column=0,row=1)

    ax = fig.add_subplot(111)


    #https://matplotlib.org/tutorials/introductory/sample_plots.html

    #x = np.arange(0, 4*np.pi, 0.01)        # x-array
    xl = []
    yl = []
    for elemento in consultar_btc_variacao_dia():
        xl.append(elemento[0])
        yl.append(elemento[1])
    ax.plot(range(len(yl)), yl)
    #ax.hist(np.random.normal(0, 0.1, 1000), 50)


    #--------- Animation
    #def animate(i):
        #line.set_ydata(np.sin(x+i/10.0))  # update the data
        #return line,

    #line, = ax.plot(x, np.sin(x))
    #ani = animation.FuncAnimation(fig, animate, np.arange(1, 200), interval=25, blit=False)

    window.mainloop()


#criando graficos do dia anterior

def GraficoVdiaDolarontem():


    window = Tk()
    window.title('Variação dolar ontem')
    label = Label(window, text="Variação de ontem do dolar").grid(column=0, row=0)

    fig = plt.Figure()
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.get_tk_widget().grid(column=0,row=1)

    ax = fig.add_subplot(111)

    xl = []
    yl = []
    for elemento in consultar_dolar_variacao_dia_anterior():
        xl.append(elemento[0])
        yl.append(elemento[1])
    ax.plot(range(len(yl)), yl)

    window.mainloop()


def GraficoVdiaEUROontem():


    window = Tk()
    window.title('Variação euro ontem')
    label = Label(window, text="Variação de ontem do euro").grid(column=0, row=0)

    fig = plt.Figure()
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.get_tk_widget().grid(column=0,row=1)

    ax = fig.add_subplot(111)


    #https://matplotlib.org/tutorials/introductory/sample_plots.html

    #x = np.arange(0, 4*np.pi, 0.01)        # x-array
    xl = []
    yl = []
    for elemento in consultar_euro_variacao_dia_anterior():
        xl.append(elemento[0])
        yl.append(elemento[1])
    ax.plot(range(len(yl)), yl)
    #ax.hist(np.random.normal(0, 0.1, 1000), 50)


    #--------- Animation
    #def animate(i):
        #line.set_ydata(np.sin(x+i/10.0))  # update the data
        #return line,

    #line, = ax.plot(x, np.sin(x))
    #ani = animation.FuncAnimation(fig, animate, np.arange(1, 200), interval=25, blit=False)

    window.mainloop()



def GraficoVdiaBTContem():


    window = Tk()
    window.title('Variação BTC ontem')
    label = Label(window, text="Variação de ontem do bitcoin").grid(column=0, row=0)

    fig = plt.Figure()
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.get_tk_widget().grid(column=0,row=1)

    ax = fig.add_subplot(111)


    #https://matplotlib.org/tutorials/introductory/sample_plots.html

    #x = np.arange(0, 4*np.pi, 0.01)        # x-array
    xl = []
    yl = []
    for elemento in consultar_btc_variacao_dia_anterior():
        xl.append(elemento[0])
        yl.append(elemento[1])
    ax.plot(range(len(yl)), yl)
    #ax.hist(np.random.normal(0, 0.1, 1000), 50)


    #--------- Animation
    #def animate(i):
        #line.set_ydata(np.sin(x+i/10.0))  # update the data
        #return line,

    #line, = ax.plot(x, np.sin(x))
    #ani = animation.FuncAnimation(fig, animate, np.arange(1, 200), interval=25, blit=False)

    window.mainloop()
