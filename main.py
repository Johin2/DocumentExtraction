import mysql.connector
import cv2
import pytesseract
import my_library as lib
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def upload_file(file_path):
    if not os.path.isfile(file_path):
        raise FileNotFoundError("File not found")

    img = cv2.imread(file_path)
    height, width = img.shape[:2]
    img = cv2.resize(img, (width // 2, height // 2))
    cv2.imshow("image", img)
    cv2.waitKey(0)

    text = pytesseract.image_to_string(img, lang='eng', config='--psm 4')
    print("OCR Output:\n", text)


def insert_to_database(file_path, document_type, cnx):
    with open(file_path, 'rb') as img:
        img_data = img.read()

        cursor = cnx.cursor()
        stmt = "INSERT INTO documents (Name, image, document_type) VALUES (%s, %s,%s)",
        for file_path in file_paths:
            with open(file_path, 'rb') as img:
                img_data = img.read()
                cursor.execute(stmt, (file_path, img_data, document_type))
        cnx.commit()
        cursor.close()


def upload_documents():
    documents = {"Aadhar Card": [], "Pan Card": [], "Bank Statement": [], "ITR/Form 16": [], "Selfie": [],
                 "Utility Bill": [], "Cheque": [], "Salary Slip": [], "Driving License": [], "Voter ID": [],
                 "Passport": []}
    uploaded_paths = []
    quit_flag = False

    while not quit_flag:
        document_type = input("Enter Document type or type 'q' to quit.")
        if document_type.lower() == 'q':
            quit_flag = True
            break

        while True:
            file_paths = input(f"Enter file paths for {document_type} (comma separated): ").split(",")
            if all([os.file.isfile(file_path) for file_path in file_paths]):
                break
            else:
                print("One or more file not found. Please try again.")

            for file_path in file_paths:
                if file_path in uploaded_paths:
                    print("This file has already been uploaded. Please upload a different file.")
                    continue

            uploaded_paths.append(file_path)
            try:
                upload_file(file_path)
            except FileNotFoundError:
                print(f"{file_path} not found. Skipping Upload")
                continue
            documents[document_type].append(file_path)

    return uploaded_paths, documents, quit_flag


def main():
    uploaded_paths, documents, quit_flag = upload_documents()

    # Connecting to my Sql Server
    with mysql.connector.connect(
        host="localhost",
        user="root",
        password="Johin2004!",
        database="documents"
    ) as cnx:

        if not quit_flag:
            for document_type, file_paths in documents.items():
                for file_path in file_paths:
                    insert_to_database(file_path, document_type, cnx)

            print("Images Uploaded successfully")
        else:
            print("Image uploading cancelled by user")

        cnx.close()


if __name__ == "__main__":
    main()
