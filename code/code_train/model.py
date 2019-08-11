from keras.applications.inception_v3 import InceptionV3
from keras.layers import Dense, GlobalAveragePooling2D
#from keras.applications.resnet50 import ResNet50
from keras.models import Model

from config import num_classes


# def build_model():
#     base_model = InceptionResNetV2(weights='imagenet', include_top=False)
#     x = base_model.output
#     x = GlobalAveragePooling2D()(x)
#     x = Dense(256, activation='relu')(x)
#     predictions = Dense(num_classes, activation='softmax')(x)
#     model = Model(inputs=base_model.input, outputs=predictions)
#     return model

def build_model():
    base_model = InceptionV3(weights='imagenet', include_top=False)
    #base_model = ResNet50(weights='imagenet', include_top=False)
    x = base_model.output
    x = GlobalAveragePooling2D()(x)
    x = Dense(1024, activation='relu')(x)
    predictions = Dense(num_classes, activation='softmax')(x)
    model = Model(inputs=base_model.input, outputs=predictions)
    return model

# def setup_to_transfer_learn(model,base_model):
#     for layer in base_model.layers:
#         layer.trainable = False
#
# base_model=InceptionResNetV2(weights='imagenet', include_top=False)