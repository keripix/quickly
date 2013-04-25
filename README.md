# Quickly

Quickly is a small python command-line script enabling you to do change directory (`cd`) without having to type the whole path. It does this by mapping a specified key to a path. The key and the path are set by the user.

## Example

We want to be able to `cd` quickly to the path: `/path/to/a/directory`. So the step is:

    $ q add a_dir /path/to/a/directory

The above command will tell quickly to store `/path/to/a/directory` as `a_dir`.

To `cd` to `/path/to/a/directory`, you just type:

    $ q a_dir

And quickly will change your current working directory to `/path/to/a/directory`.

## Other Available Options

To remove a key from quickly, run:

    $ q rm a_dir

To update a key and map it to a different path:

    $ q edit a_dir /another/path

To show the list of key and its mapped path:

    $ q ls

## Install

TODO

## Contribute

TODO

### Test

TODO