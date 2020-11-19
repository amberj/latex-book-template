## Description
A ready-to-edit LaTeX template for book-style compilations, particularly suitable for pdf print on demand.

### Installation

1. First, we need LaTeX itself

  - [Mac OSX](https://www.apple.com/macosx) via the [MacTeX Project](https://www.tug.org/mactex/)
  - [Windows](https://microsoft.com/windows) via the [MikTeX Project](https://miktex.org/download)
  - [Debian](http://www.debian.org/)/[Ubuntu](https://www.ubuntu.com/) Linux via apt:
  ```sh
sudo apt-get install texlive-full latex2rtf
```
  - [Downloads for other operating systems](http://latex-project.org/ftp.html)

2. Then, clone/download this repo

3. Optionally, [make](https://www.gnu.org/software/make/) which is included on most linux enviroments but also available for these operating systems too

  - [Mac OSX](https://www.apple.com/macosx) via [Homebrew](https://formulae.brew.sh/formula/make)
  - [Windows](https://microsoft.com/windows) via [Chocolatey](https://chocolatey.org/packages/make)

### Usage

Copy and edit the [book-template.tex](book-template.tex) and [book-template-cover.tex](book-template.tex) (optional) files to your liking, and use the [Makefile](Makefile) for convenience.

For a book cover, use either the [book-template-cover.tex](book-template-cover.tex) template, or uncomment the full-page image inclusion commands in the main template.

The main template uses a modular, extensible format: the convention is to place the individual chapters in a related folder (e.g., [book-template](book-template)) and use the [\subimport{book-template/}{file.tex}](https://ctan.org/pkg/import) command to include them, though that is optional.

It is possible to keep all the content in the main template file itself instead.

### Creating pdf files

If you use the [Makefile](Makefile), this command compiles all the <tt>.tex</tt> files to [pdf](http://en.wikipedia.org/wiki/Portable_Document_Format) format:

```sh
make all
```

LaTeX creates several log and auxiliary files which are usually not needed once the pdf is created. These can be cleared with this command:

```sh
make tidy
```

To start over, just wipe the compiled file with this:

```sh
make clean
```

## Notes

* For the look-and-feel of final output, see [this PDF file](book-template.pdf)
* The wrap-around cover and spine is in [this PDF file](book-template-cover.pdf)

## Useful resources
* If you are new to LaTeX, I'll strongly recommend that you use [Gummi](http://gummi.midnightcoding.org/) and [LaTeXila](http://projects.gnome.org/latexila/) LaTeX editors together to edit LaTeX files. I especially like the "[Live Preview](http://dev.midnightcoding.org/attachments/download/241/gummi060-1.png)" option of [Gummi](http://gummi.midnightcoding.org/) which shows the PDF preview in real-time (correspoding to the LaTeX source edits made by the user).
* Documentation on how to use LaTeX can be found both [here](http://latex-project.org/guides/) and [here](https://en.wikibooks.org/wiki/LaTeX).
* [Books about TeX and Friends](http://www.tug.org/books/) webpage on _TeX Users Group_ website.
* Free, community driven Q&A for users of TeX, LaTeX, ConTeXt, and related typesetting systems (part of the Stack Exchange network of Q&A websites): [http://tex.stackexchange.com/](http://tex.stackexchange.com/)
