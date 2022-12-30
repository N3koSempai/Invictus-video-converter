from modules.conversor import Conversor
import sys
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivymd.uix.screenmanager import MDScreenManager
from kivy import _version



class Invictus_app(MDApp):
    """main class for the kiviMD GUI"""
    
    
    def build(self):
        
        self.theme_cls.material_style = "M3"
        Gui = Builder.load_file('./Invictus_Gui.kv')
        
        return Gui

Invictus_app().run()


#input_file = "demo.mp4"
#name_out = "demo_out"
#out_format = ".mkv"



#parser = createParser(input_file)
#metadata = extractMetadata(parser)
#`text = metadata.exportDictionary()
#print(text['Metadata']['Duration'])

#conv = Conversor()

#conv.convert(input_file,700, 1200, 5000, name_out, out_format)

#vid_reader = imageio.get_reader(input_file)
#print()
#mdata = vid_reader.get_meta_data()
#print(mdata)
#video.trans_code(input_file,700, 1800,5000,out_file)
