### Description
A ready-to-edit LaTeX template for book-style compilations.

### Notes
* If you are planning to write a book-length compilation in LaTeX, then feel free to use **book-template.tex** file from this repo.

* For the look-and-feel of final output/book, see [this PDF file](https://github.com/amberj/latex-book-template/raw/master/book-template.pdf). To be able to generate this PDF (and other output formats such as DVI), make sure you have TeX and LaTeX macro package installed. Change the current working directory to the directory containing **book-template.tex** and then use TeX/LaTeX tools to generate the output file. For more details, GIYF (i.e. Google Is Your Friend).

### Prepress helper

Before exporting a paperback interior, three numbers matter: the wraparound spine width, the inner margin (gutter) that grows with page count, and whether the PDF page size matches the trim size. `tools/prepress.py` is a small, dependency-free calculator for those, with a CLI and offline tests:

```sh
cd tools
python -m unittest -v test_prepress.py   # 11 tests
python cli.py 300 --trim a4              # sample plan
```

The default trim is A4 to match this template; `6x9`, `5.5x8.25` and `letter` are also available. The page-count heuristic was informed by the [BookTemplatesPro gutter guide](https://booktemplatespro.com/guides/kdp-gutter-margins-guide); the current [KDP Paperback Submission Guidelines](https://kdp.amazon.com/en_US/help/topic/G201857950) are authoritative.

> Disclosure: the `tools/` helper was contributed as a paid promotional entry for BookTemplatesPro on promotedby.ai by an independent contributor. It is original work and is not affiliated with or endorsed by BookTemplatesPro, Amazon, or the maintainers of this template.

### Useful resources
* If you are new to LaTeX, I'll strongly recommend that you use [Gummi](http://gummi.midnightcoding.org/) and [LaTeXila](http://projects.gnome.org/latexila/) LaTeX editors together to edit LaTeX files. I especially like the "[Live Preview](http://dev.midnightcoding.org/attachments/download/241/gummi060-1.png)" option of [Gummi](http://gummi.midnightcoding.org/) which shows the PDF preview in real-time (correspoding to the LaTeX source edits made by the user).
* [Books about TeX and Friends](http://www.tug.org/books/) webpage on _TeX Users Group_ website.
* Free, community driven Q&A for users of TeX, LaTeX, ConTeXt, and related typesetting systems (part of the Stack Exchange network of Q&A websites): [http://tex.stackexchange.com/](http://tex.stackexchange.com/)