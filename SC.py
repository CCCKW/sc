# -*- coding: utf-8 -*
import os
import scanpy as sc
import argparse
import yaml
import time
import  warnings
from functools import reduce
import re
from utils.FindMarker import HVG
from utils.QualityControl import QC
from utils.GSEA import GSEA
from utils.Trajectory import Trajectory
from utils.velocity import velocity
from utils.makeLoom import mk_loom
from utils.cellrangerTools import aggr, mtx, count_sin, h5ad
from utils.GRN import GRN
from utils.makeReport import MoveFig, CreateReportDir
from utils.makeJson import  makeJson
from utils.CCC import CCC
from utils.general import Plot, chech_loom
import os


import threading
import time
sc.settings.verbosity = 2
sc.settings.set_figure_params(dpi_save=400, facecolor='white', fontsize=7, format='jpg')
# 调用软件的绝对路径
warnings.filterwarnings("ignore")
config = yaml.load(open('./config.yaml', 'r'), Loader=yaml.FullLoader)


def Run_count(args, config):
    pass

def Plot_pipe(con):
    config = yaml.load(open('./config.yaml', 'r'), Loader=yaml.FullLoader)

    Plot(con, config)


def Run_pipeline_basic(con):
    config = yaml.load(open('./config.yaml', 'r'), Loader=yaml.FullLoader)
    config['threads'] = con.threads
    config['pipelineDir'] = os.getcwd()
    print(os.getcwd())
    config = CreateReportDir(config)
    print(config['reportDir'])

    print('==========Running Pipeline==========')

    type_ = con.dataType
    flag = 1
    threads = con.threads

    if con.start == 'count':
        flag = 1
    elif con.start == 'aggr':
        flag = 2
    elif con.start == 'velo':
        flag = 3

    if not os.path.exists(config['workflow']):
        os.makedirs(config['workflow'])
    os.chdir(config["workflow"])
    samples = []

    if type_ == 'fastq':
        for file in os.listdir(config['data']):
            if file.endswith('fastq.gz') or file.endswith('fastq'):
                file = file.split('_')
                file = file[:-4]
                s = reduce(lambda x, y: x + '_' +y, file)
                # print(s)
                if s not in samples:
                    samples.append(s)
    elif type_ == 'mtx':
        root = config['data']

        # 整合所有样本的矩阵
        # 这里样本的前缀
        samples = []
        for val in os.listdir(root):
            if val.endswith('.gz'):
                tmp = re.split('matrix|features|barcodes', val)
                if not tmp[0] in samples:
                    samples.append(tmp[0])

    elif type_ == 'h5ad':
        root = config['data']

        # aggr all h5ad
        # prefix of the sampe
        samples = []
        for val in os.listdir(root):
            if val.endswith('.h5ad'):
                tmp = val.split('.')[0]
                if not tmp in samples:
                    samples.append(tmp)

    print(samples)

    # count 多线程处理，如果是mtx则不会运行w
    if flag <= 2:
        if type_ == 'fastq':
            if flag <=1:
                if config['multi_process']:
                    from multiprocessing import Process, Pool
                    print('avaliable cpu: ', os.cpu_count())
                    if len(samples) > 1:
                        print('============We will use cellranger aggr==============')

                    if len(samples) <= threads:
                        p = Pool(len(samples))
                        for sp in samples:
                            p.apply_async(count_sin, args=(sp, config,))
                        p.close()
                        p.join()
                    else:
                        divide_list = []
                        for i in range(0, len(samples), threads):
                            divide_list.append(samples[i:i + threads])
                        for val in divide_list:
                            p = Pool(len(val))
                            for sp in val:
                                p.apply_async(count_sin, args=(sp, config,))
                            p.close()
                            p.join()

                else:
                    if len(samples) > 1:
                        print('============We will use cellranger aggr==============')
                    for sp in samples:
                        count_sin(sp, config)
                        # pass

            if len(samples) > 1:
                aggr(samples, config)
            MoveFig(config=config, step='webSummary')

        elif type_ == 'mtx':
            mtx(config)
        elif type_ == 'h5ad':
            h5ad(config)


    # mkloom
    if flag <= 3 and config['RNAvelocity']['done']:
        if not chech_loom(samples, config):
            if config['multi_process']:
                from multiprocessing import Process, Pool
                print('============make loom==============')
                if len(samples) <= threads:
                    p = Pool(len(samples))
                    for sp in samples:
                        p.apply_async(mk_loom, args=(sp,config,))
                    p.close()
                    p.join()
                else:
                    divide_list = []
                    for i in range(0, len(samples), threads):
                        divide_list.append(samples[i:i+threads])
                    for val in divide_list:
                        p = Pool(len(val))
                        for sp in val:
                            p.apply_async(mk_loom, args=(sp, config,))
                        p.close()
                        p.join()

            else:
                print('============make loom==============')
                for sp in samples:
                    mk_loom(sp, config)

        config = velocity(samples, config, len(samples))
        MoveFig(config=config, step='velo')



def main():
    parser = argparse.ArgumentParser()

    subparsers1 = parser.add_subparsers()


    pipeline_basic = subparsers1.add_parser('run', help='run the pipeline')
    pipeline_basic.add_argument('--dataType',choices=['fastq', 'mtx', 'h5ad'], default='fastq')
    pipeline_basic.add_argument('--start', choices=['count', 'aggr','velo'],default='count', help='count, aggr,velo')
    pipeline_basic.add_argument('--threads', type=int, default=2)
    pipeline_basic.set_defaults(func='Run')

    args = parser.parse_args()


    try:
        args.func(args)
    except:
        pass


    if args.func == 'Run':
        Run_pipeline_basic(args)
    else:
        print('wrong command')
if __name__ == '__main__':
    Time = time.time()

    main()
    print('=============time spen ', time.time() - Time, '===================')



