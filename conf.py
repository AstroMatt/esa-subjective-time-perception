#!/usr/bin/env python3

import datetime
import subprocess


project = 'Subjective Time Perception'
author = 'Matt Harasymczuk'
copyright = '2016-{date:%Y}, Matt Harasymczuk <matt@astrotech.io>'.format(date=datetime.date.today())
language = 'en'

extensions = []

master_doc = 'README'
pygments_style = 'vs'
today_fmt = '%Y-%m-%d'
highlight_language = 'python3'
source_suffix = ['.rst']
html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_sidebars = {'sidebar': ['localtoc.html', 'sourcelink.html', 'searchbox.html']}
html_show_sphinx = False
htmlhelp_basename = 'Subjective Time Perception'

latex_elements = {
    'papersize': 'a4paper',
    'pointsize': '10pt',
    # 'preamble': '',
    # 'figure_align': 'htbp',
}

latex_documents = [
    (master_doc, 'SubjectiveTimePerception.tex', 'Subjective Time Perception', 'Matt Harasymczuk', 'manual'),
]

man_pages = [
    (master_doc, 'subjective-time-perception', 'Subjective Time Perception', [author], 1)
]

texinfo_documents = [
    (master_doc, 'SubjectiveTimePerception', 'Subjective Time Perception', author, 'SubjectiveTimePerception', 'Subjective Time Perception', 'Miscellaneous'),
]


def get_version():
    shell = subprocess.Popen('git log -1 --format="%h"', stdout=subprocess.PIPE, shell=True)
    return '{sha1}, {date:%Y-%m-%d}'.format(
        sha1=shell.stdout.read().decode().replace('\n', ''),
        date=datetime.date.today(),
    )

version = get_version()
release = get_version()






