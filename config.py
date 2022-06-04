#!/usr/bin/python
# -*- coding: utf-8 -*-

file_extension = ".md"
top_x_lines = True
num_x_lines = 10
multi_snippet_method = "first"


# DICTIONARY TO SPECIFY MAPPING OF TEXT SNIPPETS TO FILE DIRECTORY
snippet_directory_mapping = {

    ## Topic tags
    "#topic/testTag1" : "/Users/chrislovejoy/Local/1_CODE/1_active/automatic-file-sorter/test_folder1",
    "#topic/testTag2" : "/Users/chrislovejoy/Local/1_CODE/1_active/automatic-file-sorter/test_folder2",
    "#topic/PhilosophyPsychology" : "/Users/chrislovejoy/Local/1_CODE/1_active/automatic-file-sorter/test_folder1"

    ## Other content types
    # TODO: add tags for whether e.g. a person / company page

}



folders_to_ignore = [
    # TODO: add directories to ignore (and implement logic in main script)
]

