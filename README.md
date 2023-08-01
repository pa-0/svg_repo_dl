<div align="center">
	<img src=".github/README/Logo.svg" alt="logo"/>
	<p><strong>SVG_REPO Pack</strong> Downloader - a small personal tool that will allow you to download an icon pack on <a href="https://www.svgrepo.com/">SVG Repo</a> with the CLI.</p>

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![last_commit](https://img.shields.io/github/last-commit/AllanCerveaux/svg_repo_dl?style=flat-square)](https://github.com/AllanCerveaux/svg_repo_dl/commits/master)
[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/AllanCerveaux/svg_repo_dl/blob/master/LICENSE)
</div>

> Nota bene: this repository is based on its [original](https://github.com/AllanCerveaux/svg_repo_dl) from Allan Cerveaux but contains numerous bug fixes - including using `wget` instead of a headless Firefox browser for the actual download

___

## Requirement :

- Python 3
- Selenium
- Progress

## Installation
Follow these steps:

1. Clone the repo
```bash
git clone git@github.com:AllanCerveaux/svg_repo_dl.git
```

2. Go in folder
```bash
cd svg_repo_dl
```

3. And run install.sh
```bash
sh install.sh
```
## Usage :

```bash
$ svgrepodl [URL] --path[-p]
$ svgrepodl --help # Show all commands
$ svgrepodl https://www.svgrepo.com/collection/role-playing-game/ # Run downloader
```

The program saves the icons in `/home/Documents/icons/`.

Enjoy !

> **Nota bene**: SVG Repo seems to be slow - perhaps because of a massive interest in their icons. As a consequence, it may take a while to load one of their HTML pages. This script takes this time into account by waiting for 15 (fifteen!) seconds before analyzing a requested web page. Your milage may vary, but the author had good results with that long delay (and less success with shorter delays)
>
> In order to determine whether all icons could be downloaded or SVG Repo just did not respond in time, the number of successfully loaded icons is printed on the console - just compare that count with the promised number of icons in the collection of your interest.

## License
The MIT License (MIT) 2020 - Callan, Please have a look at the [License](https://github.com/AllanCerveaux/svg_repo_dl/blob/master/LICENSE) for more details.
