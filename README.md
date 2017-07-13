# x
Python3 lib to get stdin super easy. `ls | python3 -c "import x; print(x)" `

# Quickstart

This will clone the repo and then add it to your python path: 

    git clone https://github.com/Benhgift/x.git
    echo 'export PYTHONPATH=$PYTHONPATH:'`pwd` >> ~/.bashrc
    source ~/.bashrc
    
done
    
--- 

If you want to streamline bash further add this to you `.bashrc`:

    function pawk() { python3 -c "from glob import glob; from os.path import join; import sys; import x; "$@; }

Then you can `ls | pawk 'print(x)'`
