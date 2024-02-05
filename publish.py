import os

os.system("cd C:\Users\Pichau\Documents\Projetos\\blog-source")
os.system("git add *")
os.system("git commit -m" + input("Commit message: "))
os.system("git push")
os.system("cd /public/ && git add * && git commit -m" + input("Commit message: "))
os.system("git push")
