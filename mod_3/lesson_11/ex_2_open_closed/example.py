
class TextPrinter:

    def __init__(self, text):
        self.text = text

    def print_lines(self):
        lines = self.text.text_str.split("\n")
        for line in lines:
            print(line)

        # for line in self.text.lines:
        #     print(line)


class NormalText:

    def __init__(self, text_str):
        self.text_str = text_str
        # self.lines = self.text_str.split("\n")


# class RemoteText:
#
#     def __init__(self, remote_address):
#         self.remote_address = remote_address
#         self.lines = self.load_remote_text_lines()
#
#     def load_remote_text_lines(self):
#         pass
#
#
