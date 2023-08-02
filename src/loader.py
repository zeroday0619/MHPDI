import os
from pathlib import Path


class DATALoader:
    def __init__(self):
        self.area = [
            "경기도", "광주광역시", "경상북도",
            "전라북도", "부산광역시", "충청북도",
            "충청남도", "인천광역시", "제주특별자치도",
            "세종특별자치시", "경상남도", "서울특별시",
            "전라남도", "강원특별자치도", "대전광역시", "대구광역시", "울산광역시"
        ]
        self.data_dir = Path(os.path.dirname(os.path.abspath(__file__))) / 'dataset'

    def get_dir(self):
        return self.data_dir

    def filter(self, string: str):
        if string.split('.')[-1] == "json":
            return string
    
    def area_serach(self, num: int):
        return self.area[num]

    def list_files(self):
        data = [self.filter(f) for f in os.listdir(self.data_dir) if os.path.isfile(os.path.join(self.data_dir, f))]
        da = [i for i in data if i is not None]
        s = []
        for i in da:
            if len(i.split('_')) == 3:
                if self.area_serach(0) == i.split('_')[2].split('.')[0]:
                    s.append({
                        self.area_serach(0): self.get_dir() / i
                    })
                elif self.area_serach(1) == i.split('_')[2].split('.')[0]:
                    s.append({
                        self.area_serach(1): self.get_dir() / i
                    })
                elif self.area_serach(2) == i.split('_')[2].split('.')[0]:
                    s.append({
                        self.area_serach(2): self.get_dir() / i
                    })
                elif self.area_serach(3) == i.split('_')[2].split('.')[0]:
                    s.append({
                        self.area_serach(3): self.get_dir() / i
                    })
                elif self.area_serach(4) == i.split('_')[2].split('.')[0]:
                    s.append({
                        self.area_serach(4): self.get_dir() / i
                    })
                elif self.area_serach(5) == i.split('_')[2].split('.')[0]:
                    s.append({
                        self.area_serach(5): self.get_dir() / i
                    })
                elif self.area_serach(6) == i.split('_')[2].split('.')[0]:
                    s.append({
                        self.area_serach(6): self.get_dir() / i
                    })
                elif self.area_serach(7) == i.split('_')[2].split('.')[0]:
                    s.append({
                        self.area_serach(7): self.get_dir() / i
                    })
                elif self.area_serach(8) == i.split('_')[2].split('.')[0]:
                    s.append({
                        self.area_serach(8): self.get_dir() / i
                    })
                elif self.area_serach(9) == i.split('_')[2].split('.')[0]:
                    s.append({
                        self.area_serach(9): self.get_dir() / i
                    })
                elif self.area_serach(10) == i.split('_')[2].split('.')[0]:
                    s.append({
                        self.area_serach(10): self.get_dir() / i
                    })
                elif self.area_serach(11) == i.split('_')[2].split('.')[0]:
                    s.append({
                        self.area_serach(11): self.get_dir() / i
                    })
                elif self.area_serach(12) == i.split('_')[2].split('.')[0]:
                    s.append({
                        self.area_serach(12): self.get_dir() / i
                    })
                elif self.area_serach(13) == i.split('_')[2].split('.')[0]:
                    s.append({
                        self.area_serach(13): self.get_dir() / i
                    })
                elif self.area_serach(14) == i.split('_')[2].split('.')[0]:
                    s.append({
                        self.area_serach(14): self.get_dir() / i
                    })
                elif self.area_serach(15) == i.split('_')[2].split('.')[0]:
                    s.append({
                        self.area_serach(15): self.get_dir() / i
                    })
                elif self.area_serach(16) == i.split('_')[2].split('.')[0]:
                    s.append({
                        self.area_serach(16): self.get_dir() / i
                    })
        return s
