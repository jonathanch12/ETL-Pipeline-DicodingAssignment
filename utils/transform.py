import pandas as pd

EXCHANGE_RATE = 16000 # Mengubah USD ke IDR

def clean_price(price):
    try:
        if price == "Price Unavailable" or price is None:
            return None
        price = price.replace("$", "").replace(",", "")
        return float(price) * EXCHANGE_RATE
    except:
        return None

def clean_rating(rating):
    try:
        if "Invalid" in rating or "Not Rated" in rating:
            return None
        return float(rating.split("⭐")[-1].replace("/ 5", "").strip())
    except:
        return None

def clean_colors(colors):
    try:
        return int(colors.split()[0])
    except:
        return None

def clean_size(size):
    try:
        return size.replace("Size:", "").strip()
    except:
        return None

def clean_gender(gender):
    try:
        return gender.replace("Gender:", "").strip()
    except:
        return None

def transform_data(data):
    df = pd.DataFrame(data)

    # Membersihkan tiap kolom
    df["Price"] = df["Price"].apply(clean_price)
    df["Rating"] = df["Rating"].apply(clean_rating)
    df["Colors"] = df["Colors"].apply(clean_colors)
    df["Size"] = df["Size"].apply(clean_size)
    df["Gender"] = df["Gender"].apply(clean_gender)

    # Menghapus data invalid, seperti Unknown Product pada Title
    df = df[df["Title"] != "Unknown Product"]

    # Drop data null
    df = df.dropna()

    # Drop data duplikat
    df = df.drop_duplicates()

    # Reset index
    df = df.reset_index(drop=True)

    return df