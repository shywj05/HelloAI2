from tensorflow import keras
model = keras.models.load_model('/eclipse-workspace/HELLOAI/day30/model/mnist-12-0.0614.hdf5', compile=False)

export_path = '/eclipse-workspace/HELLOAI/day30/model'
model.save(export_path, save_format="tf")