class SolverBot:
    def __init__(self, x, y):
        import os
        import sys
        import subprocess
        self.x = x
        self.y = y
        if os.name == "nt":
            subprocess.Popen(f'start cmd /k python -c "print('X: {self.x}, Y: {self.y}')"', shell=True)