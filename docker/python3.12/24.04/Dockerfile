FROM ubuntu:24.04

# Avoid interactive prompts during apt install
ENV DEBIAN_FRONTEND=noninteractive

# ---------------------------------------------------------------------------
# 1. System packages
# ---------------------------------------------------------------------------
RUN apt-get update && apt-get install -y \
        g++ \
        gcc \
        git \
        jq \
        libgfortran5 \
        libgmp-dev \
        libgomp1 \
        libmpfr6 \
        locales \
        python3 \
        python-is-python3 \
        python3-dev \
        python3-pip \
        python3-pyqt5 \
        python3-pytest \
        python3-setuptools \
        python3-tk \
        python3-venv \
        python3-z3 \
        tcsh \
        tzdata \
        vim \
        wget \
        x11-apps \
        x11-xserver-utils \
        xvfb \
        z3 && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# ---------------------------------------------------------------------------
# 2. Conda 
# ---------------------------------------------------------------------------
WORKDIR /app
RUN wget --tries=5 --timeout=30 --waitretry=2 https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh && \
    bash ./Miniconda3-latest-Linux-x86_64.sh -b && \
    /root/miniconda3/bin/conda tos accept --override-channels --channel https://repo.anaconda.com/pkgs/main && \
    /root/miniconda3/bin/conda tos accept --override-channels --channel https://repo.anaconda.com/pkgs/r
    
# ---------------------------------------------------------------------------
# 2. Install scip and ipopt
# ---------------------------------------------------------------------------
RUN /root/miniconda3/bin/conda install -y -c conda-forge ipopt scip && \
    ln -sf /root/miniconda3/bin/scip /usr/local/bin && \
    ln -sf /root/miniconda3/bin/ipopt /usr/local/bin && \
    rm ./Miniconda3-latest-Linux-x86_64.sh

# ---------------------------------------------------------------------------
# 3. Mathsat
# ---------------------------------------------------------------------------
RUN wget --tries=5 --timeout=30 --waitretry=2 https://mathsat.fbk.eu/release/mathsat-5.6.15-linux-x86_64.tar.gz && \
    tar -xvf mathsat-5.6.15-linux-x86_64.tar.gz && \
    cd mathsat-5.6.15-linux-x86_64/python && \
    python setup.py build && \
    mkdir -p  /usr/local/lib/python3.12/dist-packages/mathsat && \
    mv -f mathsat.py /usr/local/lib/python3.12/dist-packages && \
    mv -f build/lib.linux-x86_64-cpython-312/_mathsat.cpython-312-x86_64-linux-gnu.so /usr/local/lib/python3.12/dist-packages/mathsat/_mathsat.so && \
    rm mathsat-5.6.15-linux-x86_64.tar.gz 

# ---------------------------------------------------------------------------
# 3. Install UTF-8 fonts
# ---------------------------------------------------------------------------
RUN locale-gen en_US.UTF-8
ENV LANG=en_US.UTF-8
ENV LANGUAGE=en_US:en
ENV LC_ALL=en_US.UTF-8

# --------------------------------------------------------------------------
# 4. Clone repository
# --------------------------------------------------------------------------
RUN git clone https://git@github.com/mdmitry1/optimization-tutorial 

# Default command
WORKDIR /app/optimization-tutorial
CMD ["/usr/bin/tcsh"]
