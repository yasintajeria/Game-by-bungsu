import types
import unittest


class DummyRect:
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def colliderect(self, other):
        return (self.x < other.x + other.w and self.x + self.w > other.x and
                self.y < other.y + other.h and self.y + self.h > other.y)


class TestWhiteBoxGameLogic(unittest.TestCase):
    def test_spawn_timer_resets_after_spawn(self):
        spawn_timer = 31
        if spawn_timer > 30:
            spawn_timer = 0
        self.assertEqual(spawn_timer, 0)

    def test_enemy_out_of_bounds_increases_score(self):
        score = 0
        enemy_y = 700
        if enemy_y > 600:
            score += 1
        self.assertEqual(score, 1)

    def test_enemy_speed_increases_every_10_points(self):
        score = 9
        enemy_speed = 5.0
        if score % 10 == 0:
            enemy_speed += 0.3
        self.assertEqual(enemy_speed, 5.0)

        score = 10
        enemy_speed = 5.0
        if score % 10 == 0:
            enemy_speed += 0.3
        self.assertEqual(enemy_speed, 5.3)

    def test_collision_detection_returns_true_when_overlap(self):
        player = DummyRect(100, 100, 50, 50)
        enemy = DummyRect(120, 120, 50, 50)
        self.assertTrue(player.colliderect(enemy))

    def test_collision_detection_returns_false_when_separated(self):
        player = DummyRect(100, 100, 50, 50)
        enemy = DummyRect(200, 200, 50, 50)
        self.assertFalse(player.colliderect(enemy))

    def test_background_reset_when_reaches_bottom(self):
        bg1 = 600
        if bg1 >= 600:
            bg1 = -600
        self.assertEqual(bg1, -600)

    def test_boundary_prevents_player_from_leaving_left_side(self):
        p1_x = 0
        speed = 7
        keys_left = True
        if keys_left and p1_x > 0:
            p1_x -= speed
        self.assertEqual(p1_x, 0)

    def test_boundary_prevents_player_from_leaving_right_side(self):
        p1_x = 550
        speed = 7
        keys_right = True
        if keys_right and p1_x < 600 - 50:
            p1_x += speed
        self.assertEqual(p1_x, 550)


if __name__ == "__main__":
    unittest.main()
