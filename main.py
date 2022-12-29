from modules.conversor import Conversor
import sys







input_file = "demo.mp4"
name_out = "demo_out"
out_format = ".mkv"



#parser = createParser(input_file)
#metadata = extractMetadata(parser)
#`text = metadata.exportDictionary()
#print(text['Metadata']['Duration'])

conv = Conversor()

conv.convert(input_file,700, 1200, 5000, name_out, out_format)

#vid_reader = imageio.get_reader(input_file)
#print()
#mdata = vid_reader.get_meta_data()
#print(mdata)
#video.trans_code(input_file,700, 1800,5000,out_file)
