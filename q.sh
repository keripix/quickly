#!/bin/sh
#eval "$(register-python-argcomplete /home/keripix/bin/q.py)"

q(){
    res=$(q.py $@)

    if [ -d "$res" ]; then
        cd $res
    else
        echo $res
    fi
}