from matplotlib import pyplot as plt
from matplotlib.widgets import RadioButtons
from datetime import datetime
import pandas as pd

class ShotTracker(object):
    def __init__(self):
        self.x = None
        self.y = None
        self.date = None
        self.time = None
        self.gameid = str(input('Enter the Game ID:'))
        self.data = []
        self.img = plt.imread('newrink.png')
        self.fig, self.ax = plt.subplots(figsize=(10,8))
        self.im = self.ax.imshow(self.img)
        self.ax.autoscale(False)
        plt.subplots_adjust(left=0.25, right=0.98)
        self.axRadio = plt.axes([0.05, 0.4, 0.15, 0.15])
        self.butRadio = RadioButtons(self.axRadio, ('EVS', 'PP', 'SH'))
        self.axRadio2 = plt.axes([0.05, 0.7, 0.15, 0.2])
        self.butRadio2 = RadioButtons(self.axRadio2, ('1ST', '2ND', '3RD', 'OT'))
        self.axRadio3 = plt.axes([0.05, 0.1, 0.15, 0.1])
        self.butRadio3 = RadioButtons(self.axRadio3, ('START', 'STOP'), active=1)
        self.cid = self.fig.canvas.mpl_connect('button_press_event', self.onclick)
        self.close = self.fig.canvas.mpl_connect('close_event', self.closewindow)
        self.msushots = 0
        self.oppshots = 0
        self.period = None
        self.sit = None
        self.status = None
        self.tform = "%H:%M:%S"
        plt.show()


    def onclick(self, event):
        button = event.button
        self.x = event.xdata
        self.y = event.ydata
        self.date = datetime.now().strftime("%m/%d/%y")
        self.time = datetime.now().strftime("%H:%M:%S")
        self.sit = self.butRadio.value_selected
        self.period = self.butRadio2.value_selected

        if button==1:
            if self.x > 0.5:
                self.ax.plot(self.x,self.y,'gh', markersize=12)
                plt.draw()
                team = "MSU"
                self.msushots += 1
                if self.sit == "EVS":
                    stage = 1
                elif self.sit =="PP":
                    stage = 2
                else:
                    stage = 3
                self.listorganizer(team, stage)
        if button!=1:
            self.ax.plot(self.x,self.y,'rh', markersize=12)
            plt.draw()
            team = "OPP"
            self.oppshots += 1
            if self.sit == "EVS":
                stage = 1
            elif self.sit =="PP":
                stage = 2
            else:
                stage = 3
            self.listorganizer(team, stage)


    def listorganizer(self, team, stage):
        record = [self.gameid, self.date, self.time, team, self.x, self.y, self.msushots, self.oppshots, self.sit, self.period, stage]
        self.data.append(record)

    def closewindow(self, event):
        a = self.data
        my_df = pd.DataFrame(a)
        csv_name = self.gameid + '_shots.csv'
        my_df.to_csv(csv_name, index=False, header=['Game ID', 'Date', 'Time', 'Team', 'X', 'Y', 'MSU Shots', 'OPP Shots', 'Situation', 'Period', 'Stage'])


ShotTracker()