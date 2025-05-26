import tensorflow as tf
import os

def convert_to_tflite(saved_model_dir, tflite_model_path, quantize=False):
    converter = tf.lite.TFLiteConverter.from_saved_model(saved_model_dir)
    if quantize:
        converter.optimizations = [tf.lite.Optimize.DEFAULT]
    tflite_model = converter.convert()

    with open(tflite_model_path, 'wb') as f:
        f.write(tflite_model)

    print(f"Model converted and saved to: {tflite_model_path}")

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 3:
        print("Usage: python optimize_models.py <saved_model_dir> <output_tflite_path> [--quantize]")
    else:
        model_path = sys.argv[1]
        output_path = sys.argv[2]
        quant = '--quantize' in sys.argv
        convert_to_tflite(model_path, output_path, quantize=quant)
