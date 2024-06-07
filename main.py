from datetime import datetime
from PIL import Image #pip install Pillow
import customtkinter
import os
import re

class HeApp(customtkinter.CTk):
    def __init__(self):
        super().__init__()
      
        # CREATE WINDOW
        self.title("HeDesign")
        self.geometry("1630x800+0+0")   
        self.minsize(1600, 700)
        # self.resizable(False, False)
        
        # CONFIGURE GRID LAYOUT 
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(3, weight=1)


        # STATIC VARIABLE
        padXFrame = 10
        padYFrame = 20
        cornRad = 20
        widthCol1 = 170
        widthCol2 = 345
        widthCol3 = 370
        widthCol4 = 800
        letscontinue = True
        
        # ARGUMENTS #ÚPRAVA
        self.entry_1p_arg = None
        self.entry_2p_arg = None
        self.entry_3p_arg = None
        self.entry_4p_arg = None
        self.entry_5p_arg = None
        self.entry_6p_arg = None
        self.entry_7p_arg = None
        self.entry_numAngle_arg = None
        self.entry_numFibers_arg = None
        self.entry_rottationC_arg = None
        self.entry_rottationA_arg = None
        self.entry_speedF_arg = None
        self.entry_speedE_arg = None
        self.entry_speedS_arg = None
        self.entry_correction_arg = None
        
        self.Z1_val = None
        self.Y1_val = None
        
        # CALCULATE VALUE  #ÚPRAVA
        self.Z1_val = None
        self.Y1_val = None
       
        self.F2_val = None
        self.Z2_val = None
        
        self.F3_val = None
        self.Z3_val = None
        self.S3_val = None
        self.C3_val = None
        self.A3_val = None
        
        self.F4_val = None
        self.Z4_val = None
        
        self.E5_val = None
        self.Y5_val = None
        
        self.S6_val = None
        self.C6_val = None
        self.A6_val = None
        
        self.E7_val = None
        self.Y7_val = None
        
        self.F8_val = None
        self.Z8_val = None
        
        self.F9_val = None
        self.Z9_val = None
    
        self.F10_val = None
        self.Z10_val = None
        self.S10_val = None
        self.C10_val = None
        self.A10_val = None
        
        self.F11_val = None
        self.Z11_val = None
        
        self.E12_val = None
        self.Y12_val = None
        
        self.S13_val = None
        self.C13_val = None
        self.A13_val = None
        
        self.E14_val = None
        self.Y14_val = None
        
        self.F15_val = None
        self.Z15_val = None
        
        self.numRun = None
        self.moveOneAngle =None
        self.sumRotation = None

                
        # COLUMN 1
        self.mainFrame = customtkinter.CTkFrame(self, width=widthCol1, corner_radius=cornRad)
        self.mainFrame.grid(row=0, column=0, padx=padXFrame, pady=padYFrame, sticky="nsew")
        
        # Column 1 (app name label)
        self.appName = customtkinter.CTkLabel(self.mainFrame, text="HeDesign", font=customtkinter.CTkFont(family="Futura", size=30, weight="bold"))
        self.appName.grid(row=0, column=0, padx=15, pady=20)
        
        # Culumn 1 (resizable place)
        self.mainFrame.grid_rowconfigure(1, weight=1)        
        
        # Column 1 (appearance mode label)
        self.appearanceModeLab = customtkinter.CTkLabel(self.mainFrame, font=customtkinter.CTkFont(family="Futura"), text="Appearance Mode:", anchor="s")
        self.appearanceModeLab.grid(row=2, column=0)
        
        # Column 1 (apperance mode menu)
        self.appearanceModeOptioneMenu = customtkinter.CTkOptionMenu(self.mainFrame,values=["Light", "Dark"],command=self.change_appearance_mode_event,anchor="center")
        self.appearanceModeOptioneMenu.grid(row=3, column=0, pady=(5, 20))        
   
    
        # COLUMN 2
        # create tabview
        self.tabview = customtkinter.CTkTabview(self, width=widthCol2, corner_radius=cornRad)
        self.tabview.grid(row=0, column=1, padx=padXFrame, pady=padYFrame, sticky="nsew")
        self.tabview.add("Generate")
        self.tabview.add("Setting")
                
        # Column 2 (GENERATE)
        # column 2 (label and entry)      
        labels_and_entries = [
            ("position 1 [mm]:", "entry_1p"),
            ("position 2 [mm]:", "entry_2p"),
            ("position 3 [mm]:", "entry_3p"),
            ("position 4 [mm]:", "entry_4p"),
            ("position 5 [mm]:", "entry_5p"),
            ("position 6 [mm]:", "entry_6p"),
            ("position 7 [mm]:", "entry_7p"),
            ("number of angles [-]:", "entry_numAngle"),
            ("number of fibres [-]:", "entry_numFibers"),
            ("c [°]:", "entry_rottationC"),
            ("a [°]:", "entry_rottationA")
        ]

        for i, (label_text, entry_name) in enumerate(labels_and_entries):
            label = customtkinter.CTkLabel(self.tabview.tab("Generate"), font=customtkinter.CTkFont(family="Futura"), text=label_text)
            label.grid(row=i, column=0, padx=10, pady=5, sticky="w")
            entry = customtkinter.CTkEntry(self.tabview.tab("Generate"), placeholder_text="0")
            entry.grid(row=i, column=1, padx=10, pady=5)

            #store entries with unique names
            setattr(self, entry_name, entry)



               
        # Culumn 2 (resizable place)
        self.tabview.tab("Generate").grid_rowconfigure(11, weight=1)   
        
        # Column 2 (generate button)
        self.generator_button = customtkinter.CTkButton(master=self.tabview.tab("Generate"), text="Generate", border_width=2, border_color="#36719f", command=self.generate_code)
        self.generator_button.grid(row=12, columnspan=2, ipady=2, ipadx=2)     

        # Column 2 (SETTING)
        # column 2 (label and entry)
        self.label_speedF = customtkinter.CTkLabel(self.tabview.tab("Setting"),font=customtkinter.CTkFont(family="Futura"), text="F [mm/s]:")
        self.label_speedF.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.entry_speedF = customtkinter.CTkEntry(self.tabview.tab("Setting"), placeholder_text="0")
        self.entry_speedF.grid(row=0, column=1, padx=10, pady=5,) # F = 30 !!!
        
        self.label_speedE = customtkinter.CTkLabel(self.tabview.tab("Setting"),font=customtkinter.CTkFont(family="Futura"), text="E [mm/s]:")
        self.label_speedE.grid(row=1, column=0, padx=10, pady=5, sticky="w")
        self.entry_speedE = customtkinter.CTkEntry(self.tabview.tab("Setting"), placeholder_text="0")
        self.entry_speedE.grid(row=1, column=1, padx=10, pady=5,)       

        #self.label_speedS = customtkinter.CTkLabel(self.tabview.tab("Setting"),font=customtkinter.CTkFont(family="Futura"), text="S [rpm]:")
        #self.label_speedS.grid(row=2, column=0, padx=10, pady=5, sticky="w")
        #self.entry_speedS = customtkinter.CTkEntry(self.tabview.tab("Setting"), placeholder_text="0")
        #self.entry_speedS.grid(row=2, column=1, padx=10, pady=5,)
        
        self.label_correction = customtkinter.CTkLabel(self.tabview.tab("Setting"),font=customtkinter.CTkFont(family="Futura"), text="correction [°]:")
        self.label_correction.grid(row=3, column=0, padx=10, pady=5, sticky="w")
        self.entry_correction = customtkinter.CTkEntry(self.tabview.tab("Setting"), placeholder_text="0")
        self.entry_correction.grid(row=3, column=1, padx=10, pady=5)     
        

        self.all_value_to_control = [self.entry_1p, self.entry_2p, self.entry_3p, self.entry_4p, self.entry_5p, self.entry_6p, self.entry_7p, self.entry_numAngle, self.entry_numFibers, self.entry_rottationC, self.entry_rottationA, self.entry_speedF, self.entry_speedE, self.entry_correction]        

        # Column 2 (resizable place)
        self.tabview.tab("Setting").grid_rowconfigure(4, weight=1)              

        # Column 2 (generate button)
        self.generatr_button2 = customtkinter.CTkButton(master=self.tabview.tab("Setting"), text="Generate", border_width=2, border_color="#36719f", command=self.generate_code)
        self.generatr_button2.grid(row=5, columnspan=2, ipady=2, ipadx=2)        
        
  
        # COLUMN 3
        # create tabview
        self.tabview2 = customtkinter.CTkTabview(self,  width=widthCol3, corner_radius=cornRad)
        self.tabview2.grid(row=0, column=2, padx=padXFrame, pady=padYFrame, sticky="nsew")
        self.tabview2.add("Generate Guide")
        self.tabview2.add("Setting Guide") 
                      
        # Guide generate textbox
        self.label_generate_guide = customtkinter.CTkTextbox(self.tabview2.tab("Generate Guide"), font=("Arial", 12), width=widthCol3, height=400, corner_radius=cornRad)
        self.label_generate_guide.grid(row=0, column=0, sticky="nsew")
        self.label_generate_guide.insert("0.0", "Position 1: Distance of the fixture from the zero point.\n\n"
                                                "Position 2: Distance between fixtures.\n\n"
                                                "Position 3: Diameter of threaded rod.\n\n"
                                                "Position 4: Diameter of heat exchanger.\n\n"
                                                "Position 5: Offset from position 1.\n\n"
                                                "Position 6: Offset from diameter position 3.\n\n"
                                                "Position 7: Offset from diameter position 4.\n\n"
                                                "Correction: Enter the correction value (recommended 2°).\n\n"
                                                "Number of Angle: Enter the number of spaces in the fixture.\n\n"
                                                "Number of Fibres: Total number of hollow fibers of the HE.\n\n"
                                                "c: Angle of rotation of the spindle at the end point of HE.\n\n"
                                                "a: Angle of rotation of the spindle during winding of HE.")
        self.label_generate_guide.configure(state="disabled")  
        
        # Guide setting textbox
        self.label_setting_guide = customtkinter.CTkTextbox(self.tabview2.tab("Setting Guide"), font=("Arial", 12), width=widthCol3, height=170, corner_radius=cornRad)
        self.label_setting_guide.grid(row=0, column=0, sticky="nsew")
        self.label_setting_guide.insert("0.0", "F:\tDetermine the speed of linear motions in\n" 
                                        "\tthe direction of the Z axis \n\n"
                                        "E:\tDetermine the speed of linear motions in\n"   
                                        "\tthe direction of the Y axis \n\n"
                                        "corr:\t Winding machine inaccuracy correction.")
        self.label_setting_guide.configure(state="disabled")  #prohibition of overwriting


        # COLUMN 4
        # create tabview
        self.tabview3 = customtkinter.CTkTabview(self, width=widthCol4, corner_radius=cornRad, fg_color="#fff")
        self.tabview3.grid(row=0, column=3, padx=padXFrame, pady=padYFrame, sticky="nsew")
        self.tabview3.add("Generate Images")
        # self.tabview3.add("XXX")
                      
        # Column 4 (img insert)
        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "img")
        self.guideImg = customtkinter.CTkImage(Image.open(os.path.join(image_path, "Image1.png")), size=(630, 343))
        self.guideImg_label = customtkinter.CTkLabel(self.tabview3.tab("Generate Images"), image=self.guideImg, text="")        
        self.guideImg_label.pack() #why pack? → pack automaticaly in the middle

        self.guideImg2 = customtkinter.CTkImage(Image.open(os.path.join(image_path, "Image2.png")), size=(630, 262))
        self.guideImg2_label = customtkinter.CTkLabel(self.tabview3.tab("Generate Images"), image=self.guideImg2, text="")
        self.guideImg2_label.pack()
        
    def change_appearance_mode_event(self, new_appearance_mode: str): 
        customtkinter.set_appearance_mode(new_appearance_mode)
    
    def check_value(self):
        letscontinue = True 
        for one_value in self.all_value_to_control:
            if re.match("^\d+(\.\d+)?$", one_value.get()) is None:
                one_value.delete(0, "end")
                one_value.configure(border_color="#ff8402", placeholder_text="Invalid input",
                                    placeholder_text_color="#ff8402")
                letscontinue = False
            else:
                one_value.configure(border_color="#8d9399")
                
    def get_entered_values(self):
        self.entry_1p_arg = int(self.entry_1p.get())
        self.entry_2p_arg = int(self.entry_2p.get())
        self.entry_3p_arg = int(self.entry_3p.get())
        self.entry_4p_arg = int(self.entry_4p.get())
        self.entry_5p_arg = int(self.entry_5p.get())
        self.entry_6p_arg = int(self.entry_6p.get())
        self.entry_7p_arg = int(self.entry_7p.get())
        self.entry_numAngle_arg = int(self.entry_numAngle.get())
        self.entry_numFibers_arg = int(self.entry_numFibers.get())
        self.entry_rottationC_arg = int(self.entry_rottationC.get())
        self.entry_rottationA_arg = int(self.entry_rottationA.get())
        self.entry_speedF_arg = int(self.entry_speedF.get()) # 30
        self.entry_speedE_arg = int(self.entry_speedE.get()) # 15
        # self.entry_speedS_arg = int(self.entry_speedS.get()) # 5 rychlos pouze v tom koncovem bode TOHLE BUDEME MUSET ODSTRANIT!!!
        self.entry_correction_arg = int(self.entry_correction.get())
        
    def formattingValue(self, valueOld):
        valueNew = str("{:.2f}".format(valueOld)).replace(".",",")
        return valueNew

    def calculateValues(self):
        self.Z1_val = self.formattingValue(self.entry_1p_arg)
        self.Y1_val = self.formattingValue(self.entry_4p_arg/2+self.entry_7p_arg)
        
        self.F2_val = self.formattingValue(self.entry_speedF_arg+10)
        self.Z2_val = self.formattingValue(self.entry_1p_arg+self.entry_2p_arg*0.1)
        
        self.F3_val = self.formattingValue(self.entry_speedF_arg)
        self.Z3_val = self.formattingValue(self.entry_1p_arg+self.entry_2p_arg)
        self.S3_val = self.formattingValue(self.entry_speedS_arg)
        self.C3_val = self.formattingValue(self.entry_rottationA_arg)
        self.A3_val = self.formattingValue(self.entry_rottationA_arg+self.sumRotation)
        
        self.F4_val = self.formattingValue(self.entry_speedF_arg-15)
        self.Z4_val = self.formattingValue((self.entry_1p_arg+self.entry_2p_arg)+(self.entry_1p_arg-self.entry_5p_arg))
        
        self.E5_val = self.formattingValue(self.entry_speedE_arg)
        self.Y5_val = self.formattingValue(self.entry_3p_arg/2+self.entry_6p_arg)
        
        self.S6_val = self.formattingValue(self.entry_speedS_arg)
        self.C6_val = self.formattingValue(self.entry_rottationC_arg+self.moveOneAngle)
        self.A6_val = self.formattingValue(self.sumRotation+self.entry_rottationC_arg+self.entry_rottationA_arg+self.moveOneAngle)
        
        self.E7_val = self.formattingValue(self.entry_speedE_arg+5)
        self.Y7_val = self.formattingValue(self.entry_3p_arg/2+self.entry_6p_arg)
        
        self.F8_val = self.formattingValue(self.entry_speedF_arg-10)
        self.Z8_val = self.formattingValue(self.entry_1p_arg+self.entry_2p_arg)
        
        self.F9_val = self.formattingValue(self.entry_speedF_arg+10)
        self.Z9_val = self.formattingValue(self.entry_1p_arg+self.entry_2p_arg*0.9)
    
        self.F10_val = self.formattingValue(self.entry_speedF_arg)
        self.Z10_val = self.formattingValue(self.entry_1p_arg)
        self.S10_val = self.formattingValue(self.entry_speedS_arg)
        self.C10_val = self.formattingValue(self.entry_rottationA_arg)
        self.A10_val = self.formattingValue(self.sumRotation+self.entry_rottationC_arg+2*self.entry_rottationA_arg+self.moveOneAngle)
        
        self.F11_val = self.formattingValue(self.entry_speedF_arg-15)
        self.Z11_val = self.formattingValue(self.entry_1p_arg-self.entry_5p_arg)
        
        self.E12_val = self.formattingValue(self.entry_speedE_arg)
        self.Y12_val = self.formattingValue(self.entry_3p_arg/2+self.entry_6p_arg)
        
        self.S13_val = self.formattingValue(self.entry_speedS_arg)
        self.C13_val = self.formattingValue(self.entry_rottationC_arg)
        self.A13_val = self.formattingValue(self.sumRotation+2*self.entry_rottationC_arg+2*self.entry_rottationA_arg+self.moveOneAngle)
        
        self.E14_val = self.formattingValue(self.entry_speedE_arg+5)
        self.Y14_val = self.formattingValue(self.entry_3p_arg/2+self.entry_6p_arg)
        
        self.F15_val = self.formattingValue(self.entry_speedF_arg-10)
        self.Z15_val = self.formattingValue(self.entry_1p_arg)
        
    def calculateInitals(self):
        self.numRun = self.entry_numFibers_arg // 2 #in one run, two fiber
        self.entry_speedS_arg = (self.entry_rottationC_arg/360)*(60/(self.entry_2p_arg*0.9/self.entry_speedF_arg))   # rychlost otáčená je počítána na základě F, nehrab do toho, REDUDANCE, 
        self.moveOneAngle = 360/self.entry_numAngle_arg - self.entry_correction_arg # rotace v koncovém bode, je tam i korekce na rotaci
        self.sumRotation = 0

    
    def generate_code(self):
        self.check_value()
        self.get_entered_values()
        self.calculateInitals()
        self.calculateValues()
        
        if letscontinue:
            with customtkinter.filedialog.asksaveasfile(mode='w', defaultextension=".txt") as file:  #select place to save
                file.writelines("[G-CODE GENERATED BY PYTHON on {}]\n".format(datetime.now().strftime("%Y-%m-%d%I:%M:%S %p")))
                file.writelines("[FilePath = {}]\n".format(os.path.dirname(os.path.realpath(__file__))))
                file.writelines("[Units are in Millimeters]\n\n")
                
                file.writelines("[INITIALIZE WINDING SESSION]\n")
                file.writelines("C C1 [DECIMAL COMMA FORMAT = YES]\n")
                file.writelines("G21 [Units are Millimeters]\n")
                file.writelines("G90 [Absolute Positioning]\n")
                file.writelines("X V417,000 T4 Z47,752\n\n")
                
                file.writelines("[ENABLE STEPPERS AND MOVE TO STARTING POSITION]\n")
                file.writelines("M17 [Enable Steppers]\n")
                file.writelines("G1 I10 J10 K10 N10 O10 T10 [Linear and Angular Acceleration Settings of Axes]\n")
                file.writelines("G28 E50,800 R4 F25,400 C0,00 [Move Axes to Limit Switches]\n")
                file.writelines("G4 P1000 [Pause 1s at Carriage Limit Switch]\n")
                file.writelines("G1 J1,250 K1,250 O1,250 T10 [Set Axes Accels]\n")
                file.writelines("G4 Z P1000 [Pause 1s]\n")
                file.writelines("G1 F15,40 Z{} Y{} E15,40 B90 R10 S0\n\n".format(self.Z1_val, self.Y1_val))

                file.writelines(["[BEGIN 4-AXIS WINDING WITH FLAT ENDS]\n"])
                file.writelines(["D0 ST=Winding Schedule\n"])
                file.writelines(["M0 [Wait for Button Press to Begin Winding Schedule]\n"])
                file.writelines(["M601 [MARK THE MANDREL REFERFENCE ANGLE]\n\n"])
    
                
                # !! tady si skončil
                for actualNumRun in range(0, self.numRun):  
                    self.calculateValues()  
                                
                    if actualNumRun % self.entry_numAngle_arg == 0:
                        self.entry_5p_arg -= self.entry_correction_arg         
                                   
                    if actualNumRun == round(self.numRun*0.8):
                        self.entry_7p_arg += 10 # na konci procesu tam vytovříme protor aby nedošlo ke kolizi
                        
                    file.writelines(["[---]\n"])
                    
                    file.writelines(["[Layer {}]\n".format(actualNumRun)]) 
                    
                    file.writelines(["G1 F{} Z{} S0 [MOVE LEFT END]\n".format(self.F2_val, self.Z2_val)])
                    
                    file.writelines(["G1 F{} Z{} S{} C{} A{} [MOVE LEFT END]\n".format(self.F3_val, self.Z3_val, self.S3_val, self.C3_val, self.A3_val)])
                    
                    file.writelines(["G1 F{} Z{} S0 [MOVE LEFT END]\n".format(self.F4_val,self.Z4_val)])
                    
                    file.writelines(["G1 E{} Y{} S0 [MOVE LEFT END]\n".format(self.E5_val, self.Y5_val)])
                    
                    file.writelines(["G1 S{} C{} A{} [ROTATION]\n".format(self.S6_val, self.C6_val, self.A6_val)])
                    
                    file.writelines(["G1 E{} Y{} S0 [MOVE BACK FROM LEFT END]\n".format(self.E7_val,  self.Y7_val)])
                    
                    file.writelines(["G1 F{} Z{} S0 [MOVE BACK FROM LEFT END]\n".format(self.F8_val, self.Z8_val)])  
                      
                    file.writelines(["G1 F{} Z{} S0 [MOVE RIGHT END]\n".format(self.F9_val, self.Z9_val)]) 
                      
                    file.writelines(["G1 F{} Z{} S{} C{} A{} [MOVE RIGHT END]\n".format(self.F10_val, self.Z10_val, self.S10_val, self.C10_val, self.A10_val)]) 
                    
                    file.writelines(["G1 F{} Z{} S0 [MOVE RIGHT END]\n".format(self.F11_val, self.Z11_val)])
                    
                    file.writelines(["G1 E{} Y{} S0 [MOVE RIGHT END]\n".format(self.E12_val, self.Y12_val)])
                    
                    file.writelines(["G1 S{} C{} A{} [ROTATION]\n".format(self.S13_val, self.C13_val, self.A13_val)])
                    
                    file.writelines(["G1 E{} Y{} S0 [MOVE BACK FROM RIGHT END]\n".format(self.E14_val, self.Y14_val)])
                    
                    file.writelines(["G1 F{} Z{} S0 [MOVE BACK FROM RIGHT END]\n".format(self.F15_val, self.Z15_val)])
                    
                    
if __name__ == "__main__":
    app = HeApp()
    app.mainloop()

