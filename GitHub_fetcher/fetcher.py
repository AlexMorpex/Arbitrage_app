import logging
import aiohttp
import asyncio
import json
import hashlib
import pathlib
import os

DEBUG = True

BASE_PATH = pathlib.Path().absolute()
GITHUB_URL = 'https://api.github.com/repos/AlexMorpex/Arbitrage_app/contents'
JSON_PATH = BASE_PATH.joinpath('files.json')

if DEBUG:
    BASE_PATH = pathlib.Path().absolute().joinpath('Test_folder')
    JSON_PATH = BASE_PATH.joinpath('files.json')

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s')


# ==========  Create .json ==========


async def recursive_check_null(session: aiohttp.ClientSession, files_dict: list, el):
    try:
        async with session.get(el['url']) as response:
            for el in await response.json():
                if el['type'] == "file":
                    async with session.get(el['download_url']) as r:
                        sha256 = hashlib.sha256(await r.read()).hexdigest()
                        logging.info(f"{el['name']} : {sha256}")

                    files_dict[el['name']] = {'Path': el['path'],
                                              'raw_url': el['download_url'],
                                              'sha256': sha256}
                else:
                    await recursive_check_null(session, files_dict, el)
    except Exception as e:
        logging.critical(f'Error in ( recursive_check_null ) : {e}')


async def get_dict_of_files_from_github(session: aiohttp.ClientSession, url) -> dict:
    try:
        async with session.get(url) as response:
            files_dict = {}
            for el in await response.json():
                if el['type'] == "file":
                    if el['name'] == 'files.json':
                        continue
                    async with session.get(el['download_url']) as r:
                        sha256 = hashlib.sha256(await r.read()).hexdigest()
                        logging.info(f"{el['name']} : {sha256}")

                    files_dict[el['name']] = {'Path': el['path'],
                                              'raw_url': el['download_url'],
                                              'sha256': sha256}
                else:
                    await recursive_check_null(session, files_dict, el)
            return files_dict
    except Exception as e:
        logging.critical(f'Error in ( get_list_of_files_from_github ) : {e}')


def write_json_file(d: dict, json_path) -> None:
    if os.path.exists(json_path):
        logging.info('Есть json файл, перезаписываю')
        with open(json_path, 'w') as f:
            json.dump(d, f, indent=4)
    else:
        logging.info('Нет json файла, записываю')
        if not os.path.exists(BASE_PATH):
            os.makedirs(BASE_PATH)
        with open(json_path, 'x') as f:
            json.dump(d, f, indent=4)

# ==========  ========== ========== ==========


async def compare_json_sha():
    pass

# ==========  Create all files ==========


async def write_file(file_path: pathlib.Path, content) -> str:
    f_path = BASE_PATH.joinpath(file_path)

    if os.path.exists(f_path):
        print('Файл есть, перезаписываю')
        with open(f_path, 'wb') as f:
            f.write(content)

        with open(BASE_PATH.joinpath(file_path), 'rb') as file:
            f = file.read()
            hash = hashlib.sha256(f).hexdigest()
            return hash

    elif pathlib.Path(f_path.parent).exists():
        print('Есть директория но нет файла')
        with open(f_path, 'wb') as f:
            f.write(content)

        with open(BASE_PATH.joinpath(file_path), 'rb') as file:
            f = file.read()
            hash = hashlib.sha256(f).hexdigest()
            return hash

    else:
        print('Ничего нет, создаю с 0')
        os.makedirs(f_path.parent, exist_ok=True)
        with open(f_path, 'wb') as f:
            f.write(content)

        with open(BASE_PATH.joinpath(file_path), 'rb') as file:
            f = file.read()
            hash = hashlib.sha256(f).hexdigest()
            return hash


async def write_all_files(session: aiohttp.ClientSession, file_path: pathlib.Path):
    with open(JSON_PATH, 'r') as file:
        dict_file = json.load(file)
        try:
            for key, value in dict_file.items():
                async with session.get(value['raw_url']) as response:
                    content = await response.read()
                    await write_file(value['Path'], content)
        except Exception as e:
            logging.critical(f'Failed to write files. Error: {e}')
            async with session.get(GITHUB_URL) as response:
                res = await response.read()
                logging.critical(res)

# ==========  ========== ========== ==========


def is_binary(file_path):
    with open(file_path, 'rb') as f:
        chunk = f.read(1024)
        if b'\x00' in chunk:
            return True
    return False


async def check_file_sha256(session: aiohttp.ClientSession) -> bool:
    try:
        files_dict = await get_dict_of_files_from_github(session, GITHUB_URL)
        with open(BASE_PATH.joinpath('json_temp.json'), 'x') as f:
            json.dump(files_dict, f, indent=4)
        with open(BASE_PATH.joinpath('json_temp.json'), 'r') as f:
            file = f.read().encode()
            sha1 = hashlib.sha256(file).hexdigest()
            logging.info(f"github json sha : {sha1}")
        os.unlink(BASE_PATH.joinpath('json_temp.json'))
        with open(JSON_PATH, 'r') as f:
            file = f.read().encode()
            sha2 = hashlib.sha256(file).hexdigest()
            logging.info(f"file json sha : {sha2}")
        logging.info(sha1 == sha2)
        return sha1 == sha2
    except Exception as e:
        logging.critical(f'Error in main else : {e}')


# ==========  ========== ========== ==========


async def main():
    async with aiohttp.ClientSession() as session:
        if not os.path.exists(JSON_PATH):
            files_dict = await get_dict_of_files_from_github(session, GITHUB_URL)
            write_json_file(files_dict, JSON_PATH)
            await write_all_files(session, BASE_PATH)

        else:
            res = await check_file_sha256(session)
            if not res:
                # TODO тут будет проверка и исправленее каждого файла
                pass


if __name__ == '__main__':
    asyncio.run(main())
