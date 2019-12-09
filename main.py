import tkinter as tk
from math import gcd

class dpi_calc:
    def __init__(self):
        self.app = tk.Tk()
        self.app.title("DPI Calculator")
        
        label_texts = [
            'Enter the horizontal pixel count: ',
            'Enter the vertical pixel count: ',
            'Width of the monitor: ',
            'height of the monitor: '
        ]

        N = len(label_texts)

        Labels = []
        
        for label_text in label_texts:
            Labels.append(tk.Label(self.app, text=label_text))
        
        #Setting their location via the grid functions. 

        for index, label in enumerate(Labels):
            label.grid(row=index, column=0)

        #Entries. 
        Entries = [] 
        self.StringVariables = [tk.StringVar() for _ in range(N)]

        for i in range(N):
            Entries.append(tk.Entry(self.app, textvariable=self.StringVariables[i]))

        #Packing, and binding entries.
        for i in range(N):
            Entries[i].grid(row=i, column=1)
            Entries[i].bind("<KeyRelease>", self.on_value_changed)
        
        self.dpi = tk.StringVar()
        self.ratio = tk.StringVar()

        tk.Label(self.app, text="", textvariable=self.dpi).grid(row=N)
        tk.Label(self.app, text="", textvariable=self.ratio).grid(row=N+1)

        self.app.mainloop()


    def calc_dpi(self, mw, mh, pw, ph):
        pixel_area = pw*ph 
        monitor_area = mw*mh 
        return pixel_area/monitor_area

    def aspect_ratio(self, x, y):
        div = gcd(x, y)
        return f'{x//div}:{y//div}'

    def on_value_changed(self, event):
        try:
            pw = int(self.StringVariables[0].get().strip())
            ph = int(self.StringVariables[1].get().strip())
            mw = int(self.StringVariables[2].get().strip())
            mh = int(self.StringVariables[3].get().strip())
            dpi = self.calc_dpi(mw, mh, pw, ph)
            ar = self.aspect_ratio(pw, ph)
            self.dpi.set(f'The value of dpi: {dpi}')
            self.ratio.set(f'The value of aspect ratio: {ar}')
        except:
            pass 


if __name__ == "__main__":
    dpi_calc()
        
        