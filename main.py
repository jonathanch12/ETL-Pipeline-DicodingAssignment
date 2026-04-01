from utils.extract import extract_all
from utils.transform import transform_data
from utils.load import load_to_csv

if __name__ == "__main__":
    # Tahap Extract
    raw_data = extract_all()
    print(f"Raw data: {len(raw_data)}")

    # Tahap Transform
    clean_data = transform_data(raw_data)
    print(f"Clean data: {len(clean_data)}")

    # Tahap Load
    load_to_csv(clean_data)