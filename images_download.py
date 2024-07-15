from bing_image_downloader import downloader

downloader.download("person", limit=100, output_dir='yolo4_data/images', adult_filter_off=True, force_replace=False, timeout=60)
downloader.download("bird", limit=100, output_dir='yolo4_data/images', adult_filter_off=True, force_replace=False, timeout=60)
downloader.download("dog", limit=100, output_dir='yolo4_data/images', adult_filter_off=True, force_replace=False, timeout=60)
downloader.download("cat", limit=100, output_dir='yolo4_data/images', adult_filter_off=True, force_replace=False, timeout=60)
