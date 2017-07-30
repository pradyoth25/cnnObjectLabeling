from keras.utils.visualize_util import plot
from keras.models import load_model

model = load_model('model_MNIST_test1.h5')
plot(model, to_file='model.png')