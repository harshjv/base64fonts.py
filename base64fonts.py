#!/usr/bin/env python

from __future__ import print_function
import os
import pathlib
import base64
import argparse
from colorama import init, Fore, Style

less_template = '@{basename}-{style}: "url(data:application/{font_mime};charset=utf-8;base64,{encoded_string}) format(\'{font_type}\')";\n'
sass_template = '${basename}-{style}: "url(data:application/{font_mime};charset=utf-8;base64,{encoded_string}) format(\'{font_type}\')";\n'


FORMAT_MAP = {
    'less': less_template,
    'sass': sass_template
}

EXT_MAP = {
    '.ttf': ['font/ttf', 'truetype'],
    '.woff': ['application/font-woff', 'woff'],
    '.woff2': ['application/font-woff2', 'woff2'],
    '.eot': ['application/vnd.ms-fontobject', 'eot'],
    '.otf': ['application/x-font-opentype', 'opentype']
}


def convert(input_dir, output_dir, preprocessor):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    output_file_name_template = '{font_name}{seperator}{suffix}.{extension}'

    font_dirs = [ p for p in pathlib.Path(input_dir).iterdir() if p.is_dir() ]

    print(Style.BRIGHT + Fore.RED + 'Font directories: %d' % len(font_dirs))

    i = 1

    for font_dir in font_dirs:
        fonts = [ w for w in font_dir.iterdir() if w.is_file() and w.suffix in EXT_MAP.keys() ]
        font_name = font_dir.name.lower()

        s = '{BRIGHT}{MAGENTA} ({INDEX}/{TOTAL}) {FONT_NAME}{RESET_ALL} {BRIGHT}{MAGENTA}({STYLE_COUNT} styles) '
        s = s.format(BRIGHT=Style.BRIGHT, RESET_ALL=Style.RESET_ALL, MAGENTA=Fore.MAGENTA, INDEX=i, TOTAL=len(font_dirs), FONT_NAME=font_name, STYLE_COUNT=len(fonts))

        print(s)

        output_file_name = output_file_name_template.format(font_name=font_name, seperator='-', suffix='data', extension=preprocessor)
        output_file_path = os.path.join(output_dir, output_file_name)

        with open(output_file_path, 'w') as out:
            for font in fonts:
                file_name = font.stem.lower()
                index = file_name.index('-') + 1
                style = file_name[index:len(file_name)]

                print(Style.BRIGHT + Fore.CYAN + ' ----> {style} ({type}, {mime})'.format(style=style, mime=EXT_MAP[font.suffix][0], type=EXT_MAP[font.suffix][1]), end='')
                print(Style.DIM + ' to ' + output_file_path)

                with font.open('rb') as woff_file:
                    encoded_string = base64.b64encode(woff_file.read()).decode('UTF-8')
                    d = FORMAT_MAP[preprocessor].format(font_mime=EXT_MAP[font.suffix][0], font_type=EXT_MAP[font.suffix][1], basename=font_name, style=style, encoded_string=encoded_string)
                    out.write(d)

        i = i + 1

        print('')


def main():
    parser = argparse.ArgumentParser(description='Batch convert fonts to base64 with SASS and LESS importable format')
    parser.add_argument('input', metavar='i', type=str, nargs=1, help='path of input directory')
    parser.add_argument('output', metavar='o', type=str, nargs=1, help='path of output directory')
    parser.add_argument('preprocessor', metavar='p', choices=FORMAT_MAP.keys(), help='preprocessor')
    args = parser.parse_args()

    init(autoreset=True)
    convert(input_dir=args.input[0],
            output_dir=args.output[0],
            preprocessor=args.preprocessor)


if __name__ == '__main__':
    main()
