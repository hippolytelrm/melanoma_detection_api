import numpy as np
from PIL import Image

def preprocessing(image:Image):

    img = image.resize((224,) * 2)
    img = np.asarray(img)
    img = np.expand_dims(img/255., axis=0)

    return img