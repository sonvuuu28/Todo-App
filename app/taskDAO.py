import mysql.connector

class taskDAO:  # Đổi tên class theo quy ước PascalCase
    @staticmethod
    def getConnection():
        try:
            conn = mysql.connector.connect(
                host="mysql_container",
                user="root",
                password="123",
                database="todo_db"
            )
            print("Kết nối MySQL thành công!")
            return conn
        except mysql.connector.Error as err:
            print(f"Lỗi kết nối MySQL: {err}")
            return None 

    @staticmethod
    def insert(taskDTO):
        conn = taskDAO.getConnection()
        if conn is None:
            return False
        
        try:
            cursor = conn.cursor()
            sql = "INSERT INTO tasks (name, status) VALUES (%s, %s)"
            cursor.execute(sql, (taskDTO.name, taskDTO.status))
            conn.commit()
            cursor.close()
            conn.close()
            return True
        except mysql.connector.Error as err:
            print(f"Lỗi khi chèn task: {err}")
            return False

    @staticmethod
    def delete(taskDTO):
        conn = taskDAO.getConnection()
        if conn is None:
            return False

        try:
            cursor = conn.cursor()
            sql = "DELETE FROM tasks WHERE id = %s"
            cursor.execute(sql, (taskDTO.id, ))  # Phải có dấu "," để tránh lỗi tuple
            conn.commit()
            cursor.close()
            conn.close()
            return True
        except mysql.connector.Error as err:
            print(f"Lỗi khi xóa task: {err}")
            return False  
        
    @staticmethod
    def update(taskDTO):
        conn = taskDAO.getConnection()
        if conn is None:
            return False
        try:
            cursor = conn.cursor()
            sql = "UPDATE tasks SET status = %s WHERE id = %s"
            cursor.execute(sql, (taskDTO.status, taskDTO.id))
            conn.commit()
            cursor.close()
            conn.close()
            return True
        except mysql.connector.Error as err:
            print(f"Lỗi khi sửa task: {err}")
            return False

    @staticmethod
    def list():
        conn = taskDAO.getConnection()
        if conn is None:
            return []
        
        try:
            cursor = conn.cursor(dictionary=True)
            sql = "SELECT * FROM tasks"
            cursor.execute(sql)
            tasks = cursor.fetchall()  # Trả về list các dict
            cursor.close()
            conn.close()
            return tasks
        except mysql.connector.Error as err:
            print(f"Lỗi lấy danh sách task: {err}")
            return []

# Test chạy thử
if __name__ == "__main__":
    tasks = taskDAO.list()
    for task in tasks:
        print(task)
