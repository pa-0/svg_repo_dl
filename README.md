<div align="center">
	<img src=".github/README/Logo.svg" alt="logo"/>
	<p><strong>SVG_REPO Pack</strong> Downloader - a small personal tool that will allow you to download an icon pack from <a href="https://www.svgrepo.com/">SVG Repo</a> with the CLI.</p>

[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![last_commit](https://img.shields.io/github/last-commit/AllanCerveaux/svg_repo_dl?style=flat-square)](https://github.com/AllanCerveaux/svg_repo_dl/commits/master)
[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://github.com/AllanCerveaux/svg_repo_dl/blob/master/LICENSE)
</div>

> Nota bene: this repository is based on its [original](https://github.com/AllanCerveaux/svg_repo_dl) from Allan Cerveaux but contains numerous bug fixes - including using `wget` instead of a headless Firefox browser for the actual download

___

## Requirements ##

You may either install and run this downloader directly from your local environmanet or run it within a Docker container. Python programmers may prefer the first variant while all other may prefer the Docker solution.

To run the downloader from your local environment you will need

- Python 3
- Selenium
- Progress

otherwise you should install Docker first (which will remain useful in the future if you plan to experiment with other unknown software as well and still want to protect your PC)

## Installation on local Machine ##

(scroll down for the Docker-based solution)

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
## Usage from local Machine ##

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

## Usage from within Docker ##

Two steps are needed to run svgrepodl within a Docker container:

1. build a Docker image<br>`docker build -t svg_repo_dl .`
2. the run that image in order to download the desired icon collection<br>`docker run -rm -v <local-download-folder>:/transfer -e COLLECTION=<name-of-desired-collection> -t svg_repo_dl`

In the `docker run` command you should replace the following placeholders with actual values:

* `<local-download-folder>` - should be replaced with the actual path of the folder you want the icons downloaded into
* `<name-of-desired-collection>` - should be replaced with the name of the desired icon collection (e.g., `dazzle-line-icons`)

As described above, it may take several attempts until all icons of a given collection could be successfully downloaded. If the final download count is less than the expected number of icons, just repeat step 2 as often as you like.

In the end, you may remove the image from step 1 and free any resources it occupied.

## License ##

The MIT License (MIT) 2020 - Callan, Please have a look at the [License](https://github.com/AllanCerveaux/svg_repo_dl/blob/master/LICENSE) for more details.
