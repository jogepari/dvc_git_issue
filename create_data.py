from pathlib import Path
import shutil
import random
import string


def create_data_file(fpath):
    content = ''.join(random.choices(string.ascii_letters, k=5000000))
    fpath.write_text(content)


def create_non_nested_data(data_root_path):
    for i in range(2):
        create_data_file(data_root_path.joinpath(f'file{i}.txt'))


def create_nested_data(data_root_path):
    for dirL in ('AB'):
        dir_path = data_root_path.joinpath(f'dir{dirL}')
        dir_path.mkdir(exist_ok=True, parents=True)
        create_non_nested_data(dir_path)


data_raw_path = Path('data/raw/')
for fpath in data_raw_path.rglob('*.txt'):
    fpath.chmod(0o644)
shutil.rmtree(data_raw_path, ignore_errors=False)
data_raw_path.mkdir(exist_ok=True)

random.seed(0)
# create_non_nested_data(data_raw_path)
create_nested_data(data_raw_path)
print('Created data/raw')