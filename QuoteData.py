import csv
import json


def load_json_data(file, encode="utf8"):
    """Load json file with quotes"""
    with open(file, "r", encoding=encode) as jfile:
        return json.load(jfile)


class InitData:
    def __init__(self, file, encode="utf8"):
        self.__encode_type = encode
        self.__file_path = file
        self.data = self.__load_data()

    def __load_data(self):
        # Load csv data file with quotes and transfer it to dic
        newdata = {"quote": [], "ref": []}
        with open(self.__file_path, encoding=self.__encode_type) as datafile:
            data = csv.reader(datafile, delimiter='(')
            quote = ""
            temp = ""
            for row in data:
                if row:
                    temp = " ".join(row)
                    if temp[0] != "(":
                        for _ in range(5):
                            if temp[0].isdigit() or temp[0] == ".":
                                temp = temp.replace(temp[0], "")
                        quote = quote + "\n" + temp
                else:
                    newdata["quote"].append(quote)
                    newdata["ref"].append(temp)
                    quote = ""
        return newdata


class SaveData:
    """Saves dic to json file"""
    def __init__(self, data, file, encode="utf8"):
        self.__encode_type = encode
        self.__file_path = file
        self.__data = data
        self.__save_json()

    def __save_json(self):
        with open(self.__file_path, "w", encoding=self.__encode_type) as file:
            json.dump(self.__data, file, indent=4, ensure_ascii=False)
