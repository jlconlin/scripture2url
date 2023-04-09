#!/usr/bin/env python

import re
import argparse

books = {
    # Old Testament
    'Genesis'         : 'ot/gen',
    'Exodus'          : 'ot/ex',
    'Leviticus'       : 'ot/lev',
    'Numbers'         : 'ot/num',
    'Deuteronomy'     : 'ot/deut',
    'Joshua'          : 'ot/josh',
    'Judges'          : 'ot/judg',
    'Ruth'            : 'ot/ruth',
    '1 Samuel'        : 'ot/1-sam',
    '2 Samuel'        : 'ot/2-sam',
    '1 Kings'         : 'ot/1-kgs',
    '2 Kings'         : 'ot/2-kgs',
    '1 Chronicles'    : 'ot/1-chr',
    '2 Chronicles'    : 'ot/2-chr',
    'Ezra'            : 'ot/ezra',
    'Nehemiah'        : 'ot/neh',
    'Esther'          : 'ot/esth',
    'Job'             : 'ot/job',
    'Psalms'          : 'ot/ps',
    'Proverbs'        : 'ot/prov',
    'Ecclesiastes'    : 'ot/eccl',
    'Song of Solomon' : 'ot/song',
    'Isaiah'          : 'ot/isa',
    'Jeremiah'        : 'ot/jer',
    'Lamentations'    : 'ot/lam',
    'Ezekiel'         : 'ot/ezek',
    'Daniel'          : 'ot/dan',
    'Hosea'           : 'ot/hosea',
    'Joel'            : 'ot/joel',
    'Amos'            : 'ot/amos',
    'Obadiah'         : 'ot/obad',
    'Jonah'           : 'ot/jonah',
    'Micah'           : 'ot/micah',
    'Nahum'           : 'ot/nahum',
    'Habakkuk'        : 'ot/hab',
    'Zephaniah'       : 'ot/zeph',
    'Haggai'          : 'ot/Haggai',
    'Zechariah'       : 'ot/zech',
    'Malachi'         : 'ot/mal',
    # New Testament
    'Matthew'         : 'nt/matt',
    'Mark'            : 'nt/mark',
    'Luke'            : 'nt/luke',
    'John'            : 'nt/john',
    'Acts'            : 'nt/acts',
    'Romans'          : 'nt/rom',
    '1 Corinthians'   : 'nt/1-cor',
    '2 Corinthians'   : 'nt/2-cor',
    'Galatians'       : 'nt/gal',
    'Ephesians'       : 'nt/eph',
    'Philippians'     : 'nt/philip',
    'Colossians'      : 'nt/col',
    '1 Thessalonians' : 'nt/1-thes',
    '2 Thessalonians' : 'nt/2-thes',
    '1 Timothy'       : 'nt/1-tim',
    '2 Timothy'       : 'nt/2-tim',
    'Titus'           : 'nt/titus',
    'Philemon'        : 'nt/philem',
    'Hebrews'         : 'nt/heb',
    'James'           : 'nt/james',
    '1 Peter'         : 'nt/1-pet',
    '2 Peter'         : 'nt/2-pet',
    '1 John'          : 'nt/1-jn',
    '2 John'          : 'nt/2-jn',
    '3 John'          : 'nt/3-jn',
    'Jude'            : 'nt/jude',
    'Revelation'      : 'nt/rev',
    # Book of Mormon
    '1 Nephi'         : 'bofm/1-ne',
    '2 Nephi'         : 'bofm/2-ne',
    'Jacob'           : 'bofm/jacob',
    'Enos'            : 'bofm/enos',
    'Jarom'           : 'bofm/jarom',
    'Omni'            : 'bofm/omni',
    'Words of Mormon' : 'bofm/w-of-m',
    'Mosiah'          : 'bofm/mosiah',
    'Alma'            : 'bofm/alma',
    'Helaman'         : 'bofm/hel',
    '3 Nephi'         : 'bofm/3-ne',
    '4 Nephi'         : 'bofm/4-ne',
    'Mormon'          : 'bofm/morm',
    'Ether'           : 'bofm/ether',
    'Moroni'          : 'bofm/moro',
    # Doctrine and Covenants
    'D&C' : 'dc-testament/dc',
    # Pearl of Great Price
    'Moses'                : 'pgp/moses',
    'Abraham'              : 'pgp/abr',
    'Joseph Smith-History' : 'pgp/js-h',
    'Joseph Smith–History' : 'pgp/js-h',
    'Joseph Smith-Matthew' : 'pgp/js-m',
    'Joseph Smith–Matthew' : 'pgp/js-h',
}

regex=re.compile("""
    (?P<book>([1-4] )?[A-Za-z- ]+)\s+
    (?P<chapter>[0-9]+):
    (?P<verse>[0-9]*)
    (-(?P<other>[0-9]+))?
    """, re.VERBOSE)

def ref2url(scripture, language):
    """
    """
    found = regex.search(scripture)
    if found:
        d = found.groupdict()
        book = books.get(d['book'])
        url="https://www.churchofjesuschrist.org/study/scriptures/{Book:}/{chapter:}?lang={lang:}&id=p{verse:}".format(lang=language, Book=book, **d)

        if d['other']:
            url += "-p{}".format(d['other'])
        return url
    else:
        print("Scripture reference not found in: '{}'".format(scripture))

def convert(reference, url, form):
    """
    Convert the reference to a particular format. Available formats are:

        markdown
        html
    """
    forms = {
        'markdown': '[{ref:}]({url:})',
        'html': '<a href="{url:}">{ref:}</a>'
    }

    return forms.get(form).format(ref=reference, url=url)


if __name__ == "__main__":
    description = """
        Convert scripture reference to URL link to
        \thttps://www.churchofjesuschrist.org/study/scriptures
    """
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('reference', type=str,
        help='Scripture reference. Note the reference must be in quotes')
    parser.add_argument('-l', '--language', type=str,
                        default="eng",
                        help='3-letter language option for URL query')
    parser.add_argument('--form', choices=['markdown', 'md', 'html', 'plain'],
                        default="markdown",
                        help="What form should the link be given.")
    parser.add_argument('--dont-copy', default=False, action='store_true',
                        help="Don't copy output to clipboard")
    args = parser.parse_args()

    url = ref2url(args.reference, args.language)

    if args.form != "plain":
        url = convert(args.reference, url, args.form)

    if not args.dont_copy:
        try:
            import pyperclip
            pyperclip.copy(url)
        except ImportError as e:
            print("Can't copy to clipboard.\n"
                  "Please install pyperclip Python package.")
    else:
        print(url)
