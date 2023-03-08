import os
import scanpy as sc

import re
import anndata as ad

def count_sin(sample, config):
    threads = config['threads']
    print('===============cellranger count===============')
    os.chdir(config['workflow'])
    # if not os.path.exists(config['workflow'] + '/' + sample):
    #     os.makedirs(config['workflow'] + '/' + sample)
    #     # os.chdir(config['workflow'] + '/' + sample)
    outFolder =   sample + '_countResult'
    cmd = 'cellranger'
    cmd += ' count '
    cmd += '--id=' + outFolder
    cmd += ' --sample=' + sample

    cmd += ' --transcriptome=' + config['refdata']
    if ' ' in config['data']:
        path_to_data = config['data'].replace(' ', '\ ')
        cmd += ' --fastqs=' + path_to_data
    else:
        cmd += ' --fastqs=' + config['data']
    cmd += ' --localcores=8'
    print(cmd)
    try:
        print('run cmd')
        os.system(cmd)
    except:
        print('the path you gave of cellranger is ', 'cellranger', 'its right?')
        print('check the cmd, whether the args you gave were wrong')
        
def aggr(samples, config):
    print('==============scanpy aggr==================')
    aggrFolder = config['workflow'] + '/' + 'total_aggr/'
    if not os.path.exists(aggrFolder):
        os.makedirs(aggrFolder)
    os.chdir(config['workflow'])
    adatalist = []
    for sm in samples: #[p b s]
        # print(sm)
        mtxPath = config['workflow'] + '/'  + sm + '_countResult/outs/filtered_feature_bc_matrix/'
        adata = sc.read_10x_mtx(mtxPath,  var_names='gene_symbols', cache=True)
        adata.var_names_make_unique()
        adata.obs_names_make_unique()
        # print(sm)
        adata.obs['sample'] = sm
        # print(adata.obs['sample'] )
        adatalist.append(adata)

    adata_aggr = ad.concat(adatalist,merge='same')



    # if config['QC']['batch_effect']:
    #     sc.external.pp.harmony_integrate(adata_aggr, 'sample')
    adata_aggr.write(aggrFolder + 'aggr.h5ad')
    
def mtx(config):
    root = config['data']

    # 整合所有样本的矩阵
    #这里样本的前缀
    prefix = []
    for val in os.listdir(root):
        print(val)
        if val.endswith('.gz'):
            tmp = re.split('matrix|features|barcodes|genes', val)
            print(tmp)
            if not tmp[0] in prefix:
                prefix.append(tmp[0])
    print(prefix)
    adata_list = []
    for fix in prefix:

        adata  = sc.read_10x_mtx(root, var_names='gene_symbols',
                                          prefix=fix,
                                          cache=True)
        adata.var_names_make_unique()
        adata.obs_names_make_unique()
        adata.obs['sample'] = fix
        adata_list.append(adata)
    print(adata_list)
    if len(adata_list) == 1:
        adata_aggr = adata
    else:
        adata_aggr =  ad.concat(adata_list,merge='same')

    os.chdir(config['workflow'])
    mtxFile = './MTX_aggr/'

    if not os.path.exists(mtxFile):
        os.makedirs(mtxFile)
    # if config['QC']['batch_effect'] and len(prefix) > 1:
    #     sc.external.pp.harmony_integrate(adata_aggr, 'sample')
    adata_aggr.write(mtxFile + 'res.h5ad')
    return prefix

def h5ad(config):
    root = config['data']

    # 整合所有样本的矩阵
    # 这里样本的前缀
    prefix = []
    for val in os.listdir(root):
        print(val)
        if val.endswith('h5ad'):
            tmp = val.split('.')

            if not tmp[0] in prefix:
                prefix.append(tmp[0])
    print(prefix)
    adata_list = []
    for fix in prefix:
        adata = sc.read_h5ad(root + '/' + fix+'.h5ad')
        adata.var_names_make_unique()
        adata.obs_names_make_unique()
        adata_list.append(adata)
    print(adata_list)
    if len(adata_list) == 1:
        adata_aggr = adata
    else:
        adata_aggr = ad.concat(adata_list, merge='same')

    os.chdir(config['workflow'])
    h5adFile = './h5ad_aggr/'

    if not os.path.exists(h5adFile):
        os.makedirs(h5adFile)
    # if config['QC']['batch_effect'] and len(prefix) > 1:
    #     sc.external.pp.harmony_integrate(adata_aggr, 'sample')
    adata_aggr.write(h5adFile + 'res.h5ad')
    return prefix