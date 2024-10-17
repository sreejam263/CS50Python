def main():
    filename = input('File Name (with extensions):\n ').strip().lower()
    extension = filename.rpartition(".")[2]

    match extension:
        case "gif" | "png":
            print('image/'+extension)
        case "jpg" | "jpeg":
            print('image/jpeg')
        case "pdf" | "zip":
            print('application/'+extension)
        case "txt":
             print('text/plain')
        case _:
            print('application/octet-stream')

main()




