import json
import os
import sys


def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

transaction_file = resource_path('config.json')
cwd = os.getcwd()

def transaction_data(mode, data):
    if mode.lower() == 'r':
        with open(transaction_file, 'r') as f:
            json_data = json.load(f)
            return json_data
    elif mode.lower() == 'w':
        with open(transaction_file, 'w') as f:
            json.dump(data, f, indent=4)


def set_user_details(name, section):
    try:
        data = transaction_data(mode='r', data=None)
        data['UserData'] = {}
        data['UserData']['Name'] = name
        data['UserData']['Section'] = section
        transaction_data(mode='w', data=data)
    except Exception as e:
        print(e)


def get_user_details():
    try:
        data = transaction_data(mode='r', data=None)
        details = {'Name': data["UserData"]['Name'], 'Section': data["UserData"]["Section"]}
        return details
    except Exception as e:
        print(e)


def get_message(header):
    try:
        data = transaction_data(mode='r', data=None)
        message = data['Messages'][header]
        return message
    except Exception as e:
        print(e)


def set_selected_file(path):
    try:
        data = transaction_data(mode='r', data=None)
        data['SelectedFile'] = path
        transaction_data(mode='w', data=data)
    except Exception as e:
        print(e)


def get_selected_file():
    try:
        data = transaction_data(mode='r', data=None)
        path = data['SelectedFile']
        return path
    except Exception as e:
        print(e)


def set_image_paths(path):
    try:
        data = transaction_data(mode='r', data=None)
        data['ImagePaths'].append(path)
        transaction_data(mode='w', data=data)
    except Exception as e:
        print(e)


def get_image_paths():
    try:
        data = transaction_data(mode='r', data=None)
        paths = data['ImagePaths']
        return paths
    except Exception as e:
        print(e)


def clear_image_paths():
    try:
        data = transaction_data(mode='r', data=None)
        data['ImagePaths'].clear()
        transaction_data(mode='w', data=data)
    except Exception as e:
        print(e)


def clear_file_path():
    try:
        data = transaction_data(mode='r', data=None)
        data['SelectedFile'] = ''
        transaction_data(mode='w', data=data)
    except Exception as e:
        print(e)


def clear_images():
    try:
        path = r"screenshots"
        for file_name in os.listdir(path):
            file = path + file_name
            if os.path.isfile(file):
                os.remove(file)
    except Exception as e:
        print(e)


def create_screenshot_dir():
    try:
        path = os.path.join(cwd, "screenshots")
        os.mkdir(path)
    except Exception as e:
        print(e)


def delete_screenshot_dir():
    try:
        path = os.path.join(cwd, "screenshots")
        os.rmdir(path)
    except Exception as e:
        print(e)


