import os

os.system("cd C:\\Users\\Pichau\\Documents\\Projetos\\blog-source")
os.system("git add *")
os.system("git commit -m" + input("Commit message dev: "))
os.system("cd .\\public\\ && git add * && git commit -m" + input("Commit message prod: "))
os.system("cd ..")
os.system("git push --recurse-submodules=on-demand")