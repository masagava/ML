from dotenv import find_dotenv, load_dotenv
from pathlib import Path


def get_dataset():
    kaggle_path = Path.home() / '.kaggle\\kaggle.json'
    download_path = '..\\data\\external'
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
        filename = api.dataset_list_files('rajyellow46/wine-quality').files[0]
        api.dataset_download_file('rajyellow46/wine-quality', filename.name, path=download_path)

    except Exception as err:
        print(err)
        print('\nInstall kaggle library OR check if `kaggle.json` is correct OR provide correct credentials in .env file')
        exit(0xFF)

    print(f'file `{filename}` was successfully donwloaded into `{download_path}` folder')
    return


if __name__ == '__main__':
    get_dataset()
