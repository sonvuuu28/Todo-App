// Khi DOM đã sẵn sàng, thực hiện các thao tác sau:
document.addEventListener("DOMContentLoaded", function() { 
    // Lấy tham chiếu đến các phần tử HTML cần thiết
    const tenCongViec = document.getElementById("tenCongViec");  
    const themCongViec = document.getElementById("themCongViec"); 
    const dsCongViec = document.getElementById("dsCongViec");

    // Hàm thêm task mới
    function addTask() {
        const text = tenCongViec.value.trim();
        if (!text) return; // Nếu không nhập gì, dừng hàm

        // Gửi POST request để thêm task vào DB
        fetch('/add_task', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'  // Dữ liệu gửi đi ở định dạng JSON
            },
            body: JSON.stringify({ name: text, status: false })  // Chuyển đối tượng JS thành chuỗi JSON
        })
        .then(response => response.json())  // Chuyển đổi phản hồi từ server thành đối tượng JS
        .then(data => {
            if (data.success) {
                // Nếu thêm thành công, reload lại trang để cập nhật danh sách task từ DB
                window.location.reload();
            } else {
                alert("Thêm công việc thất bại!");
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
    }

    // Hàm xóa task từ DB và cập nhật giao diện
    function deleteTask(taskId, taskElement) {
        fetch('/delete_task', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            // Gửi id của task cần xóa
            body: JSON.stringify({ id: taskId })
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                // Nếu xóa thành công trên DB, loại bỏ element khỏi DOM
                taskElement.remove();
            } else {
                alert("Xóa công việc thất bại!");
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
    }

    // Hàm update task: khi checkbox thay đổi, cập nhật status của task
    function updateTask(taskId, newStatus) {
        fetch('/update_task', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            // Gửi id và trạng thái mới của task
            body: JSON.stringify({ id: taskId, status: newStatus })
        })
        .then(response => response.json())
        .then(data => {
            if (!data.success) {
                alert("Cập nhật trạng thái thất bại!");
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
    }

    // Gán sự kiện cho nút thêm: khi click, gọi hàm addTask
    themCongViec.addEventListener("click", addTask);

    // Gán sự kiện cho ô input: khi nhấn Enter, gọi hàm addTask
    tenCongViec.addEventListener("keypress", function(event) {
        if (event.key === "Enter") {
            addTask();
        }
    });

    // Gán sự kiện xóa cho tất cả các icon delete (được render từ DB)
    dsCongViec.querySelectorAll(".delete").forEach(function(deleteIcon) {
        deleteIcon.addEventListener("click", function() {
            const taskId = this.getAttribute("data-id");
            const taskElement = this.closest(".box");
            deleteTask(taskId, taskElement);
        });
    });

    dsCongViec.querySelectorAll("input[type='checkbox']").forEach(function(checkbox) {
        checkbox.addEventListener("change", function() {
            const taskId = this.getAttribute("data-id");
            const newStatus = this.checked;
            updateTask(taskId, newStatus);
        });
    });
});
