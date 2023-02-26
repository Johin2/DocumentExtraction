# DocumentExtraction
What I did was first make a dictionary in which all the documents I required as input was passed. After that, I created an array of uploaded_paths so that the same document cant be uploaded multiple times
I used OpenCV library to read the documents. After the documents are uploaded the program implements OCR on the documents for this I used py-tesseract. After the OCR is performed using the mysql.connector library I connect the code to my personal database the documents are stored in the BLOB datatype 
