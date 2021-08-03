import tensorflow as tf

saved_model_dir = 'D:/eclipse-workspace/HELLOAI/day30/model/saved_model.pb'

converter = tf.lite.TFLiteConverter.from_saved_model(saved_model_dir)
converter.target_spec.supported_ops = [tf.lite.OpsSet.TFLITE_BUILTINS,
                                       tf.lite.OpsSet.SELECT_TF_OPS]
tflite_quant_model = converter.convert()

open('/eclipse-workspace/HELLOAI/day30/model/converted_model.tflite', 'wb').write(tflite_quant_model)
