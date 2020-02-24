# Three courses (AISO, IPCV, ML) and one dockerfile to rule them all.
# Attention: The image generated will be big.
FROM jupyter/base-notebook
USER jovyan

# AISO (and part of ML)
RUN conda install --quiet --yes --channel https://conda.anaconda.org/conda-forge numpy pandas scikit-learn matplotlib tqdm networkx && conda clean -tipsy
RUN python -m pip install ortools

# ML specific
RUN python -m pip install pandas-profiling seaborn mlxtend nltk scikit-image tqdm plotly scipy jupyter_contrib_nbextensions
RUN jupyter contrib nbextension install --user

# IPCV specific
RUN python -m pip install opencv-contrib-python