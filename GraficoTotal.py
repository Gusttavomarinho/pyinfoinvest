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

def GraficoBarraTotalInvestido():


    window = Tk()
    window.title('Grafico Total investido')
    label = Label(window, text="Grafico Barra Total Investido").grid(column=0, row=0)

    fig = plt.Figure()
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.get_tk_widget().grid(column=0,row=1)

    ax = fig.add_subplot(111)


    #https://matplotlib.org/tutorials/introductory/sample_plots.html

    #x = np.arange(0, 4*np.pi, 0.01)        # x-array
    #coletando os valores para os graficos
    gettotal_tesouro = bd_total_investido(1)
    gettotal_cdb = bd_total_investido(2)
    gettotal_rdb = bd_total_investido(3)
    gettotal_lci = bd_total_investido(4)
    gettotal_lca = bd_total_investido(5)
    gettotal_lc = bd_total_investido(6)
    gettotal_pop = bd_total_investido(7)
    #gerando dicionario estatico
    total_dic = {"Tesouro Direto  ": gettotal_tesouro,"CDB": gettotal_cdb,"RDB": gettotal_rdb,"LCI": gettotal_lci,"LCA": gettotal_lca,"LC": gettotal_lc,"Poupança": gettotal_pop}
    #pegandos nomes e valores
    nomes_investimentos  = total_dic.keys()
    valores_investimento = total_dic.values()
    #ax.plot(range(len(yl)), yl)
    ax.bar(nomes_investimentos,valores_investimento)


    #--------- Animation
    #def animate(i):
        #line.set_ydata(np.sin(x+i/10.0))  # update the data
        #return line,

    #line, = ax.plot(x, np.sin(x))
    #ani = animation.FuncAnimation(fig, animate, np.arange(1, 200), interval=25, blit=False)

    window.mainloop()

def GraficoPlotTotalInvestido():


    window = Tk()
    window.title('Grafico Total investido')
    label = Label(window, text="Grafico Plot Total Investido").grid(column=0, row=0)

    fig = plt.Figure()
    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.get_tk_widget().grid(column=0,row=1)

    ax = fig.add_subplot(111)


    #https://matplotlib.org/tutorials/introductory/sample_plots.html

    #x = np.arange(0, 4*np.pi, 0.01)        # x-array
    #coletando os valores para os graficos
    gettotal_tesouro = bd_total_investido(1)
    gettotal_cdb = bd_total_investido(2)
    gettotal_rdb = bd_total_investido(3)
    gettotal_lci = bd_total_investido(4)
    gettotal_lca = bd_total_investido(5)
    gettotal_lc = bd_total_investido(6)
    gettotal_pop = bd_total_investido(7)
    #gerando dicionario estatico
    total_dic = {"Tesouro Direto  ": gettotal_tesouro,"CDB": gettotal_cdb,"RDB": gettotal_rdb,"LCI": gettotal_lci,"LCA": gettotal_lca,"LC": gettotal_lc,"Poupança": gettotal_pop}
    #pegandos nomes e valores
    nomes_investimentos  = total_dic.keys()
    valores_investimento = total_dic.values()
    #ax.plot(range(len(yl)), yl)
    ax.plot(nomes_investimentos,valores_investimento)


    #--------- Animation
    #def animate(i):
        #line.set_ydata(np.sin(x+i/10.0))  # update the data
        #return line,

    #line, = ax.plot(x, np.sin(x))
    #ani = animation.FuncAnimation(fig, animate, np.arange(1, 200), interval=25, blit=False)

    window.mainloop()