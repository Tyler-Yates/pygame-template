import json
import logging
import os
from pathlib import Path
from typing import List

from src.mygame.util.paths import get_save_file_directory

MAXIMUM_NUMBER_OF_HIGHSCORES = 10

HIGHSCORE_KEY = "hiscores"

SAVE_FILE_NAME = "save.json"


class HiscoreState:
    def __init__(self):
        self.log = logging.getLogger(self.__class__.__name__)
        self.hiscores: List[int] = []

        self.save_file_path = os.path.join(get_save_file_directory(), SAVE_FILE_NAME)

        # Attempt to load the save file from disk
        self.hiscores = self._load_save_file()
        self._cleanup_hiscore()

    def _cleanup_hiscore(self):
        self.hiscores = sorted(self.hiscores, reverse=True)
        self.hiscores = self.hiscores[:MAXIMUM_NUMBER_OF_HIGHSCORES]

    def _load_save_file(self) -> List[int]:
        if not os.path.exists(self.save_file_path):
            self.log.info(f"No save file found at {self.save_file_path}")
            return []

        try:
            with open(self.save_file_path, mode="r") as save_file:
                json_data = json.load(save_file)
                return json_data[HIGHSCORE_KEY]
        except Exception as e:
            self.log.error("Could not load hiscore file.", e)
            return []

    def add_hiscore(self, score: int) -> bool:
        """
        Attempts to add the given score the hiscore table.
        Returns whether the score is good enough to make it onto the hiscore table.

        Args:
            score: The given score

        Returns:
            True if the score is good enough to make it on the hiscore table, False otherwise
        """
        if len(self.hiscores) < MAXIMUM_NUMBER_OF_HIGHSCORES or (score > self.hiscores[-1]):
            self.hiscores.append(score)
            self._cleanup_hiscore()
            return True
        else:
            return False

    def save_hiscores(self):
        self.log.info(f"Saving hiscores to {self.save_file_path}")

        Path(get_save_file_directory()).mkdir(parents=True, exist_ok=True)

        with open(self.save_file_path, mode="w") as save_file:
            data_to_save = {HIGHSCORE_KEY: self.hiscores}
            json.dump(data_to_save, save_file)
