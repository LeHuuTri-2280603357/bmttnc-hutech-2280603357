import hashlib

def calculate_md5(input_String):
    md5_hash = hashlib.md5()
    md5_hash.update(input_String.encode('utf-8'))
    return md5_hash.hexdigest()

input_String = input("Nhap chuoi can bam: ")
md5_hash = calculate_md5(input_String)

print("Ma bam Md5 cus chuoi '{}' la: {}".format(input_String, md5_hash))