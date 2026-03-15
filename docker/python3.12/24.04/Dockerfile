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
        libgomp1 \
        libmpfr6 \
        locales \
        tcsh \
        tzdata \
        vim \
        wget \
        x11-apps && \
        x11-xserver-utils && \
        xvfb && \
    apt-get update && apt-get install -y \
        python3 python3-dev python3-venv python3-tk python3-pip python3-setuptools python-is-python3 z3 && \
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
