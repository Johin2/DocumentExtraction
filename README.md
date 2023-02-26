# DocumentExtraction
The code defines several functions to upload images, perform OCR (Optical Character Recognition) on them, and insert them into a MySQL database.

The upload_file() function reads an image file using OpenCV, resizes it, displays it, performs OCR on it using the Tesseract library, and prints the recognized text to the console.

The insert_to_database() function inserts an image file and its metadata into a MySQL database.

The upload_documents() function prompts the user to enter the document type and file paths for each image, calls the upload_file() function to process the images and collect their text, and stores the results in a dictionary.

The main() function connects to a MySQL server, calls upload_documents() to process the images and store them in the database, and prints a success or cancellation message to the console.

Overall, this code enables the user to upload images, extract text from them, and store the text and metadata in a MySQL database.

This project will keep on updating as I learn new things
