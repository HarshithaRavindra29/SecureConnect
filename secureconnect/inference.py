import os


def run(mdl, image_path, debug):
    if os.path.exists(image_path):
        result = mdl.classify(image_path)
        print(result)
        return result
    else:
        print(f"No image found at path: {image_path}")
