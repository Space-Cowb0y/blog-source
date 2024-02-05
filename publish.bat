cd C:\Users\Pichau\Documents\Projetos\blog-source
hugo
git add *
git commit -m %1
cd public
git add *
git commit -m %2
git push
cd ..
git push --recurse-submodules=on-demand