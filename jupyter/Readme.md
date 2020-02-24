# Jupyter Notebook

Verschiedene Module an der HSLU setzen auf [Jupyter Notebooks](https://jupyter.org), stets unter Verwendung spezifischer Python-Pakete.

## Umfang

Zur Vereinfachung der Inbetriebnahme wurde ein Docker-Image erstellt, welches die folgenden Pakete beinhaltet:

- jupyter_contrib_nbextensions
- matplotlib 
- mlxtend 
- networkx
- nltk 
- numpy 
- opencv-contrib-python
- ortools
- pandas 
- pandas-profiling 
- plotly 
- scikit-image 
- scikit-learn 
- scipy 
- seaborn 
- tqdm

Damit sollten die Anforderungen an die folgenden Module abgedeckt sein:

- AISO (Artificial Intelligence and Search Optimization)
- IPCV (Image Processing and Computer Vision)
- ML (Machine Learning)

## Ausführen

Das erstellte Image kann wie folgt heruntergeladen werden:

```sh
docker pull docker.pkg.github.com/unexpected-yeti/class-notes/jupyter-hslu:1.0.1
```
> Es wird ein persönliches Token benötigt, um auf Githubs Docker-Registry zuzugreifen. 
Für Details [siehe hier.](https://help.github.com/en/packages/using-github-packages-with-your-projects-ecosystem/configuring-docker-for-use-with-github-packages)

Der gewünschte Pfad mit den `ipynb`-Dateien kann als Docker Volume in den Container gemounted werden.

### Linux

Mit separat erstelltem Docker Volume:

```sh
sudo docker volume create --name {volume-name} --opt type=none --opt o=bind --opt device=/path/to/your/folder

sudo docker run -it -p 8888:8888 --mount source={volume-name},target=/home/jovyan -e JUPYTER_RUNTIME_DIR=/tmp/runtime docker.pkg.github.com/unexpected-yeti/class-notes/jupyter-hslu:1.0.1
```

> Falls mit WSL2 gearbeitet wird gilt zu beachten, dass WSL2 eine eigene IP-Adresse zugewiesen bekommt. Somit können die Windows-Applikationen nicht per `localhost` auf die Jupyter-Instanz zugreifen.

### Windows

```ps1
docker run -it -p 8888:8888 -v C:\path\to\your\folder:/home/jovyan -e JUPYTER_RUNTIME_DIR=/tmp/runtime docker.pkg.github.com/unexpected-yeti/class-notes/jupyter-hslu:1.0.1
```
