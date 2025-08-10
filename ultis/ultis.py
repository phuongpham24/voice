# from pydub import AudioSegment
import os
import subprocess

class Ultis():
    def __init__(self):
        pass

    def get_files(self, path):
        self.files = os.listdir(path)
        return self.files

    def play_audio(self, audio):
        print("File opening", audio)
        subprocess.run(["ffplay", "-nodisp", "-autoexit", audio], 
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

    def get_file_id(self, file):
        self.file_name = os.path.basename(file)
        self.name_without_extention = os.path.splitext(self.file_name)[0]
        self.splited_data = self.name_without_extention.split("_")
        self.file_id = self.splited_data[1]
        return self.file_id

    def get_column_letter(self, column_index):
        self.result = ""
        while column_index > 0:
            self.remainder = (column_index - 1) % 26
            self.result = chr(ord('A') + self.remainder) + self.result
            self.column_index = (column_index - 1) // 26
        return self.result
    
    # def convert_aac_wav(self, aac_file_path, wac_output_path):
    #     # aac_file_path = "./voice-data/mot-con-vit.aac"
    #     # wac_output_path = "./wav-data/mot-con-vit.wav"
    #     self.audio = AudioSegment.from_file(aac_file_path, format="aac")
    #     self.audio.export(wac_output_path, format="wav")
    

