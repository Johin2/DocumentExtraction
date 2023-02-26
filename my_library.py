import cv2
import pytesseract
from pyspark import SparkContext, SparkConf

# Set Tesseract path
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def extract_details(image_path):
    # Read image using OpenCV
    img = cv2.imread(image_path)

    # Convert image to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Apply thresholding to remove noise
    threshold = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

    # Apply dilation to improve OCR accuracy
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
    dilated = cv2.dilate(threshold, kernel, iterations=1)

    # Extract text from image using Tesseract OCR
    text = pytesseract.image_to_string(dilated, lang='eng', config='--psm 6')

    return text


def process_images(image_paths):
    # Initialize Spark context
    conf = SparkConf().setAppName("Image Processing").setMaster("local[*]")
    sc = SparkContext(conf=conf)

    # Distribute image paths across multiple nodes
    image_paths_rdd = sc.parallelize(image_paths)

    # Extract text from images using Tesseract OCR
    texts_rdd = image_paths_rdd.map(extract_details)

    # Collect results
    texts = texts_rdd.collect()

    # Stop Spark context
    sc.stop()

    return texts
