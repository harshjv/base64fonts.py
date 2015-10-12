# base64fonts.py

Batch convert fonts to base64 with SASS and LESS importable format


## Usage

    $ python convert.py --help

```
positional arguments:
  i           path of input directory
  o           path of output directory
  p           preprocessor

optional arguments:
  -h, --help  show this help message and exit
```


## Example

    $ python convert.py example/fonts/woff example/less less

```
Font directories: 3
 (1/3) hack (4 styles)
 ----> bold (woff, application/font-woff) to example/less/hack-data.less
 ----> boldoblique (woff, application/font-woff) to example/less/hack-data.less
 ----> regular (woff, application/font-woff) to example/less/hack-data.less
 ----> regularoblique (woff, application/font-woff) to example/less/hack-data.less

 (2/3) open-sans (4 styles)
 ----> bold (woff, application/font-woff) to example/less/open-sans-data.less
 ----> bolditalic (woff, application/font-woff) to example/less/open-sans-data.less
 ----> italic (woff, application/font-woff) to example/less/open-sans-data.less
 ----> regular (woff, application/font-woff) to example/less/open-sans-data.less

 (3/3) ubuntu-mono (4 styles)
 ----> bold (woff, application/font-woff) to example/less/ubuntu-mono-data.less
 ----> bolditalic (woff, application/font-woff) to example/less/ubuntu-mono-data.less
 ----> italic (woff, application/font-woff) to example/less/ubuntu-mono-data.less
 ----> regular (woff, application/font-woff) to example/less/ubuntu-mono-data.less
```


## Contribute

Make a pull request!
