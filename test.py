import os

current = dir_path = os.path.dirname(os.path.realpath(__file__))
print(current)

os.chdir(current)
print(os.getcwd())
