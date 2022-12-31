#from modules.conversor import Conversor
import os
from kivy.core.window import Window
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.filemanager import MDFileManager
from kivymd.uix.label import MDLabel
from kivy import platform
#if platform == "android":
#    from android.permissions import request_permissions, Permission
#    request_permissions([Permission.WRITE_EXTERNAL_STORAGE, 
#   Permission.READ_EXTERNAL_STORAGE])





from kivymd.uix.screenmanager import MDScreenManager
from kivy import _version



class Invictus_app(MDApp):
    """main class for the kiviMD GUI"""
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.bind(on_keyboard=self.events)
        self.manager_open = False
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager, select_path=self.select_path
            )
    
    def build(self):
        
        self.theme_cls.material_style = "M3"
        Gui = Builder.load_file('./Invictus_Gui.kv')
        
        return Gui
        
    def file_manage(self):
        self.file_manager.show(os.path.expanduser("~"))
        self.manager_open = True




    def select_path(self, path: str):
        #conv = Conversor()
        name_out = 'demo_out'
        out_format = '.avi'
        self.exit_manager()
        #conv.convert(path,700, 1200, 5000, name_out, out_format)
        

    def exit_manager(self, *args):
        self.manager_open = False
        self.file_manager.close()







Invictus_app().run()


#input_file = "demo.mp4"
#name_out = "demo_out"
#out_format = ".mkv"



#parser = createParser(input_file)
#metadata = extractMetadata(parser)
#`text = metadata.exportDictionary()
#print(text['Metadata']['Duration'])



#conv.convert(input_file,700, 1200, 5000, name_out, out_format)

#vid_reader = imageio.get_reader(input_file)
#print()
#mdata = vid_reader.get_meta_data()
#print(mdata)
#video.trans_code(input_file,700, 1800,5000,out_file)
