# x
Python3 lib to get stdin super easy. `ls | python3 -c "import x; print(x)" `

Add this to your `.bashrc` after cloning: 

    export PYTHONPATH=$PYTHONPATH:/wherever/you/cloned/this

If you want to streamline bash further add this to you `.bashrc`:

    function pawk() { python3 -c "from glob import glob; from os.path import join; import sys; import x; "$@; }

Then you can `ls | pawk 'print(x)'`
