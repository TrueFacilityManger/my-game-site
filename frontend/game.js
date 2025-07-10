const API_URL = "https://название-бэкенда.onrender.com";

async function loadLeaderboard() {
  const res = await fetch(${API_URL}/leaderboard);
  const data = await res.json();
  const list = document.getElementById("leaderboard");
  list.innerHTML = "";
  data.forEach(entry => {
    const li = document.createElement("li");
    li.textContent = ${entry.name}: ${entry.score};
    list.appendChild(li);
  });
}

async function submitScore() {
  const name = document.getElementById("name").value;
  const score = parseInt(document.getElementById("score").value);
  await fetch(${API_URL}/submit?name=${name}&score=${score}, {
    method: "POST"
  });
  loadLeaderboard();
}

loadLeaderboard();