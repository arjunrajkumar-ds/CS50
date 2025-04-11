def main():
    filename = input("File name: ").lower().strip()
    extension = filename.split(".")[-1]
    match extension:
        case "gif":
            print(f"image/{extension}")
        case "jpg":
            print(f"image/jpeg")
        case "jpeg":
            print(f"image/jpeg")
        case "png":
            print(f"image/{extension}")
        case "pdf":
            print(f"application/{extension}")
        case "txt":
            print(f"text/plain")
        case "zip":
            print(f"application/{extension}")
        case _:
            print(f"application/octet-stream")

main()