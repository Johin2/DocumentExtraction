import mysql.connector
import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

documents = {"Aadhar Card": [], "Pan Card": [], "Bank Statement": [], "ITR/Form 16": [], "Selfie": [], "Utility Bill": [], "Cheque": [], "Salary Slip": [], "Driving License": [], "Voter ID": [], "Passport": []}

uploaded_paths = []


def upload_file(file_path, document_type):
    while file_path in uploaded_paths:
        print("This file has already been uploaded. Please upload a different file.")
        file_path = input("Enter the file location again: ")
        continue
    uploaded_paths.append(file_path)
    # Perform the file upload here
    print("Uploading file:", file_path)
    try:
        img = cv2.imread(file_path)
        height, width = img.shape[:2]
        img = cv2.resize(img, (width // 2, height // 2))
        cv2.imshow("image", img)
        cv2.waitKey(0)

        text = pytesseract.image_to_string(img, lang='eng', config='--psm 4')
        print("OCR Output:\n", text)

    except FileNotFoundError as e:
        print("File not found, Please upload the file again")


document_type = "Aadhar Card"
AadharCard = input("Enter Aadhar Card Image file location: ").split(",")
for file_path in AadharCard:
    upload_file(file_path, document_type)

document_type = "Pan Card"
PanCard = input("Enter Pan Card Image file location: ").split(",")
for file_path in PanCard:
    upload_file(file_path, document_type)

document_type = "Bank Statement"
Bank_Statement = input("Enter Bank Statement Image file location: ").split(",")
for file_path in Bank_Statement:
    upload_file(file_path, document_type)

document_type = "ITR/Form 16"
ITR_Form16 = input("Enter ITR/Form 16 Image file location: ").split(",")
for file_path in ITR_Form16:
    upload_file(file_path, document_type)

document_type = "Selfie"
Selfiepic = input("Upload a Selfie Image file location: ").split(",")
for file_path in Selfie:
    upload_file(file_path, document_type)

document_type = "Utility Bill"
UtilityBill = input("Enter a Utility Bill Image file location: ").split(",")
for file_path in UtilityBill:
    upload_file(file_path, document_type)

document_type = "Cheque"
ChequeLeaf = input("Enter a Cheque Image file location: ").split(",")
for file_path in ChequeLeaf:
    upload_file(file_path, document_type)

document_type = "Salary Slip"
Salaryslip = input("Enter a Salary slip Image file location: ").split(",")
for file_path in Salaryslip:
    upload_file(file_path, document_type)

document_type = "Driving License"
DrivingLicense = input("Enter a Drivers License file location: ").split(",")
for file_path in DrivingLicense:
    upload_file(file_path, document_type)

document_type = "Voter ID"
VoterId = input("Enter a Voter Id Image file location: ").split(",")
for file_path in VoterId:
    upload_file(file_path, document_type)

document_type = "Passport"
PassportId = input("Enter a Passport Image file location: ").split(",")
for file_path in PassportId:
    upload_file(file_path, document_type)

# Connecting to my Sql Server
cnx = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Johin2004!",
            database="documents"
        )

cursor = cnx.cursor()

for file_path in uploaded_paths:
    document_type = input("Enter the document type")
    with open(file_path, 'rb') as img:
        img_data = img.read()

        # Insert the image data into the table
        cursor.execute("INSERT INTO documents (Name, image, document_type) VALUES (%s, %s,%s)", (file_path, img_data, document_type))
        cnx.commit()

cursor.close()
cnx.close()

print("Image uploaded successfully")

