#!bin/bash
{
  velocyto --help

}&&{
  echo "successfully install velocyto"
}

{
  cellranger --help
  echo "successfully install cellranger"
}&&{
  echo "Fail to install cellranger"
}
python test_install_python.py
Rscript test_install_R.R