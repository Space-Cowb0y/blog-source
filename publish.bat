cd C:\Users\Pichau\Documents\Projetos\blog-source
hugo
git add *
git commit -m %1
git push --recurse-submodules=on-demand
cd public
git add * && git commit -m %2 && git push
cd ..