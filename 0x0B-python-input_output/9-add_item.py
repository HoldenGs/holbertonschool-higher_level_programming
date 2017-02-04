#!/usr/bin/python3


if __name__ == "__main__":
    from sys import argv
    json_file = "add_item.json"
    save_json = __import__('7-save_to_json_file').save_to_json_file
    load_json = __import__('8-load_from_json_file').load_from_json_file
    try:
        json_list = load_json(json_file)
    except:
        json_list = []
    for item in argv[1:]:
        json_list.append(item)
    save_json(json_list, json_file)
