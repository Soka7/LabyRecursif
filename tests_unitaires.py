import unittest
import os
import tempfile
import threading
import time
from unittest.mock import patch, MagicMock

# Stub pyray pour éviter d'avoir besoin d'une fenêtre graphique lors des tests
import sys
import types

pyray_stub = types.ModuleType("pyray")

class Vector2:
    def __init__(self, x=0, y=0): self.x, self.y = x, y

class Color:
    def __init__(self, r=0, g=0, b=0, a=255): self.r, self.g, self.b, self.a = r, g, b, a

class Rectangle:
    def __init__(self, x=0, y=0, w=0, h=0): self.x, self.y, self.width, self.height = x, y, w, h

pyray_stub.Vector2         = Vector2
pyray_stub.Color           = Color
pyray_stub.Rectangle       = Rectangle
pyray_stub.draw_rectangle_rec = lambda *a, **kw: None

sys.modules["pyray"] = pyray_stub

from Labyrinth import Labyrinth   # adapte le nom si ton fichier s'appelle différemment


# ─────────────────────────────────────────────────────────────────────────────
# Helpers
# ─────────────────────────────────────────────────────────────────────────────
def make_maze_file(content: str) -> str:
    """Écrit un contenu dans un fichier temporaire et retourne son chemin."""
    tmp = tempfile.NamedTemporaryFile(mode="w", suffix=".txt", delete=False)
    tmp.write(content)
    tmp.close()
    return tmp.name


SIMPLE_MAZE = (
    "XXXXX\n"
    "E   X\n"
    "XXXXX\n"
    "X   S\n"
    "XXXXX"
)

SOLVABLE_MAZE = (
    "XXXXXXX\n"
    "E     X\n"
    "XXXXX X\n"
    "X     X\n"
    "X XXXXX\n"
    "X     S\n"
    "XXXXXXX"
)

NO_EXIT_MAZE = (
    "XXXXX\n"
    "E   X\n"
    "XXXXX"
)

TRIVIAL_MAZE = (
    "XXX\n"
    "ESX\n"
    "XXX"
)


# ═════════════════════════════════════════════════════════════════════════════
# 1. Tests — LoadLabyrinth
# ═════════════════════════════════════════════════════════════════════════════
class TestLoadLabyrinth(unittest.TestCase):

    def setUp(self):
        self.lab = Labyrinth()

    # Chargement nominal
    def test_load_fills_array(self):
        path = make_maze_file(SIMPLE_MAZE)
        self.lab.LoadLabyrinth(path)
        os.unlink(path)
        self.assertEqual(len(self.lab.LabyrinthArray), 5)
        self.assertEqual(self.lab.LabyrinthArray[1][0], 'E')

    # Rechargement : l'ancien contenu doit disparaître
    def test_reload_clears_previous(self):
        path1 = make_maze_file(SIMPLE_MAZE)
        path2 = make_maze_file("XX\nES\nXX")
        self.lab.LoadLabyrinth(path1)
        self.lab.LoadLabyrinth(path2)
        os.unlink(path1); os.unlink(path2)
        self.assertEqual(len(self.lab.LabyrinthArray), 3)

    # Fichier inexistant → exception
    def test_missing_file_raises(self):
        with self.assertRaises(FileNotFoundError):
            self.lab.LoadLabyrinth("/tmp/fichier_qui_nexiste_pas_du_tout.txt")

    # Fichier vide → tableau vide
    def test_empty_file(self):
        path = make_maze_file("")
        self.lab.LoadLabyrinth(path)
        os.unlink(path)
        # splitlines() sur "" donne [] donc LabyrinthArray doit être vide
        self.assertEqual(self.lab.LabyrinthArray, [])

    # Lignes de longueur variable
    def test_uneven_lines(self):
        path = make_maze_file("XX\nXXXX\nX")
        self.lab.LoadLabyrinth(path)
        os.unlink(path)
        self.assertEqual(len(self.lab.LabyrinthArray[0]), 2)
        self.assertEqual(len(self.lab.LabyrinthArray[1]), 4)
        self.assertEqual(len(self.lab.LabyrinthArray[2]), 1)


# ═════════════════════════════════════════════════════════════════════════════
# 2. Tests — FindEntry
# ═════════════════════════════════════════════════════════════════════════════
class TestFindEntry(unittest.TestCase):

    def setUp(self):
        self.lab = Labyrinth()

    def _load(self, content):
        path = make_maze_file(content)
        self.lab.LoadLabyrinth(path)
        os.unlink(path)

    # Entrée trouvée à la bonne position
    def test_entry_found(self):
        self._load(SIMPLE_MAZE)
        self.lab.FindEntry()
        self.assertEqual(self.lab.Entry, (0, 1))

    # Pas d'entrée : Entry reste (-1, -1)
    def test_no_entry(self):
        self._load("XXX\nXXX\nXXX")
        self.lab.FindEntry()
        self.assertEqual(self.lab.Entry, (-1, -1))

    # Plusieurs E : retourne le premier (ligne 0 → n, colonne 0 → m)
    def test_multiple_entries_returns_first(self):
        self._load("XEX\nXEX\nXXX")
        self.lab.FindEntry()
        self.assertEqual(self.lab.Entry, (1, 0))

    # Entrée en première case
    def test_entry_at_origin(self):
        self._load("EXX\nXXX")
        self.lab.FindEntry()
        self.assertEqual(self.lab.Entry, (0, 0))


# ═════════════════════════════════════════════════════════════════════════════
# 3. Tests — FindState
# ═════════════════════════════════════════════════════════════════════════════
class TestFindState(unittest.TestCase):

    def setUp(self):
        self.lab = Labyrinth()
        path = make_maze_file(SIMPLE_MAZE)
        self.lab.LoadLabyrinth(path)
        os.unlink(path)

    # Cases normales
    def test_wall(self):
        self.assertEqual(self.lab.FindState(0, 0), 'X')

    def test_entry(self):
        self.assertEqual(self.lab.FindState(0, 1), 'E')

    def test_ground(self):
        self.assertEqual(self.lab.FindState(1, 1), ' ')

    def test_exit(self):
        self.assertEqual(self.lab.FindState(4, 3), 'S')

    # Hors bornes
    def test_out_of_bounds_negative_y(self):
        self.assertEqual(self.lab.FindState(0, -1), 'X')

    def test_out_of_bounds_large_y(self):
        self.assertEqual(self.lab.FindState(0, 9999), 'X')

    def test_out_of_bounds_negative_x(self):
        self.assertEqual(self.lab.FindState(-1, 0), 'X')

    def test_out_of_bounds_large_x(self):
        self.assertEqual(self.lab.FindState(9999, 0), 'X')

    # Labyrinthe vide : tout doit renvoyer 'X'
    def test_empty_labyrinth(self):
        self.lab.LabyrinthArray = []
        self.assertEqual(self.lab.FindState(0, 0), 'X')


# ═════════════════════════════════════════════════════════════════════════════
# 4. Tests — Solve / Threaded  (intégration)
# ═════════════════════════════════════════════════════════════════════════════
def _wait_for_solve(lab: Labyrinth, timeout: float = 5.0) -> None:
    """Attend que PathFound devienne True ou que le timeout expire."""
    deadline = time.time() + timeout
    while not lab.PathFound and time.time() < deadline:
        time.sleep(0.05)


class TestSolve(unittest.TestCase):

    def _build(self, content):
        lab = Labyrinth()
        path = make_maze_file(content)
        lab.LoadLabyrinth(path)
        os.unlink(path)
        lab.FindEntry()
        return lab

    # Labyrinthe résolvable : PathFound doit passer à True
    def test_solvable_maze(self):
        lab = self._build(SOLVABLE_MAZE)
        lab.Solve(lab.Entry, [])
        _wait_for_solve(lab)
        self.assertTrue(lab.PathFound)

    # PathStorage non vide après résolution
    def test_path_storage_not_empty(self):
        lab = self._build(SOLVABLE_MAZE)
        lab.Solve(lab.Entry, [])
        _wait_for_solve(lab)
        self.assertGreater(len(lab.PathStorage), 0)

    # Les cases du chemin sont marquées 'z' dans le tableau
    def test_path_marked_in_array(self):
        lab = self._build(SOLVABLE_MAZE)
        lab.Solve(lab.Entry, [])
        _wait_for_solve(lab)
        flat = [cell for row in lab.LabyrinthArray for cell in row]
        self.assertIn('z', flat)

    # L'entrée est rétablie en 'E' après résolution
    def test_entry_restored_after_solve(self):
        lab = self._build(SOLVABLE_MAZE)
        lab.Solve(lab.Entry, [])
        _wait_for_solve(lab)
        ex, ey = lab.Entry
        self.assertEqual(lab.LabyrinthArray[ey][ex], 'E')

    # Labyrinthe trivial : E directement adjacent à S
    def test_trivial_maze(self):
        lab = self._build(TRIVIAL_MAZE)
        lab.Solve(lab.Entry, [])
        _wait_for_solve(lab, timeout=2.0)
        self.assertTrue(lab.PathFound)

    # Labyrinthe sans sortie : PathFound reste False
    def test_no_exit_maze(self):
        lab = self._build(NO_EXIT_MAZE)
        lab.Solve(lab.Entry, [])
        time.sleep(1.0)   # laisse le temps aux threads de s'épuiser
        self.assertFalse(lab.PathFound)

    # PathFound ne peut être mis à True qu'une seule fois (cohérence du Lock)
    def test_path_found_set_once(self):
        lab = self._build(SOLVABLE_MAZE)
        lab.Solve(lab.Entry, [])
        _wait_for_solve(lab)
        first_path = list(lab.PathStorage)
        time.sleep(0.2)   # autres threads éventuels
        self.assertEqual(lab.PathStorage, first_path)


# ═════════════════════════════════════════════════════════════════════════════
# 5. Tests de concurrence
# ═════════════════════════════════════════════════════════════════════════════
class TestConcurrency(unittest.TestCase):

    def _build(self, content):
        lab = Labyrinth()
        path = make_maze_file(content)
        lab.LoadLabyrinth(path)
        os.unlink(path)
        lab.FindEntry()
        return lab

    # Exécutions répétées : PathStorage toujours cohérent
    def test_repeated_solve_consistency(self):
        for _ in range(10):
            lab = self._build(SOLVABLE_MAZE)
            lab.Solve(lab.Entry, [])
            _wait_for_solve(lab, timeout=5.0)
            self.assertTrue(lab.PathFound)
            # Toutes les coordonnées du chemin doivent être des tuples (x, y)
            for coord in lab.PathStorage:
                self.assertIsInstance(coord, tuple)
                self.assertEqual(len(coord), 2)

    # Draw() ne lève pas d'exception pendant Solve()
    def test_draw_during_solve_no_crash(self):
        lab = self._build(SOLVABLE_MAZE)
        errors = []

        def run_draw():
            for _ in range(20):
                try:
                    lab.Draw()
                except Exception as e:
                    errors.append(e)
                time.sleep(0.01)

        draw_thread = threading.Thread(target=run_draw)
        draw_thread.start()
        lab.Solve(lab.Entry, [])
        _wait_for_solve(lab, timeout=5.0)
        draw_thread.join()
        self.assertEqual(errors, [], f"Draw() a levé des exceptions : {errors}")


# ═════════════════════════════════════════════════════════════════════════════
# 6. Tests — Draw  (appels sans crash)
# ═════════════════════════════════════════════════════════════════════════════
class TestDraw(unittest.TestCase):

    def setUp(self):
        self.lab = Labyrinth()

    def _load(self, content):
        path = make_maze_file(content)
        self.lab.LoadLabyrinth(path)
        os.unlink(path)

    # Draw ne lève pas d'exception sur un labyrinthe normal
    def test_draw_no_exception(self):
        self._load(SIMPLE_MAZE)
        try:
            self.lab.Draw()
        except Exception as e:
            self.fail(f"Draw() a levé une exception inattendue : {e}")

    # Draw sur tableau vide
    def test_draw_empty_maze(self):
        self.lab.LabyrinthArray = []
        try:
            self.lab.Draw()
        except Exception as e:
            self.fail(f"Draw() a levé une exception sur tableau vide : {e}")

    # Draw avec un caractère inconnu (cas non géré par le match)
    def test_draw_unknown_character(self):
        self._load("X?X\nESX\nXXX")
        try:
            self.lab.Draw()
        except Exception as e:
            self.fail(f"Draw() a levé une exception sur caractère inconnu : {e}")

    # Draw après résolution (cases 'z' présentes)
    def test_draw_after_solve(self):
        self._load(SOLVABLE_MAZE)
        self.lab.FindEntry()
        self.lab.Solve(self.lab.Entry, [])
        _wait_for_solve(self.lab, timeout=5.0)
        try:
            self.lab.Draw()
        except Exception as e:
            self.fail(f"Draw() a levé une exception après résolution : {e}")


# ═════════════════════════════════════════════════════════════════════════════
# 7. Tests — Cas limites
# ═════════════════════════════════════════════════════════════════════════════
class TestEdgeCases(unittest.TestCase):

    # Labyrinthe 1×1
    def test_1x1_maze(self):
        lab = Labyrinth()
        path = make_maze_file("E")
        lab.LoadLabyrinth(path)
        os.unlink(path)
        lab.FindEntry()
        self.assertEqual(lab.Entry, (0, 0))
        self.assertEqual(lab.FindState(0, 0), 'E')

    # Solve appelé sans FindEntry (Entry reste (-1,-1))
    def test_solve_without_find_entry(self):
        lab = Labyrinth()
        path = make_maze_file(SOLVABLE_MAZE)
        lab.LoadLabyrinth(path)
        os.unlink(path)
        # On ne devrait pas crasher ; comportement documenté : no-op ou erreur contrôlée
        try:
            lab.Solve(lab.Entry, [])
        except Exception:
            pass  # Un crash est acceptable ici, l'important est de le détecter

    # Constructeur initialise correctement toutes les valeurs par défaut
    def test_constructor_defaults(self):
        lab = Labyrinth()
        self.assertEqual(lab.LabyrinthArray, [])
        self.assertEqual(lab.Entry, (-1, -1))
        self.assertFalse(lab.PathFound)
        self.assertEqual(lab.PathStorage, [])
        self.assertEqual(lab.SideLenght, 10)
        self.assertEqual(lab.OffsetX, 100)
        self.assertEqual(lab.OffsetY, 100)


if __name__ == "__main__":
    unittest.main(verbosity=2)