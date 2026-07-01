import os
import subprocess
import sys
import time
import unittest
from pathlib import Path


class TestBlackBoxGame(unittest.TestCase):
    def setUp(self):
        self.project_root = Path(__file__).resolve().parents[1]
        self.game_path = self.project_root / "game_by_bungsu.py"

    def test_game_launches_without_immediate_crash(self):
        process = subprocess.Popen(
            [sys.executable, str(self.game_path)],
            cwd=str(self.project_root),
            creationflags=subprocess.CREATE_NEW_CONSOLE if os.name == "nt" else 0,
        )

        try:
            time.sleep(3)
            self.assertIsNone(process.poll(), "Game seharusnya tetap berjalan selama pengujian")
        finally:
            if process.poll() is None:
                process.terminate()
                try:
                    process.wait(timeout=2)
                except subprocess.TimeoutExpired:
                    process.kill()

    def test_user_visible_messages_exist(self):
        source = self.game_path.read_text(encoding="utf-8")

        self.assertIn("KELARR", source)
        self.assertIn("Final Score:", source)
        self.assertIn("Score:", source)


if __name__ == "__main__":
    unittest.main()
