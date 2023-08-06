import tkinter as tk
from PIL import ImageTk, Image
import os
import threading
import time

path = os.getcwd()

class Lidar:
    def __init__(self):
        self.x = 1
        pass
    
    def get_distance(self):
        t = self.x
        self.x += 2
        return t

class myGUI:
    def __init__(self):
        self.APP_HEIGHT = 480
        self.APP_WIDTH = 800
        self.sensors_value_render = [0] * 15
        
        def FONT(font_size=32) -> None:
            return ("Arial", font_size)
        
        # state handler
        self.application_state = {
            "button" : {
                "text": "Kunci Pengukuran",
                "color": "#A10000"
            },
            "status_label" : {
                "text": "Status:\nMengukur..."
            },
            "sensors" : {
                "entity": list(),
                "values": [float(0)]*15,
                "status": [0]*15,
                "active" : True
            }
        }
        
        # main window
        self.root = tk.Tk()
        self.root.geometry(f"{self.APP_WIDTH}x{self.APP_HEIGHT}")
        self.root.columnconfigure(1, weight=1)
        
        # left frame
        self.sensors = tk.Frame(self.root, width=self.APP_WIDTH / 2, height=self.APP_HEIGHT)
        self.sensors.grid(column=0, row=0)
        
        # put canvas inside the frame
        canvas = tk.Canvas(self.sensors, width=self.APP_WIDTH/2, height=self.APP_HEIGHT)
        
        for i in range(15):
            # create object inside the canvas
            canvas.create_rectangle(0, 32*i, self.APP_WIDTH/12, 32*(i+1), width=3)  
            canvas.create_rectangle(self.APP_WIDTH/12, 32*i, self.APP_WIDTH/2, 32*(i+1), width=3)
            
            # create and place sensor index
            index = tk.Label(self.sensors,
                                  text=i+1,
                                  font=FONT(14),
                                 )
            index.place(x=21, y=3+(i*32))
            
            # place jarak
            self.sensors_value_render[i] = tk.Label(self.sensors,
                                                      text=0, 
                                                      font=FONT(14)
                                                   )
            
            self.sensors_value_render[i].place(x=220, y=3+(i*32))
            
            # create and place units
            unit = tk.Label(self.sensors,
                             text="cm",
                             font=FONT(15))
            unit.place(x=350, y=2+(i*32))
            
        # sensor initialization
        for _ in range(15):
            self.application_state["sensors"]["entity"].append(Lidar())
        self.sensor_thread = threading.Thread(target=self.handle_update_sensors, daemon=True)
        self.sensor_thread.start()
        
        # right frame
        self.indicators = tk.Frame(self.root, width=self.APP_WIDTH/2, height=self.APP_HEIGHT)
        self.indicators.grid(column=1, row=0, sticky=tk.S+tk.N+tk.E+tk.W)
        self.indicators.columnconfigure(0, weight=1)

        # place it in the frame
        canvas.grid(column=0, row=0)
        
        # status label
        self.status_label = tk.Label(self.indicators, \
                                     text=self.application_state["status_label"]["text"], \
                                     pady=135, \
                                     font=FONT())
        self.status_label.grid(column=0, row=0)
        
        # lock button
        self.lock_button = tk.Button(self.indicators, \
                                     text=self.application_state["button"]["text"], \
                                     font=FONT(), \
                                     bg=self.application_state["button"]["color"], \
                                     command=self.handle_kunci_pengukuran)
        self.lock_button.grid(column=0, row=1, sticky=tk.W+tk.E)
        
        # credit
        self.credit = tk.Label(self.indicators,\
                               text="Dibuat Oleh Vinsensius Reinard", \
                               font=FONT(12))
        self.credit.grid(column=0, row=2)
        
        # logo ft untar
        img = ImageTk.PhotoImage( \
                                 Image.open(os.path.join(path, "src", "assets", "logo_ft_untar.png")) \
                                      .resize((108*2, 45*2)))
        self.image = tk.Label(self.indicators, image=img)
        self.image.place(x=175, y=20)
        
        
        # render the main window continously
        self.root.mainloop()
    
    def handle_update_sensors(self):
        red = "#A10000"
        
        while True:
            while self.application_state["button"]["color"] == red:
                for i, d in enumerate(self.application_state["sensors"]["entity"]):
                    self.application_state["sensors"]["values"][i] = \
                        self.application_state["sensors"]["entity"][i].get_distance()
                        
                    self.sensors_value_render[i].configure(text= \
                        f'Jarak: {self.application_state["sensors"]["values"][i]}')
                time.sleep(0.2)
            time.sleep(0.01)
        
            
    
    def handle_kunci_pengukuran(self):
        red = "#A10000"
        green = "#00C514"
        
        if self.application_state["button"]["color"] == red:
            self.application_state["status_label"]["text"] = "Status:\nTerkunci"
            self.application_state["button"]["text"] = "Mulai Mengukur"
            self.application_state["button"]["color"] = green
            
        else: 
            self.application_state["status_label"]["text"] = "Status:\nMengukur..."
            self.application_state["button"]["text"] = "Kunci Pengukuran"
            self.application_state["button"]["color"] = red
        
        self.status_label.configure(text=self.application_state["status_label"]["text"])
        self.lock_button.configure(text=self.application_state["button"]["text"], \
                                   bg=self.application_state["button"]["color"])

myGUI()