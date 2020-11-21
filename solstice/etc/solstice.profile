#!/bin/bash

solstice_path=$(dirname $(dirname $(realpath $BASH_SOURCE)))

export LD_LIBRARY_PATH=$solstice_path/lib:${LD_LIBRARY_PATH}
export PATH=$solstice_path/bin:${PATH}
export MANPATH=$solstice_path/share/man/:${MANPATH}
