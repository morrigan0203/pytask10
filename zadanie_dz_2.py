from pathlib import Path
import csv
import json
import pickle

class Serializer:

    def __init__(self, target: Path) -> None:
        self.target = target
    

    def __scan_dir(self, target: Path, res_list: list)->int:
        size_f = 0
        for path in Path(target).iterdir():
            #print(path, path.is_dir(), path.is_file(), path.name, path.absolute())
            if path.is_dir():
                size_f = size_f + self.__scan_dir(path, res_list)
            else:
                size_f = size_f + path.stat().st_size
            info = {"name":path.name, "full_name":str(path.absolute()), "parent":path.parent.name, "type":"file" if path.is_file() else "directory", "size":size_f}
            res_list.append(info)
        return size_f

    def scan(self) -> list:
        res = []
        self.__scan_dir(self.target, res)
        return res

    def write_csv(self, name: str):
        data = self.scan()
        field_names = ["name", "full_name","parent","type","size"]
        with open(name, 'w') as f:
            write = csv.DictWriter(f, fieldnames=field_names, quotechar='"', skipinitialspace=True, quoting=csv.QUOTE_NONNUMERIC)
            write.writeheader()
            write.writerows(data)

    def write_json(self, name: str):
        data = self.scan()
        with open(name, 'w') as f:
            json.dump(data,f,indent=4)

    def write_pickle(self, name: str):
        data = self.scan()
        with open(name, 'wb') as f:
            pickle.dump(data,f)


if __name__ == "__main__":
    scun_dir = Path(__file__).parent.parent
    print(scun_dir)
    s = Serializer(scun_dir)
    s.write_csv("./TesT_10/dir.csv")
    s.write_json("./TesT_10/dir.json")
    s.write_pickle("./TesT_10/dir.pickle")



