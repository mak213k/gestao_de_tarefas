function getTasks() {
  fetch("http://localhost:5000/tarefas")
    .then(response => response.json())
    .then(data => {
      const taskList = document.getElementById("taskList");
      taskList.innerHTML = "";

      data.forEach(task => {
        const li = document.createElement("li");
        li.textContent = `${task.nome_tarefa} - ${task.data_tarefa} `;

        const button = document.createElement("button");
        button.textContent = "Deletar";

        button.onclick = () => deletetask(task.id);
                const button2 = document.createElement("button");
        li.appendChild(button);
        taskList.appendChild(li);
      });
    })
    .catch(err => console.error("não foi possivel achar os elementos:", err));
}
   function addTask() {
      const nome_tarefa = document.getElementById("taskName").value;
      const data_tarefa = document.getElementById("taskDate").value;

      if (!nome_tarefa || !data_tarefa) {
        alert("sem informações necessarias.");
        return;
      }

      const newTask = { nome_tarefa, data_tarefa };

      fetch("http://localhost:5000/tarefas", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(newTask)
      })
        .then(response => {
          if (response.ok) {
            document.getElementById("taskName").value = "";
            document.getElementById("taskDate").value = "";
            getTasks();
          } else {
            alert("Erro ao criar tarefa.");
          }
        })
        .catch(err => console.error("Error ao adicionar tarefa:", err));
    }
    function deletetask(id) {
  fetch(`http://localhost:5000/tarefas/${id}`, {
    method: 'DELETE',
  })
  .then(response => {
    if (response.ok) {
      console.log("Tarefa deletada com sucesso.");
      getTasks(); // Atualiza a lista após deletar
    } else {
      console.error("Erro ao deletar a tarefa.");
    }
  })
  .catch(err => console.error("Erro na requisição:", err));
}

    window.onload = getTasks;
