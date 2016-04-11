import string

def translator(frm='', to='', delete='', keep=None):

    if len(to) == 1:
        to = to*len(frm)
    trans = string.maketrans(frm, to)
    if keep is not None:
        allcharts = string.maketrans('', '')
        delete = allcharts.translate(allcharts, keep.translate(allcharts, delete))
    def translate(s):
        return s.translate(trans, delete)
    return translate
