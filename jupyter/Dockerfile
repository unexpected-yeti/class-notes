# Three courses (AISO, IPCV, ML) and one dockerfile to rule them all.
# Attention: The image generated will be big.
FROM jupyter/base-notebook

# AISO (and part of ML)
RUN conda install --quiet --yes --channel https://conda.anaconda.org/conda-forge numpy pandas scikit-learn matplotlib tqdm networkx && conda clean -tipsy
RUN python -m pip install ortools

# ML specific
RUN python -m pip install pandas-profiling seaborn mlxtend nltk scikit-image tqdm plotly scipy jupyter_contrib_nbextensions
RUN jupyter contrib nbextension install --user

# IPCV specific
RUN python -m pip install opencv-contrib-python

USER root
RUN apt update
RUN apt install -y libsm-dev libsm6
RUN apt install -y apt-utils
RUN apt install -y libxrender-dev
RUN apt-get update
RUN apt-get install -y libxext-dev
USER jovyan