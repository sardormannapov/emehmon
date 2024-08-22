import os
from dotenv import load_dotenv


class BotConfig:
    def __init__(self, envpath) -> None:
        self.envpath = envpath
        self.SetDotEnv()
        self.GetBotEnv()


    def SetDotEnv(self):
        try:
            load_dotenv(dotenv_path=self.envpath)
        except Exception as ex:
            print(".env not found.")

    def GetBotEnv(self):
        self.token = os.getenv("BOT_TOKEN", "defaultbottoken")
        self.admin_tg_id = [int(id.strip()) for id in os.getenv("ADMIN_TG_ID", "").split(",")]
        self.operator_id = os.getenv("OPERATOR_ID", "")


