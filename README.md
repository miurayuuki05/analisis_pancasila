
# Pancasila

## Analysis Result

1. Notebook File
2. result.csv

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Virtual environment manager (virtualenv or conda)

## Installation

1. First, clone this repository:
```bash
git clone https://github.com/miurayuuki05/analisis_pancasila.git
cd analisis_pancasila
```

2. Create and activate a virtual environment:

Using virtualenv:
```bash
python -m venv venv
# On Windows
.\venv\Scripts\activate
# On Unix or MacOS
source venv/bin/activate
```

Using conda:
```bash
conda create -n text-analysis python=3.8
conda activate text-analysis
```

3. Install the required packages:
```bash
pip install -r requirements.txt
```

## Project Structure

```
.
├── README.md
├── requirements.txt
└── notebooks/
    └── analysis.ipynb
```

## Running the Notebook

1. Ensure your virtual environment is activated
2. Launch Jupyter Notebook:
```bash
jupyter notebook
```
3. Navigate to the `notebooks` directory and open `analysis.ipynb`

## Dependencies

The project requires the following main packages:

- TensorFlow for deep learning models
- NLTK for natural language processing
- Pandas and NumPy for data manipulation
- Matplotlib for visualization
- Sastrawi for Indonesian text processing
- WordCloud for text visualization

## Troubleshooting

If you encounter NLTK-related errors, you might need to download additional NLTK data:
```python
import nltk
nltk.download('punkt')
nltk.download('vader_lexicon')
```

For Sastrawi-related issues, ensure you have the latest version installed:
```bash
pip install -U Sastrawi
```

## Additional Notes

- Make sure you have sufficient RAM for running the deep learning models
- GPU support is recommended but not required
- For large datasets, consider using batch processing

## Contributing

Feel free to submit issues and enhancement requests.

