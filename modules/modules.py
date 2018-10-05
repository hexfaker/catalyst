import torch.nn as nn
import catalyst.modules.common as commom
import catalyst.modules.pooling as pooling
import catalyst.modules.noisy as noisy
import catalyst.models.sequential as sequential


MODULES = {
    **nn.__dict__,
    **commom.__dict__,
    **pooling.__dict__,
    **noisy.__dict__,
    **sequential.__dict__
}


def name2nn(name):
    if name is None:
        return None
    elif isinstance(name, nn.Module):
        return name
    elif isinstance(name, str):
        return MODULES[name]
    else:
        return name
