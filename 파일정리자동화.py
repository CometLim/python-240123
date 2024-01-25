import os
import shutil

# 다운로드 폴더 경로
download_folder = r'C:\Users\blues\Downloads'

# 대상 폴더들의 경로
image_folder = os.path.join(download_folder, 'images')
data_folder = os.path.join(download_folder, 'data')
setup_folder = os.path.join(download_folder, 'Setup')
mail_folder = os.path.join(download_folder, 'mail')
archive_folder = os.path.join(download_folder, 'Archive')
docs_folder = os.path.join(download_folder, 'docs')

# 대상 확장자들
image_extensions = ['.jpg', '.jpeg', '.png']
data_extensions = ['.csv', '.xlsx', '.pptx', '.hwp', '.hwpx']
setup_extensions = ['.exe', '.msi']
mail_extensions = ['.eml']
archive_extensions = ['.zip']
docs_extensions = ['.pdf', '.docx']

# 폴더가 없다면 생성
for folder in [image_folder, data_folder, setup_folder, mail_folder, archive_folder, docs_folder]:
    if not os.path.exists(folder):
        os.makedirs(folder)

# 다운로드 폴더 내의 파일들을 검사하고 이동
for filename in os.listdir(download_folder):
    source_path = os.path.join(download_folder, filename)

    if filename.lower().endswith(tuple(image_extensions)):
        destination_path = os.path.join(image_folder, filename)
    elif filename.lower().endswith(tuple(data_extensions)):
        destination_path = os.path.join(data_folder, filename)
    elif filename.lower().endswith(tuple(setup_extensions)):
        destination_path = os.path.join(setup_folder, filename)
    elif filename.lower().endswith(tuple(mail_extensions)):
        destination_path = os.path.join(mail_folder, filename)
    elif filename.lower().endswith(tuple(archive_extensions)):
        destination_path = os.path.join(archive_folder, filename)
    elif filename.lower().endswith(tuple(docs_extensions)):
        destination_path = os.path.join(docs_folder, filename)
    else:
        continue  # 해당하지 않는 확장자의 파일은 건너뜁니다.

    # 파일 이동
    shutil.move(source_path, destination_path)
    print(f"{filename}을(를) {destination_path}로 이동했습니다.")
