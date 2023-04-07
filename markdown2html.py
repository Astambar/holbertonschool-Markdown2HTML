#!/usr/bin/python3
"""Markdown to HTML converter"""


import sys
import os
import re


def convert_md_to_html(md_filename: str, html_filename: str) -> None:
    """Converts a markdown file to an HTML file"""
    if not os.path.exists(md_filename):
        sys.stderr.write("Missing {}\n".format(md_filename))
        sys.exit(1)

    with open(md_filename, 'r') as md_file:
        with open(html_filename, 'w') as html_file:
            for line in md_file:
                line = line.rstrip()
                if re.match(r'^#', line):
                    level = len(line.split()[0])
                    content = line[level + 1:]
                    html_file.write('<h{}>{}</h{}>\n'.format(level, content, level))
                elif re.match(r'^-', line):
                    html_file.write('<ul>\n')
                    while re.match(r'^-', line):
                        content = line[2:]
                        html_file.write('<li>{}</li>\n'.format(content))
                        line = md_file.readline().rstrip()
                    html_file.write('</ul>\n')
                elif re.match(r'^\*', line):
                    html_file.write('<ol>\n')
                    while re.match(r'^\*', line):
                        content = line[2:]
                        html_file.write('<li>{}</li>\n'.format(content))
                        line = md_file.readline().rstrip()
                    html_file.write('</ol>\n')
                else:
                    html_file.write('<p>{}</p>\n'.format(line))


if __name__ == '__main__':
    if len(sys.argv) < 3:
        sys.stderr.write("Usage: ./markdown2html.py README.md README.html\n")
        sys.exit(1)

    md_filename = sys.argv[1]
    html_filename = sys.argv[2]

    convert_md_to_html(md_filename, html_filename)
