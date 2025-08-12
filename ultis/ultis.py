# from pydub import AudioSegment
import os
import subprocess
import requests

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

    def get_file_info(self, file):
        self.file_name = os.path.basename(file)
        self.name_without_extention = os.path.splitext(self.file_name)[0]
        self.splited_data = self.name_without_extention.split("_")
        self.merchant_code = self.splited_data[0]
        # self.file_id = self.splited_data[1]
        # return self.file_id
        return self.name_without_extention, self.merchant_code

    def get_column_letter(self, column_index):
        self.result = ""
        while column_index > 0:
            self.remainder = (column_index - 1) % 26
            self.result = chr(ord('A') + self.remainder) + self.result
            self.column_index = (column_index - 1) // 26
        return self.result
    
    def voice_to_text_api(self, merchant_code, text):
        self.params = {
            "merchantCode": "MCL0GHI45KN66",
            "recognizedText": text
        }
        self.response = requests.post("https://api-litepos-qc.int.vinshop.dev/pcm-int/api/voice-to-order/process", params=self.params)
        self.response.raise_for_status()
        self.data = self.response.json()
        try:
            self.llm_response = self.data["llmResponse"]
        except Exception as error:
            print(f"{error}❌")
            return
        else:
            return self.llm_response
    
    # def convert_aac_wav(self, aac_file_path, wac_output_path):
    #     # aac_file_path = "./voice-data/mot-con-vit.aac"
    #     # wac_output_path = "./wav-data/mot-con-vit.wav"
    #     self.audio = AudioSegment.from_file(aac_file_path, format="aac")
    #     self.audio.export(wac_output_path, format="wav")
    

