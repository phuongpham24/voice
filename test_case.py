import time
from ultis.ggsheet import *
from ultis.mobile_interaction import *
from ultis.app import *
from ultis.ultis import *
from test_variable import FOLDER, WAIT_SECONDS

ggsheet = GGSheet()

class TestCase():
    def __init__(self):
        pass

    def test_voice(self, file, test_variable):
        file_name, merchant_code = ultis.get_file_info(file)
        print(f"{file_name}🫆🫆🫆🫆🫆🫆🫆🫆🫆🫆🫆🫆🫆🫆🫆🫆🫆🫆🫆🫆🫆🫆")
        if file_name != "Store":
            try:
                wav_path = f"{FOLDER}/{file}"
                connection = App(app_config=test_variable["app_config"])
                driver = connection.open_app()
                ui_interact = MobileUIInteraction(driver=driver)
                for step in test_variable["steps"]:
                    if step["action"] == "sleep":
                        time.sleep(step["second"])
                    elif step["action"] == "click":
                        if not ui_interact.click_element(step["element"]):
                            return
                    elif step["action"] == "voice":
                        ultis.play_audio(wav_path)
                    elif step["action"] == "get_text":
                        time.sleep(WAIT_SECONDS)
                        if not ui_interact.click_element(step["element"]):
                            return
                        voice_text = ui_interact.get_element_text(element=step["element"])
                        print(voice_text)
                        row = ggsheet.find_row(id=file_name)
                        ggsheet.write_text(text=voice_text, row=row, col=test_variable["result_column"])
                    else:
                        pass

            except Exception as error:
                print(f"{error}❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌❌")
            finally:
                time.sleep(5)
                connection.terminate_app(app_config=test_variable["app_config"])
                connection.teardown()
                