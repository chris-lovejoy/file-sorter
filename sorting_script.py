#!/usr/bin/python
# -*- coding: utf-8 -*-

import config
import os

root_dir = os.getcwd()

def sort_files():

    for root,dirs,files in os.walk(root_dir):

        for file in files:
            if(file.endswith(config.file_extension)):
                # TODO: enable conditional to accept multiple file extensions

                # temporary print statement
                print(f"\nnow looking at file {root}/{file}.")

                (present, snippet) = check_for_snippet(root,file)

                if present:
                    move_file(root,file, snippet)
                else:
                    break
                    # TODO: check that breaks to the appropriate level

                # TODO: consider saving up the required file moves until later, and executing together
                # IN PARTICULAR, because may currently will try to move some files twice - as loops 
                # back over them (once moved into a subfolder)

    # TODO: add a print / log statement at the end about the total number of files that have been moved.

    return None


def check_for_snippet(root, file):

    snippets = config.snippet_directory_mapping.keys()
    snippet_present = dict.fromkeys(snippets, 0)

    for snippet in snippets:
        with open(os.path.join(root,file), 'r') as f:
            if config.top_x_lines:
                # (add logic for looking only at x number of lines)
                # necessity for this depends on time it takes for long files
                # TODO: implement logic then run a time test to compare
                print("top x lines")
                pass
            else:
                if snippet in f.read():
                    snippet_present[snippet] = 1

    if sum(snippet_present.values()) == 0:
        print(f"no snippets present in file {os.path.join(root,file)}.")
        return (False, "")
    elif sum(snippet_present.values()) == 1:
        selected_snippet = get_key(snippet_present, 1)
        return(True, selected_snippet)
    else:
        print("more than one present")
        return (False, "") # TODO: update to return the selected snippet
        # TODO: add logic to deal with multiple snippets being present
        # will likely involve looking at which appears first.
        # probably write a separate function to check this



def move_file(root,file,snippet):
    new_root = os.path.join(root_dir, config.snippet_directory_mapping[snippet])
        # TODO: modify this so that it uses the full directory

    if root == new_root:
        print("file", file, "contains snippet but already in correct location.")
        return None

    # TODO: add a log for every time this is executed
    print("moving file", file, "\n\tfrom:\t", root, "\n\tto:\t", new_root)
    os.rename(os.path.join(root,file),os.path.join(new_root,file))
    return None




# TODO: add a script that checks for existence of all folders specified in the 
# snippet_directory_mapping config. (as if folders don't exist, ie. when I've re-named
# them, I don't want to create them)



### HELPER FUNCTIONS

def get_key(my_dict, val):
    """Returns the dictionary key based on the specific value"""
    for key, value in my_dict.items():
         if val == value:
             return key
 
    return "key doesn't exist"



### COMMAND LINE CALL

if __name__ == "__main__":
    sort_files()