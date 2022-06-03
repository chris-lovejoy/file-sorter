#!/usr/bin/python
# -*- coding: utf-8 -*-

file_extension = ".md"
top_x_lines = False
num_x_lines = 10


# DICTIONARY TO SPECIFY MAPPING OF TEXT SNIPPETS TO FILE DIRECTORY
snippet_directory_mapping = {

    ## Topic tags
    "#topic/testTag1" : "test_folder1",
    "#topic/testTag2" : "test_folder2",
    "#topic/ContentCreation🎤" : "3. Resources/Approach to Content Creation",
    "#topic/PhilosophyPsychology" : "test_folder1"
    # TODO: figure out how to specify multi-level folders in an operating system agnostic way

    ## Other content types
    # TODO: add tags for whether e.g. a person / company page

}


folders_to_ignore = [
    # TODO: add directories to ignore (and implement logic in main script)
]