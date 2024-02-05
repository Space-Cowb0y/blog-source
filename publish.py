import os

os.system("cd C:\\Users\\Pichau\\Documents\\Projetos\\blog-source")
os.system("hugo")
os.system("git add *")
os.system("git commit -m" + input("Commit message dev: "))
os.system("git push --recurse-submodules=on-demand")
os.system("cd .\public")
os.system("git add * && git commit -m" + input("Commit message prod: ") + " && git push")