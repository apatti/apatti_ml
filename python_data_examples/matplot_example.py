__author__ = 'apatti'

from matplotlib import pyplot as plt
import numpy as np

class MultiPanelPlot:

    @staticmethod
    def insetPlot():
        """
        The add_axes method allows you to create an axes instance by specifying the size relative to the figure edges.
        The argument is [left, bottom, width, height] which specifies the axes extent in fractions of the figure size (i.e. between 0 and 1):
        """
        fig = plt.figure()
        main_ax = fig.add_axes([0.1,0.1,0.8,0.8])
        inset_ax = fig.add_axes([0.6,0.6,0.25,0.25])
        main_ax.plot(np.random.rand(100),color="gray")
        inset_ax.plot(np.random.rand(20),color="green")
        plt.show()
        pass

    @staticmethod
    def simpleMultiPanel():

        """
        create a simple multi-panel graph using add_subplot
        :return: None
        """
        fig = plt.figure()
        for i in range(1,7):
            ax = fig.add_subplot(2,3,i)
            #to add text
            #ax.text(0.45,0.45,str(i),fontsize=24)
            ax.plot(np.random.rand(20))

        #to add spaces.
        fig.subplots_adjust(left=0.1, right=0.9,
                    bottom=0.1, top=0.9,
                    hspace=0.4, wspace=0.4)
        plt.show()

    @staticmethod
    def multipleSubplots():
        fig,axes = plt.subplots(nrows=2,ncols=3,sharex=True,sharey=True)
        for i in range(2):
            for j in range(3):
                axes[i][j].plot(np.random.rand(20))
                #axes[i][j].text(0.45,0.45,str((i,j)),fontsize=24)
        plt.show()

    @staticmethod
    def gridSpecPlot():
        """
        GridSpec is the highest-level routine for creating subplots.
        It's an abstract object that allows the creation of multi-row or multi-column subplots via an intuitive slicing interface
        :return: None
        """
        gs = plt.GridSpec(3,3,wspace=0.4,hspace=0.4) # a 3x3 grid
        fig = plt.figure(figsize=(6,6))
        fig.add_subplot(gs[1,:2])
        fig.add_subplot(gs[0,:2])
        fig.add_subplot(gs[:2,2])
        fig.add_subplot(gs[2,1:])
        fig.add_subplot(gs[2,0])
        plt.show()

if __name__ == '__main__':

    MultiPanelPlot.insetPlot()
    MultiPanelPlot.simpleMultiPanel()
    MultiPanelPlot.multipleSubplots()
    MultiPanelPlot.gridSpecPlot()