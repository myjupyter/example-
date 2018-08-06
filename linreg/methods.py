from datetime import datetime 
from pandas import read_csv, DataFrame
from seaborn import regplot, jointplot
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.pyplot as mpt
import patsy as pt
import numpy as np
import os 
from fpdf import FPDF

def handle_uploaded_file(data):
    save_path = '/tmp/' + datetime.now().strftime('%d%m%y %H:%M:%S') + '.csv'
    
    with open(save_path, 'wb+') as dest:
        for chunk in data.chunks():
            dest.write(chunk)
    return save_path
'''
def ploting(save_path):
    table = read_csv(save_path, delimiter = ',')
    way = save_path.split('.')[0]
    os.mkdir(way)
    index = table.columns
    for i in range(0,table.shape[1] - 1):
        g = regplot(x = index[i], y = index[-1],  data = table[[index[i], index[-1]]] )
        mpt.savefig(way + '/' + way.split('/')[-1] + index[i] + '.jpg')

    pdf = FPDF()
    for image in os.listdir(way):
        pdf.add_page()
        pdf.image(way + '/' + image, w = 200, h = 200)
    pdf.output( way + '/result.pdf', 'F')

    return way + '/result.pdf'

'''
def ploting(save_path):
    table = read_csv(save_path, delimiter = ',')
    way = save_path.split('.')[0] + '.pdf'
    pp = PdfPages(way)
    index = table.columns
    for i in range(0,table.shape[1] - 1):
        regplot(x = index[i], y = index[-1], data = table[[index[i], index[-1]]])
        pp.savefig()
    pp.close()

    return way





def eqs(t):
    st = 'y ~ ' + ' + '.join([ e for e in table.columns if e[0] == 'x'])
    print(st)
    pt_y, pt_x = pt.dmatrices(st, t)
    res = np.linalg.lstsq(pt_x, pt_y)
    print(res[0].ravel())






