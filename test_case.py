import time
from ultis.ggsheet import *
from ultis.voice_ui import *
from ultis.app_connect import *
from ultis.ultis import *
from test_variables import OS, WAIT_SECONDS, FOLDER

ggsheet = GGSheet()

class TestCase():
    def __init__(self):
        pass

    def test_voice(self, file):
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
                