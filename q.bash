#!/bin/bash

q() {
    res=$(q.py $@)

    if [ -d "$res" ]; then
        cd $res
    else
        echo $res
    fi
}