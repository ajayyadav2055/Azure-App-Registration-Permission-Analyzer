from pathlib import Path
from llama_index import download_loader

#llamahub JSON data connectors: https://llamahub.ai/l/file-json?from=all
#original code for JSON data connectors: https://github.com/run-llama/llama-hub/tree/2c95b021246b54b0542bf9ed9289828cc9da6654/llama_hub/file/json

JSONReader = download_loader("JSONReader")

loader = JSONReader()
documents = loader.load_data(Path('./Data/Permission_data.json'))