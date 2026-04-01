from utils.transform import transform_data

def test_transform_data():
    raw_data = [
        {
            "Title": "Test Product",
            "Price": "$100.00",
            "Rating": "Rating: ⭐ 4.5 / 5",
            "Colors": "3 Colors",
            "Size": "Size: M",
            "Gender": "Gender: Men"
        },
        {
            "Title": "Unknown Product",
            "Price": "$50.00",
            "Rating": "Rating: ⭐ 4.0 / 5",
            "Colors": "2 Colors",
            "Size": "Size: L",
            "Gender": "Gender: Women"
        }
    ]

    df = transform_data(raw_data)

    assert len(df) == 1 # Mengecek transform_data dimana hanya ada 1 data valid dari data testing
    assert df.iloc[0]["Price"] == 1600000.0
    assert df.iloc[0]["Rating"] == 4.5
    assert df.iloc[0]["Colors"] == 3
    assert df.iloc[0]["Size"] == "M"
    assert df.iloc[0]["Gender"] == "Men"