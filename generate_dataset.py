import random
import pandas as pd

safe_domains = [
    "google.com", "facebook.com", "amazon.com",
    "github.com", "openai.com", "microsoft.com",
    "apple.com", "netflix.com", "linkedin.com"
]

phishing_keywords = [
    "login", "verify", "secure", "account",
    "update", "bank", "paypal", "password", "free", "bonus"
]

def generate_safe_url():
    return f"https://{random.choice(safe_domains)}"

def generate_phishing_url():
    return f"http://{random.choice(phishing_keywords)}-{random.choice(phishing_keywords)}-{random.randint(100,999)}{random.choice(['.xyz','.ru','.tk','.ml'])}"

data = []

for _ in range(5000):
    data.append([generate_safe_url(), 0])

for _ in range(5000):
    data.append([generate_phishing_url(), 1])

random.shuffle(data)

df = pd.DataFrame(data, columns=["url", "label"])
df.to_csv("dataset.csv", index=False)

print("Dataset created!")
