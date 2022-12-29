#create by Alvaro
# module for conversion of codec

import ffmpeg

class Conversor:

    def __init__(self):
        pass
        
     
    def convert(self, input_file: str, width: int, height: int, rate: int, name_out: str, out_format: str):
        """Main function for transcode video"""
        stream = ffmpeg.input(input_file)
        stream = ffmpeg.output(stream, name_out + out_format,vcodec="libsvtav1", strict="-2", video_bitrate='2M', crf= 40)
        
        
        #stream = ffmpeg.output(stream, name_out + out_format, vcodec="libvpx-vp9", strict="-2", video_bitrate='2M')
        
        #stream = ffmpeg.output(stream, name_out + out_format, vcodec="mpeg4", strict="-2", video_bitrate='555k')
        ffmpeg.run(stream)
