import re

def extract_features(url):
    features = []

    features.append(len(url))
    features.append(1 if re.search(r'\d+\.\d+\.\d+\.\d+', url) else 0)
    features.append(url.count('.'))
    features.append(1 if '@' in url else 0)
    features.append(1 if url.startswith('https') else 0)

    suspicious_words = [
        'login','verify','bank','secure',
        'account','update','free','bonus','password','paypal'
    ]

    features.append(1 if any(word in url.lower() for word in suspicious_words) else 0)

    return features
