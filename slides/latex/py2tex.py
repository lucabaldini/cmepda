#! /usr/bin/env python
#
# -----------------------------------------------------------------------------
# Copyright (C) 2019 Luca Baldini (luca.baldini@pi.infn.it)
#
# For the license terms see the file LICENCE, distributed
# along with this software.
# -----------------------------------------------------------------------------
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.


import glob
import os
import sys
import subprocess


PACKAGE_ROOT = os.path.abspath(os.path.dirname(__file__))
SNIPPET_FOLDER_PATH = os.path.join(PACKAGE_ROOT, 'snippets')
PYGMENT_FOLDER_PATH = os.path.join(PACKAGE_ROOT, 'pygments')

GITHUB_URL = 'https://github.com/lucabaldini/cmepda/tree/master/slides/latex/'

PROC_KWARGS = dict(stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)

NO_OUTPUT_SCRIPTS = []


def _decode(b):
    """Decode a byte object from subprocess.Popen.

    See https://stackoverflow.com/questions/606191/convert-bytes-to-a-string
    """
    return b.decode(sys.stdout.encoding)

def run_snippet(file_path):
    """Run a python snippet and capture the output.
    """
    assert(file_path.endswith('.py'))
    print('Executing the snippet %s...' % file_path)
    cmd = 'python %s' % file_path
    with subprocess.Popen(cmd, **PROC_KWARGS) as process:
        error = process.stderr.read()
        output = process.stdout.read()
        if error:
            print(error)
            output += error
        return output

def run_pygmentize(file_path, label=True):
    """Run the pygmentize application and format the output in a suitable
    form for the target LaTeX file.

    Args
    ----
    file_path: str
        the path to the input snippet file.

    label: bool
        if True, add a github link to the code box.

    This is achieved through something along the lines of:
    pygmentize -f latex -O full -l python file.py
    We do not produce the output LaTeX file directly, as we include the
    necessary pygmentize-related LaTeX macros into the preamble and we
    filter the pygmentize output to:
    1 - strip the un-necessary preamble
    2 - add the python output at the end of the file.

    The function is spawning a process running the pygmentize application, and
    piping the output internally.
    """
    assert(file_path.endswith('.py'))
    # Run pygmentize.
    print('Running pygments on %s...' % file_path)
    cmd = 'pygmentize -f latex -O full -l python %s' % file_path
    with subprocess.Popen(cmd, **PROC_KWARGS) as process:
        output = process.stdout.readlines()
    # Open the the output file path.
    file_name = os.path.basename(file_path)
    output_file_path = os.path.join(PYGMENT_FOLDER_PATH,
                                    file_name.replace('.py', '.tex'))
    print('Opening output file %s...' % output_file_path)
    with open(output_file_path, 'w') as output_file:
        # Filter the output and limit to the interesting part, i.e., the main
        # fancyverb block.
        do_write = False
        for line in output:
            line = _decode(line)
            if line.startswith('\\begin{Verbatim}'):
                do_write = True
                if label:
                    text = file_name.replace('_', '\_')
                    folder = os.path.dirname(file_path)
                    folder = folder.replace(PACKAGE_ROOT, '').strip('\/')
                    text = '%s%s/%s' % (GITHUB_URL, folder, text)
                    text = '\\makebox{\\url{%s}}' % text
                    line = line.replace('[', '[label=%s,' % text)
            # We don't want to write the \end{Verbatim} bit at the first pass,
            # as we typically need to add the output.
            elif line.startswith('\\end{Verbatim}'):
                do_write = False
            if do_write:
                output_file.write(line)
        # At this point we're done with parsing the pygmentized text, and
        # we can proceed with the code outoput.
        snip_out = run_snippet(file_path)
        if len(snip_out):
            output_file.write('\n[Output]\n%s' % _decode(snip_out))
        output_file.write('\\end{Verbatim}')
    print('Done.')

def pygmentize(target_path, label=True):
    """Run pygments on a python script and generate the corresponding
    LaTeX output.

    If the target_path argument points to a directory, all the python files in
    the directory are recursively translated.
    """
    # Are we pointing to a folder?
    if os.path.isdir(target_path):
        print('Pygmentizing folder %s...' % target_path)
        for file_path in glob.glob(os.path.join(target_path, '*.py')):
            pygmentize(file_path)
        return
    # If we're pointing to a file, is its extension correct?
    if not target_path.endswith('.py'):
        print('%s does not look like a python file, skipping...'% target_path)
        return
    # Ready to go. Ho ho ho!!!
    run_pygmentize(target_path)



if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Process Python snippets')
    parser.add_argument('targets', nargs='+')
    args = parser.parse_args()
    for target in args.targets:
        pygmentize(target)
