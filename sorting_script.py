#!/usr/bin/python
# -*- coding: utf-8 -*-

import config
import os
import logging
from datetime import datetime


def sort_files(root_dir):

    move_counter = 0
    initiate_log_file()
    logging.info(f"Commencing sequence in f{root_dir}.")

    for root,dirs,files in os.walk(root_dir):

        for file in files:
            if(file.endswith(config.file_extension)):

                print(f"Looking at file {root}/{file}.")

                (present, snippet) = check_for_snippet(root,file)

                if present:
                    move_counter = move_file(root,file,snippet,move_counter)

                else:
                    break

                # TODO: consider saving up the required file moves until later, and executing together
                # IN PARTICULAR, because may currently will try to move some files twice - as loops 
                # back over them (once moved into a subfolder)

    logging.info(f"File sorting complete. In total, {move_counter} files were moved.")

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
                # See previous implemnentation for template for this
                print("top x lines")
                pass
            else:
                if snippet in f.read():
                    snippet_present[snippet] = 1

    if sum(snippet_present.values()) == 0:
        print(f"no snippets present in file.")
        return (False, "")
    elif sum(snippet_present.values()) == 1:
        selected_snippet = get_key(snippet_present, 1)
        return(True, selected_snippet)
    else:
        print("more than one snippet present")
        return (False, "") # TODO: update to return True + the selected snippet
        # TODO: add logic to deal with multiple snippets being present
        # will likely involve looking at which appears first.
        # probably write a separate function to check this


def move_file(root,file,snippet,move_counter):
    new_root = config.snippet_directory_mapping[snippet]

    if root == new_root:
        print("file", file, "contains snippet but file already in correct location.")
        return move_counter

    else:
        logging.info(f"moving file {file} from {root} to {new_root}")
        print(f"moving file {file} from {root} to {new_root}")
        os.rename(os.path.join(root,file),os.path.join(new_root,file))
        move_counter += 1
        return move_counter


# TODO: add a script that checks for existence of all folders specified in the 
# snippet_directory_mapping config. (as if folders don't exist, ie. when I've re-named
# them, I don't want to create them)
# (note: I can use this as a separately-run script to check for changes to file structure.)


### HELPER FUNCTIONS

def get_key(my_dict, val):
    """Returns the dictionary key based on the specific value"""
    for key, value in my_dict.items():
         if val == value:
             return key
    return "key doesn't exist"


def initiate_log_file():
    date_time_now = str(datetime.now())[:16].replace(" ","_")
    python_script_dir = os.path.dirname(os.path.realpath(__file__))
    log_filename = os.path.join(python_script_dir,"logs",f"{date_time_now}.log")
    logging.basicConfig(filename=log_filename,
                        format='%(asctime)s - %(message)s',
                        level=logging.INFO)
    return None


### COMMAND LINE CALL

if __name__ == "__main__":
    root_dir = os.getcwd() # TODO: check whether this uses current directory or directory of sorting_script.py
    sort_files(root_dir)