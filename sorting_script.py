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
                top_x_lines_list = f.readlines()[:config.num_x_lines]
                for line in top_x_lines_list:
                    if snippet in line:
                        snippet_present[snippet] = 1
                # TODO: run a test to see if this is faster
                print(f"looking at top {config.num_x_lines} lines for snippet {snippet}")
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
        selected_snippet = resolve_multi_snippet(snippet_present, root, file)
        return(True, selected_snippet)


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


def resolve_multi_snippet(snippet_present_dict, root, file):
    if config.multi_snippet_method == "first":
        earliest_index = float('inf')
        earliest_snippet = ""
        with open(os.path.join(root,file), 'r') as f:
            file_contents = f.read()
            for key in snippet_present_dict.keys():
                if snippet_present_dict[key] == 1:
                    snippet_index = file_contents.find(key)
                    if snippet_index < earliest_index:
                        earliest_index = snippet_index
                        earliest_snippet = key
                # print(f"earliest index is {earliest_index} and earliest_snippet is {earliest_snippet}.")
        selected_snippet = earliest_snippet

    # TODO: add more options for dealing with multiple snippets. For example, based on priority

    return selected_snippet


### COMMAND LINE CALL

if __name__ == "__main__":
    root_dir = os.getcwd()
    sort_files(root_dir)