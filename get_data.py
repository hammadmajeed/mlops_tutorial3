
# data from https://www.sciencedirect.com/science/article/pii/S2352340920303048

# Download the zipped dataset
url = 'https://drive.google.com/file/d/1NFjX2SUFheYRACqiwC6Vno7Fh-mmYna5/view?usp=sharing'
name = "data_raw.csv"

import gdown

gdown.download(url, name, quiet=False, fuzzy=True)

