#!/usr/bin/env python
# encoding: utf-8

"""
.. codeauthor:: Tsuyoshi Hombashi <gogogo.vm@gmail.com>
"""

from __future__ import unicode_literals
import sys

import readmemaker


PROJECT_NAME = "SimpleSQLite"
OUTPUT_DIR = ".."


def write_examples(maker):
    maker.set_indent_level(0)
    maker.write_chapter("Examples")

    maker.inc_indent_level()
    maker.write_chapter("Create a table")
    maker.inc_indent_level()
    maker.write_chapter("Create a table from data matrix")
    maker.write_example_file("create_table_from_data_matrix.txt")

    maker.write_chapter("Create a table from CSV")
    maker.write_example_file("create_table_from_csv.txt")

    maker.dec_indent_level()
    maker.write_chapter("Insert records into a table")
    maker.write_example_file("insert_record_example.txt")

    maker.write_chapter("For more information")
    maker.write_line_list([
        "More examples are available at ",
        "http://{:s}.rtfd.io/en/latest/pages/examples/index.html".format(
            PROJECT_NAME.lower()),
    ])


def main():
    maker = readmemaker.ReadmeMaker(PROJECT_NAME, OUTPUT_DIR)

    maker.write_introduction_file("badges.txt")

    maker.inc_indent_level()
    maker.write_chapter("Summary")
    maker.write_introduction_file("summary.txt")
    maker.write_introduction_file("feature.txt")

    write_examples(maker)

    maker.write_file(
        maker.doc_page_root_dir_path.joinpath("installation.rst"))

    maker.set_indent_level(0)
    maker.write_chapter("Documentation")
    maker.write_line_list([
        "http://{:s}.rtfd.io/".format(PROJECT_NAME.lower()),
    ])

    maker.write_chapter("Related project")
    maker.write_line_list([
        "- `sqlitebiter <https://github.com/thombashi/sqlitebiter>`__: "
        "CLI tool to convert CSV/Excel/HTML/JSON/LTSV/Markdown/TSV/Google-Sheets "
        "SQLite database by using SimpleSQLite",
    ])

    return 0


if __name__ == '__main__':
    sys.exit(main())
