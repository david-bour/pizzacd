import sys
import io
import urllib
from urllib.request import Request
from flask import Blueprint, jsonify, g
from guppy import hpy

bp = Blueprint('memory', __name__, url_prefix='/memory')

@bp.route('/<sizemb>', methods=['GET'])
def size(sizemb):
    size = int(sizemb)
    # char = 1 byte
    # 1024 bytes = 1 kb
    # 1024 kb = 1 mb
    total_size =  1024 * 1024 * size
    var = 'a' * total_size
    output = io.StringIO()
    output.write(var)
    contents = output.getvalue()
    return jsonify(dict(size=sys.getsizeof(var)))


@bp.route('/file', methods=['GET'])
@bp.route('/file/<index>', methods=['GET'])
def openfile(index=None):

    # hp = hpy()
    # before = hp.heap()

    pdfs = [
        'https://jeffe.cs.illinois.edu/teaching/algorithms/book/Algorithms-JeffE.pdf',
        'http://1.droppdf.com/files/87BCs/the-linux-programming-interface.pdf',
        'https://edutechlearners.com/download/Introduction_to_algorithms-3rd%20Edition.pdf',
        'http://algorithmics.lsi.upc.edu/docs/Dasgupta-Papadimitriou-Vazirani.pdf',
        'https://www.cs.sjtu.edu.cn/~jiangli/teaching/CS222/files/materials/Algorithm%20Design.pdf',
        'https://people.cs.clemson.edu/~jmarty/courses/kurose/KuroseCh1-2.pdf',
    ]

    if index:
        index = int(index)
        pdf = pdfs[index]
        url = Request(pdf, headers={'User-Agent': 'Mozilla/5.0'})
        data = urllib.request.urlopen(url).read()
        with open(f'experiment-{index}.pdf', 'wb') as fi:
            fi.write(data)
    else:
        junk = []
        for fi in pdfs:
            url = Request(fi, headers={'User-Agent': 'Mozilla/5.0'})
            data = urllib.request.urlopen(url).read()
            with open(f'experiment-{index}.pdf', 'wb') as fi:
                junk.append(data)
                fi.write(data)

    # after = hp.heap()
    # leftover = after - before
    # print(leftover)

    return jsonify(dict(data='done'))
