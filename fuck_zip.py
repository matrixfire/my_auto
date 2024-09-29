import zipfile
import itertools


filename ="x_tst.zip"
# filename ="x_tst.zip'

def uncompress(filename, password):
    try:
        with zipfile.ZipFile(filename) as zfile:
            zfile.extractall("./", pwd=password.encode("utf-8"))
        return True
    except Exception as e:
        print(e)
        return False

# chars = "abcdefghijklmnopqrstuvwxyz0123456789"
# chars = "yz01234"
# for c in itertools.permutations(chars, 4):
#     password = "".join(c)
#     print(password)
#     result = uncompress(filename, password)
#     if not result:
#         print("解压失败", password)
#     else:
#         print("解压成功", password)
#         break


import pyzipper

def unzip_aes_encrypted_zip(zip_path, password_list):
    try:
        # Open the encrypted zip file
        with pyzipper.AESZipFile(zip_path, 'r', compression=pyzipper.ZIP_DEFLATED, encryption=pyzipper.WZ_AES) as extracted_zip:
            # Try each password in the list
            for password in password_list:
                try:
                    # Try to extract all contents using the current password
                    extracted_zip.pwd = str.encode(password)
                    extracted_zip.extractall(path='unzipped_content')
                    print(f"Successfully extracted the files with password: {password}")
                    return True
                except RuntimeError as e:
                    # Print the error and try the next password
                    print(f"Failed with password: {password}, Error: {e}")
        print("Failed to extract files with the given passwords.")
    except FileNotFoundError:
        print("The zip file was not found. Please check the path.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return False



def _unzip_aes_encrypted_zip(zip_path, password):
    try:
        # Open the encrypted zip file
        with pyzipper.AESZipFile(zip_path, 'r', compression=pyzipper.ZIP_DEFLATED, encryption=pyzipper.WZ_AES) as extracted_zip:
            # Try each password in the list
            # for password in password_list:
            try:
                # Try to extract all contents using the current password
                extracted_zip.pwd = str.encode(password)
                extracted_zip.extractall(path='unzipped_content')
                print(f"Successfully extracted the files with password: {password}")
                return True
            except RuntimeError as e:
                # Print the error and try the next password
                print(f"Failed with password: {password}, Error: {e}")
        print("Failed to extract files with the given passwords.")
    except FileNotFoundError:
        print("The zip file was not found. Please check the path.")
    except Exception as e:
        print(f"An error occurred: {e}")
    return False


# Example usage
passwords = ['password123', '123z', 'secret']  # Define your list of passwords
# zip_file_path = 'x_tst.zip'  # Path to your password-protected zip file
zip_file_path = '程序员的数学（第2版）_.zip'  # Path to your password-protected zip file

# Call the function with the path and the password list
# unzip_aes_encrypted_zip(zip_file_path, passwords)

chars = "abcdefghijklmnopqrstuvwxyz0123456789"
# chars = "yz01234"
for c in itertools.permutations(chars, 4):
    password = "".join(c)
    print(f'Now guessing password {password}')
    result = _unzip_aes_encrypted_zip(zip_file_path, password)
    if not result:
        print("解压失败", password)
    else:
        print("解压成功", password)
        break


