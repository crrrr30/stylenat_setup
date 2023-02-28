# Environment Setup for StyleNAT

This assumes running under a `pytorch/pytorch:latest` Docker image.

First, initialize the `conda` command by running `conda init`.

Since `conda` comes preinstalled, we can create the environment right away.

```
conda create --name nat python=3.10 -y
```

We now activate the environment and install PyTorch.

```
conda activate nat
conda install pytorch=1.13.1 torchvision cudatoolkit=11.6 -c pytorch -c nvidia -y
```

Do **NOT** install from `requirements.txt`. The following versions have been tested.

```
wget https://shi-labs.com/natten/wheels/cu116/torch1.13/natten-0.14.4%2Btorch1130cu116-cp310-cp310-linux_x86_64.whl
pip install natten-0.14.4+torch1130cu116-cp310-cp310-linux_x86_64.whl
conda install -c conda-forge gxx=10.4.0 -y
conda install ipython
pip install -q lmdb==1.4.0
pip install -q timm==0.6.12
pip install -q scipy==1.9.3
conda install -c anaconda scikit-learn=1.2.0 -y
pip install -q einops==0.6.0
pip install -q tqdm==4.64.1
pip install -q wandb==0.13.10
pip install -q hydra-core==1.3.1
pip install -q joblib==1.2.0
pip install -q dill==0.3.6
pip install -q imageio-ffmpeg==0.4.8
pip install -q ftfy==6.1.1
pip install -q ninja==1.10.2.1

pip install -q protobuf==3.20.0
pip install -q tfrecord==1.14.1
```

Remember to put the directory with png images, `ffhq-08`, inside another directory `ffhq`.

To run with multiple GPUs, use
```
torchrun --nnodes=1 --nproc_per_node=[N_GPUS] main.py type=train
```
