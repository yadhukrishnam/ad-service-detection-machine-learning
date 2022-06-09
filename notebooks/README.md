### Notebooks and usages

1. dataset-conversion.ipynb 
    - Combines different datasets from various sources
    - Output: `merged.csv` 
    
2. external-features.ipynb
    - Runs web scraper module and generates valid URLs
    - Contains Domain Name, URL, HTTP Response Code, Class Variable, Zlib Compressed HTML Source code of Web page
    - Output: `external-feature-dataset.csv`
   
3. preprocessing.ipynb
    - Extracts metadata information from compressed Zlib HTML
    - Drops unwanted compressed data
    - Output: `metainfo_decompressed.csv`
    
4. url-features.ipynb
    - Extracts features from URL
    - Includes count of special charecters, domain name extension, http / https, www or absense of www.
    - Length of hostname
    - Output: `final_dataset.csv`