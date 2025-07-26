import json
from pathlib import Path

class Memory:
    def __init__(self, data_dir="data"):
        self.data_dir = Path(data_dir)
        self.memory_file = self.data_dir / "memory.json"
        self.logs_file = self.data_dir / "logs.json"
        self._create_files_if_not_exist()

    def _create_files_if_not_exist(self):
        self.data_dir.mkdir(exist_ok=True)
        if not self.memory_file.exists():
            with open(self.memory_file, "w") as f:
                json.dump({}, f)
        if not self.logs_file.exists():
            with open(self.logs_file, "w") as f:
                json.dump([], f)

    def get_user_context(self, user_id):
        with open(self.memory_file, "r") as f:
            data = json.load(f)
        return data.get(user_id, {})

    def set_user_context(self, user_id, context):
        with open(self.memory_file, "r+") as f:
            data = json.load(f)
            if user_id not in data:
                data[user_id] = {}
            data[user_id].update(context)
            f.seek(0)
            f.truncate() # Clear existing file content
            json.dump(data, f, indent=4)

    def log(self, entry):
        with open(self.logs_file, "r+") as f:
            logs = json.load(f)
            logs.append(entry)
            f.seek(0)
            f.truncate() # Clear existing file content
            json.dump(logs, f, indent=4)
