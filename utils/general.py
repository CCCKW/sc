import scanpy as sc
import sys
import os



def Plot(con, config):
    workflow = config['workflow']
    HVGdir = workflow + '/HVG'
    path_adata = HVGdir + '/before_leiden.h5ad'
    if not os.path.exists(HVGdir) or not os.path.exists(path_adata):
        sys.exit('Not find the h5ad file in the HVG')


    adata = sc.read_h5ad(path_adata)

    gene_list = con.gene_list
    if con.plot_leiden:
        gene_list = ['leiden'] + gene_list

    outdir = workflow + '/plot_gene'
    if not os.path.exists(outdir):
        os.makedirs(outdir)

    os.chdir(outdir)

    sc.pl.umap(adata, color=gene_list, save=True)

def chech_loom(sample, config):
    ldata_list = []
    for root, dirs, files in os.walk(config['workflow']):
        for val in files:
            if val.endswith('loom'):
                ldata_list.append(root + '/' + val)
    if len(ldata_list) == len(sample):
        print('=========loom files have been made============')
        return True
    return False


def remake_barcode_from_adata(adata):
    wbarcode = list(adata.obs.index)
    barcode = [x.split('-')[0] for x in wbarcode]
    adata.obs.index = barcode
    adata.var_names_make_unique()
    adata.obs_names_make_unique()
    return adata


def remake_barcode_from_ldata(ldata):
    wbarcode = list(ldata.obs.index)
    barcode = [x.split(':')[0] for x in wbarcode]
    ldata.obs.index = barcode
    ldata.var_names_make_unique()
    ldata.obs_names_make_unique()
    return ldata