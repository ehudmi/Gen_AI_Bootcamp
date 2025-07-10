from utils import unzip_with_7z as unz

zip_file_path = "congrats.7z"  # keep as is
dest_path = "."  # keep as is

find_me = ""  # 2 letters are missing!
secret_password = find_me + "bcmpda"
# print(unz(zip_file_path, dest_path, secret_password))


# WRITE YOUR CODE BELOW
def try_unzip():
    global find_me, secret_password
    counter = 0
    for i in range(97, 123):
        for j in range(97, 123):
            find_me = chr(i) + chr(j)
            secret_password = find_me + "bcmpda"
            counter += 1
            # print(find_me, secret_password, counter)
            if unz(zip_file_path, dest_path, secret_password):
                break
    print(f"The password was {secret_password}")


try_unzip()
