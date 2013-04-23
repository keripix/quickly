# Quickly

Quickly is a small python command-line script enabling you to do change directory (`cd`) without having to type the whole path. It does this by mapping a specified key to a path. The key and the path are set by the user.

## Example

We want to be able to `cd` quickly to the path: `/path/to/a/directory`. So the step is:

    $ quickly -add /path/to/a/directory -as a_dir

The above command will tell quickly to store `/path/to/a/directory` as `a_dir`. To `cd` to `/path/to/a/directory`, you just type:

    $ quickly a_dir

And quickly will bring you to `/path/to/a/directory`.