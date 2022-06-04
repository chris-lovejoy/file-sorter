#!/usr/bin/python
# -*- coding: utf-8 -*-

file_extension = ".md"
top_x_lines = True
num_x_lines = 10

# (add way to deal with multi-snippets)


# DICTIONARY TO SPECIFY MAPPING OF TEXT SNIPPETS TO FILE DIRECTORY
snippet_directory_mapping = {

    ## Topic tags
    "#topic/testTag1" : "/Users/chrislovejoy/Local/1_CODE/1_active/automatic-file-sorter/test_folder1",
    "#topic/testTag2" : "/Users/chrislovejoy/Local/1_CODE/1_active/automatic-file-sorter/test_folder2",
    "#topic/PhilosophyPsychology" : "test_folder1"
    # TODO: figure out how to specify multi-level folders in an operating system agnostic way

    ## Other content types
    # TODO: add tags for whether e.g. a person / company page

}



folders_to_ignore = [
    # TODO: add directories to ignore (and implement logic in main script)
]

