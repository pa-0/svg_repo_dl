<div align="center">
	<img src=".github/README/Logo.svg" alt="logo"/>
	<p><strong>SVG_REPO Pack</strong> Downloader A small personal tool that will allow you to download an icon pack on <a href="https://www.svgrepo.com/">SVGREPO</a> with the CLI.</p>

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![last_commit](https://img.shields.io/github/last-commit/AllanCerveaux/svg_repo_dl?style=flat-square)](https://github.com/AllanCerveaux/svg_repo_dl/commits/master)
[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/AllanCerveaux/svg_repo_dl/blob/master/LICENSE)
</div>

> Nota bene: this repository is based on its [original](https://github.com/AllanCerveaux/svg_repo_dl) but contains numerous bug fixes - including using `wget` instead of a headless Firefox browser for the actual download

___

## Requirement :

- Python 3
- Selenium
- Progress

## Installation
Follow this step:

Clone the repo
```bash
git clone git@github.com:AllanCerveaux/svg_repo_dl.git
```

Go in folder
```bash
cd svg_repo_dl
```

And run install.sh
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

## License
The MIT License (MIT) 2020 - Callan, Please have a look at the [License](https://github.com/AllanCerveaux/svg_repo_dl/blob/master/LICENSE) for more details.
