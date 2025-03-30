class taskDTO:
    def __init__(self, id: int, name: str, status: str):
        self.id = id
        self.name = name
        self.status = status

    def __repr__(self):
        return f"TaskDTO(id={self.id}, name='{self.name}', status='{self.status}')"

task = taskDTO(1, "Làm báo cáo", "Pending")
print(task)
