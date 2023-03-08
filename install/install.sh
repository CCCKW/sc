# !bin/bash
# install python package
conda config --add channels conda-forge
echo "********************install annoy********************"
yes|conda install -c conda-forge python-annoy
echo "********************install bbknn********************"
pip install bbknn
echo "********************install samtools********************"
yes|conda install -c bioconda samtools
echo "********************install pysam********************"
pip install pysam
echo "********************install cpython********************"
pip install cython
echo "********************install numba********************"
pip install numba
echo "********************install h5py********************"
pip install h5py
echo "********************install click********************"
pip install click
echo "********************install velocyto********************"
pip install velocyto
echo "********************install scvelo********************"
pip install scvelo
echo "********************install scanpy********************"
pip install scanpy==1.9.1
echo "********************install leidenalg********************"
yes|conda install -c conda-forge leidenalg
echo "********************install fa2********************"
yes|conda install -c conda-forge fa2
echo "********************install pyyaml********************"
pip install pyyaml
echo "********************install gseapy********************"
yes|conda install -c bioconda gseapy
echo "********************install anndata********************"
pip install anndata
echo "********************install diopy********************"
pip install diopy





echo "********************install r-base********************"
yes|conda install -c conda-forge r-base==4.1.3
## install R package
echo "********************install R package********************"
echo "********************install biocmanger********************"
yes|conda install -c conda-forge r-biocmanager
echo "********************install devtools********************"
yes|conda install -c conda-forge r-devtools
echo "********************install r-seurat********************"
yes|conda install -c conda-forge r-seurat
#
echo "********************install r-anndata********************"
yes|conda install -c bioconda r-anndata
echo "********************install r-ggrastr********************"
yes|conda install -c conda-forge r-ggrastr
echo "********************install loomr********************"
yes|conda install -c bioconda r-loomr
echo "********************install cowplot********************"
yes|conda install -c conda-forge r-cowplot

yes|conda install -c bioconda bioconductor-genomicranges

yes|conda install -c bioconda bioconductor-scater
yes|conda install -c bioconda bioconductor-monocle
#yes|conda install -c bioconda bioconductor-rbgl
#yes|conda install -c conda-forge libxml2
#yes|conda install -c bioconda bioconductor-biocviews
#yes|conda install -c conda-forge r-viridis



#
## 以上都是可以的，下面是新加的模块
#echo "********************install pyscenic********************"
#pip install pyscenic
#echo "********************install adjustText********************"
#pip install adjustText
#yes|conda install -c powerai multicoretsne
#pip install -U cellphonedb
pip install matplotlib==3.5.0

yes|conda install -c conda-forge r-nloptr
yes|conda install -c conda-forge r-lme4
yes|conda install -c conda-forge r-rstatix
yes|conda install -c conda-forge r-ggpubr
Rscript install_ccc.R
pip install harmonypy
pip install dask
pip install arboreto
pip install ctxcore
pip install attr
pip install pyscenic
pip install chord
pip install adjustText

Rscript install.R

python test_install_python.py
Rscript test_install_R.R


# conda install -c conda-forge r-ggrastr


