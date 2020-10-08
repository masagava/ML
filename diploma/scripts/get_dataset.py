from dotenv import find_dotenv, load_dotenv
from pathlib import Path
from time import time, ctime

import zipfile


class Error(Exception):
    pass


def get_dataset():
    kaggle_path = Path.home() / '.kaggle\\kaggle.json'
    download_path = '..\\data\\external'
    dwnld_pth = Path(download_path)
    dwnld_pth.mkdir(exist_ok=True, parents=True)

    if not kaggle_path.exists():
        dotenv_path = find_dotenv()
        if not dotenv_path:
            print('provide credentials in .env file')
            exit(0xFF)
        else:
            load_dotenv(dotenv_path=dotenv_path)

    try:
        from kaggle.api.kaggle_api_extended import KaggleApi

        api = KaggleApi()
        api.authenticate()
        # dataset_files = api.dataset_list_files('rajyellow46/wine-quality').files
        filename = api.dataset_list_files('austinreese/craigslist-carstrucks-data').files[0]
        api.dataset_download_file('austinreese/craigslist-carstrucks-data', filename.name, path=download_path)

    except Exception as err:
        print(err)
        print('\nInstall kaggle library OR check if `kaggle.json` is correct OR provide correct credentials in .env file')
        exit(0xFF)

    print(f'file `{filename}` was successfully donwloaded into `{download_path}` folder')
    for i, fn in enumerate(list(dwnld_pth.glob('*.zip'))):
        zf = zipfile.ZipFile(fn)
        try:
            zf.extractall(path=dwnld_pth)
            print(f'#{i}: file {fn.name} was unzipped')
        except Error as e:
            print(f'Error was occured: {e}')

        zf.close()

    return


if __name__ == '__main__':
    start = time()
    print(f'Processing started: {ctime()}')

    get_dataset()

    print(f'Elapsed time: {time()-start:.3f}s')
