import os

def mk_loom(sp, config):

    cmd = 'velocyto run10x'
    cmd += ' -m ' + config['RNAvelocity']['make_loom']['rgtf']


    cmd += ' ' + config['workflow']  + '/' + sp + '_countResult'
    cmd += ' ' + config['RNAvelocity']['make_loom']['gtf']

    os.system(cmd)
