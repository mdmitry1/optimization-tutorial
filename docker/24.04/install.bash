#!/usr/bin/env bash
# Avoid interactive prompts during apt install
export DEBIAN_FRONTEND=noninteractive

# ---------------------------------------------------------------------------
# 1. System packages
# ---------------------------------------------------------------------------
apt-get update && apt-get install -y \
        g++ \
        gcc \
        git \
        glpk-utils \
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
        python3-pytest-mock \
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
        z3 

if [[ $? -ne 0 ]]; then
    echo -e "\nERROR: system packages installation failed\n"
fi    

# ---------------------------------------------------------------------------
# 2. python3.11 and python3.13
# ---------------------------------------------------------------------------

apt-get install -y --no-install-recommends \
        gnupg \
        curl \
        ca-certificates && \
        curl -fsSL "https://keyserver.ubuntu.com/pks/lookup?op=get&search=0xF23C5A6CF475977595C89F51BA6932366A755776" \
            | gpg --dearmor -o /etc/apt/trusted.gpg.d/deadsnakes.gpg && \
        echo "deb https://ppa.launchpadcontent.net/deadsnakes/ppa/ubuntu noble main" \
            > /etc/apt/sources.list.d/deadsnakes.list && \
    apt-get update && \
    apt-get install -y --no-install-recommends \
        python3.11 \
        python3.11-venv \
        python3.11-dev \
        python3.11-tk \
        python3.13 \
        python3.13-venv \
        python3.13-dev \
        python3.13-tk && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

if [[ $? -ne 0 ]]; then
    echo -e "\nERROR: python3.11 and/or python3.13 installation failed\n"
fi    

# ---------------------------------------------------------------------------
# 3. Conda 
# ---------------------------------------------------------------------------
wget --tries=5 --timeout=30 --waitretry=2 https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh && \
    bash ./Miniconda3-latest-Linux-x86_64.sh -b && \
    $HOME/miniconda3/bin/conda tos accept --override-channels --channel https://repo.anaconda.com/pkgs/main && \
    $HOME/miniconda3/bin/conda tos accept --override-channels --channel https://repo.anaconda.com/pkgs/r
    
if [[ $? -ne 0 ]]; then
    echo -e "\nERROR: conda installation failed\n"
fi    

# ---------------------------------------------------------------------------
# 4. Install scip and ipopt
# ---------------------------------------------------------------------------
$HOME/miniconda3/bin/conda install -y -c conda-forge ipopt scip && \
    ln -sf $HOME/miniconda3/bin/scip /usr/local/bin && \
    ln -sf $HOME/miniconda3/bin/ipopt /usr/local/bin && \
    rm ./Miniconda3-latest-Linux-x86_64.sh

if [[ $? -ne 0 ]]; then
    echo -e "\nERROR: SCIP and/or IPOPT installation failed\n"
fi    

# ---------------------------------------------------------------------------
# 5. Mathsat
# ---------------------------------------------------------------------------
current_dir=$PWD
wget --tries=5 --timeout=30 --waitretry=2 https://mathsat.fbk.eu/release/mathsat-5.6.15-linux-x86_64.tar.gz && \
    tar -xvf mathsat-5.6.15-linux-x86_64.tar.gz && \
    cd mathsat-5.6.15-linux-x86_64/python && \
    python setup.py build && \
    mkdir -p  /usr/local/lib/python3.12/dist-packages && \
    mv -f mathsat.py /usr/local/lib/python3.12/dist-packages && \
    mv -f build/lib.linux-x86_64-cpython-312/_mathsat.cpython-312-x86_64-linux-gnu.so /usr/local/lib/python3.12/dist-packages/_mathsat.so && \
    cd $current_dir && \
    rm -rf mathsat-5.6.15-linux-x86_64 && \
    tar -xvf mathsat-5.6.15-linux-x86_64.tar.gz && \
    cd mathsat-5.6.15-linux-x86_64/python && \
    python3.13 setup.py build && \
    mkdir -p  /usr/local/lib/python3.13/dist-packages && \
    mv -f mathsat.py /usr/local/lib/python3.13/dist-packages && \
    mv -f build/lib.linux-x86_64-cpython-313/_mathsat.cpython-313-x86_64-linux-gnu.so /usr/local/lib/python3.13/dist-packages/_mathsat.so && \
    cd $current_dir && \
    rm -rf mathsat-5.6.15-linux-x86_64 && \
    tar -xvf mathsat-5.6.15-linux-x86_64.tar.gz && \
    cd mathsat-5.6.15-linux-x86_64/python && \
    python3.11 setup.py build && \
    mkdir -p  /usr/local/lib/python3.11/dist-packages && \
    mv -f mathsat.py /usr/local/lib/python3.11/dist-packages && \
    mv -f build/lib.linux-x86_64-cpython-311/_mathsat.cpython-311-x86_64-linux-gnu.so /usr/local/lib/python3.11/dist-packages/_mathsat.so && \
    cd $current_dir && \
    rm -rf mathsat*

if [[ $? -ne 0 ]]; then
    echo -e "\nERROR: Mathsat installation failed\n"
fi    

# ---------------------------------------------------------------------------
# 6. Install UTF-8 fonts
# ---------------------------------------------------------------------------
locale-gen en_US.UTF-8

if [[ $? -ne 0 ]]; then
    echo -e "\nERROR: UTF-8 fonts installation failed\n"
fi    
