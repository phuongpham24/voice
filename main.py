import unittest
import time
from ultis.ggsheet import *
from ultis.voice_ui import *
from ultis.app_connect import *
from ultis.ultis import *

OS = "ios"
WAIT_SECONDS = 0.85
FOLDER = "./data/wav-data"

ggsheet = GGSheet()
ultis = Ultis()

files = ultis.get_files(FOLDER)

class TestAppium(unittest.TestCase):
    def test_voice_to_text(self):
        for file in files:
            with self.subTest(file=file):
                file_id = ultis.get_file_id(file)
                print(f"{file_id}🫆🫆🫆🫆🫆🫆🫆🫆🫆🫆🫆🫆🫆🫆🫆🫆🫆🫆🫆🫆🫆🫆")
                if file_id != "Store":
                    try:
                        wav_path = f"{FOLDER}/{file}"
                        connection = App_Connect(os=OS)
                        driver = connection.open_app()
                        ui_interact = VoiceUI(driver=driver, os=OS)
                        ui_interact.click_voice_entry()
                        ultis.play_audio(wav_path)
                        time.sleep(WAIT_SECONDS)
                        ui_interact.click_voice_input()
                        voice_text = ui_interact.get_voice_text()
                        row = ggsheet.find_row(id=file_id)
                        column = ggsheet.get_column(os=OS)
                        ggsheet.write_text(text=voice_text, row=row, col=column)
                    except Exception as error:
                        print(f"{error}❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌")
                    finally:
                        time.sleep(5)
                        connection.terminate_app()
                        connection.teardown()
                else:
                    continue

unittest.main()
