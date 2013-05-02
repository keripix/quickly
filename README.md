# Quickly

Quickly is a small python command-line script enabling you to do change directory (`cd`) without having to type the whole path. It does this by mapping a specified key to the path. The key and the path are set by the user.

## WARNING: Alpha Quality Software

The software has been unit tested. But in no way I'm claiming that the tests are complete.

The software has also been tested manually on ArchLinux, and is running as expected. But please see the TODO section below to know why I still consider this an alpha quality software.

## Example

We want to be able to `cd` quickly to the path: `/path/to/a/directory`. So the step is:

    $ q -a a_dir /path/to/a/directory

The above command will tell quickly to store `/path/to/a/directory` as `a_dir`.

To `cd` to `/path/to/a/directory`, you just type:

    $ q a_dir

And quickly will change your current working directory to `/path/to/a/directory`.

## Other Available Options

To remove a key from quickly, run:

    $ q -rm a_dir

To update a key and map it to a different path:

    $ q -e a_dir /another/path

To show the list of key and its mapped path:

    $ q -ls

## Install

Currently, the installation process is still manual.

1. Clone this repo
2. Link the q.py file to a path that is recognised by your command line $PATH environment.
3. Copy q.sh to /etc/profile.d/
4. Restart (maybe?)

I'm still studying how to distribute this software properly.

## Contribute

TODO

## Test

> python -m unittest tests/*.py -v

I'm also still finding a way to run the test easily.

## TODO

1. Autocompletion
2. Better way to install and distribute
3. Easier step to test