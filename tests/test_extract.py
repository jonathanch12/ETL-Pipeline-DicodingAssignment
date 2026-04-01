from utils.extract import scrape_page

def test_scrape_page():
    data = scrape_page(1)
    assert isinstance(data, list)
    assert len(data) > 0
    sample = data[0]
    assert "Title" in sample
    assert "Price" in sample
    assert "Rating" in sample
    assert "Colors" in sample
    assert "Size" in sample
    assert "Gender" in sample