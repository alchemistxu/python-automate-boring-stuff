import zipfile

with open('file1.txt', 'w', encoding='utf-8') as file_job:
    file_job.write('Hello' * 100)

with zipfile.ZipFile('example.zip', 'w') as example_zip:
    example_zip.write('file1.txt', compress_type=zipfile.ZIP_DEFLATED)

with zipfile.ZipFile('example.zip','a') as example_zip:
    example_zip.write('spam/file2.txt', compress_type=zipfile.ZIP_DEFLATED)