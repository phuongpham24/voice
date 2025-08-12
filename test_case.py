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
        file_name, merchant_code = ultis.get_file_info(file)
        print(f"{file_name}🫆🫆🫆🫆🫆🫆🫆🫆🫆🫆🫆🫆🫆🫆🫆🫆🫆🫆🫆🫆🫆🫆")
        if file_name != "Store":
            try:
                wav_path = f"{FOLDER}/{file}"
                connection = App_Connect(os=OS)
                driver = connection.open_app()
                ui_interact = VoiceUI(driver=driver, os=OS)
                if not ui_interact.click_voice_entry():
                    return
                ultis.play_audio(wav_path)
                time.sleep(WAIT_SECONDS)
                if not ui_interact.click_voice_input():
                    return
                voice_text = ui_interact.get_voice_text()
                row = ggsheet.find_row(id=file_name)
                device_text_col = ggsheet.get_column(os=OS)
                ggsheet.write_text(text=voice_text, row=row, col=device_text_col)

                llm_response = ultis.voice_to_text_api(merchant_code=merchant_code, text=voice_text)
                api_text_col = ggsheet.get_column(os="API")
                ggsheet.write_text(text=llm_response, row=row, col=api_text_col)
            except Exception as error:
                print(f"{error}❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌")
            finally:
                time.sleep(5)
                connection.terminate_app(os=OS)
                connection.teardown()
                