from . import *


class PlayerBot(Bot):
    def play_round(self):
        yield Submission(Demographics, timeout_happened=True)
        if self.player.student:
            yield Submission(StudentDetails, timeout_happened=True)
        yield Submission(Summary, check_html=False)
