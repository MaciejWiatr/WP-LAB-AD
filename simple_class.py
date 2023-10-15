
class InfoLog:
    def __init__(self, message) -> None:
        self.message = message

    def print_message(self):
        print(f"INFO | {self.message}")


inf_log = InfoLog("hello world")
inf_log.print_message()
