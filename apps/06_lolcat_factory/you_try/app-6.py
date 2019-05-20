import os
import download_cats


def main():
    header()
    folder = get_or_create_output_folder()
    download_cats_images(folder)
    # display cats


def header():
    print('-----------------------------------')
    print('           CAT FACTORY')
    print('-----------------------------------')


def get_or_create_output_folder():
    base_folder = os.path.abspath(os.path.dirname(__file__))
    folder = 'cat_pictures'
    full_path = os.path.join(base_folder, folder)

    if not os.path.exists(full_path) or not os.path.isdir(full_path):
        print('Creating new directory at {}'.format(full_path))
        os.mkdir(full_path)

    return full_path


def download_cats_images(folder):
    print('Contacting server to download cats...')
    cat_count = 8
    for i in range(1, cat_count + 1):
        name = 'lolcat_{}'.format(i)
        print('Downloading {}'.format(name))
        download_cats.get_cat(folder, name)


if __name__ == '__main__':
    main()
