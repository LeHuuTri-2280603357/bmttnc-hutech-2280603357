import base64

def main():
    input_String = input("Nhap thong tin can ma hoa: ")

    encoded_bytes = base64.b64encode(input_String.encode("utf-8"))
    encoded_String = encoded_bytes.decode("utf-8")

    with open("data.txt", "w") as file:
        file.write(encoded_String)

    print("Da ma hoa va ghi vao tep data.txt")

if __name__ == "__main__":
    main()
