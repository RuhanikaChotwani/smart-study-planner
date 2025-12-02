function addTask() {
    fetch("/add_task", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({
            task: document.getElementById("task").value,
            deadline: document.getElementById("deadline").value,
            difficulty: document.getElementById("difficulty").value
        })
    })
    .then(res => res.json())
    .then(data => alert(data.message));
}

function getSchedule() {
    fetch("/get_schedule")
        .then(res => res.json())
        .then(data => {
            let html = "";

            data.tasks.forEach(t => {
                html += `
                    <div class="schedule-item">
                        <b>${t.task}</b><br>
                        Priority: ${t.priority}<br>
                        Deadline: ${t.deadline}<br><br>

                        ${t.completed == 0 
                            ? `<button onclick="completeTask(${t.id})">Mark Completed</button>` 
                            : `<span style='color:green;'>✔ Completed</span>`}
                    </div>
                `;
            });

            document.getElementById("schedule").innerHTML = html;

            document.getElementById("progress").innerHTML =
                `<h3>Progress: ${data.progress}%</h3>
                 <div class="bar"><div class="fill" style="width:${data.progress}%"></div></div>`;
        });
}

function completeTask(id) {
    fetch("/complete_task", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({ task_id: id })
    })
    .then(res => res.json())
    .then(() => getSchedule());
}

function getBestHour() {
    fetch("/best_hour")
        .then(res => res.json())
        .then(data => {
            document.getElementById("best-hour").innerHTML =
                `<b>Best Hour:</b> ${data.best_hour}`;
        });
}
