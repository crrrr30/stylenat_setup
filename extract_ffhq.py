import torch
from tqdm import trange
from tfrecord.torch.dataset import TFRecordDataset
from PIL import Image


tfrecord_path = "/workspace/ffhq-r08.tfrecords"
index_path = None
description = {"data": "byte", "shape": "int"}
dataset = TFRecordDataset(tfrecord_path, index_path, description)
loader = torch.utils.data.DataLoader(dataset, batch_size=1)
dl = iter(loader)

for i in trange(70000):
    data = Image.fromarray(next(dl)["data"].reshape(3, 256, 256).permute(1, 2, 0).numpy()).save(f"./ffhq/{i:05d}.png")
    