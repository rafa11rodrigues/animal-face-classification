import src.utils as utils
from deepfeatx.image import ImageFeatureExtractor

_feature_extractor = ImageFeatureExtractor()
_model = utils.load_model()


def predict(src):
    img = _get_image(src)
    features = _feature_extractor.img_to_vector(img)
    return _get_prediction(features)

def _get_image(src):
    return utils.load_image_from_url(src) if type(src) == str else utils.load_image_from_bytes(src)

def _get_prediction(features):
    probs = _model.predict_proba(features)[0]
    idx = probs.argmax()
    label = _model.classes_[idx]
    prob = probs[idx]
    return {'predicted_label': label, 'confidence': prob}