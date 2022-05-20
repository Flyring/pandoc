from panflute import *
from sys import stderr

headers = []

def makeBold(doc):
    doc.replace_keyword("BOLD", Strong(Str("BOLD")))


def upper_header(elem, doc):
    if type(elem) == Header and elem.level > 2:
        return Header(Str(stringify(elem).upper()), level=elem.level)


def duplicate_headers(elem, doc):
    if type(elem) == Header:
        text = stringify(elem)
        if text in headers:
            print("Одинаковые заголовки", file=stderr)
        else:
            headers.append(text)

if __name__ == "__main__":
    run_filters([upper_header, duplicate_headers], prepare=makeBold)
