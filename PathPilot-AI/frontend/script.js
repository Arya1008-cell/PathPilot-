async function analyze() {

  const profile = document.getElementById("profile").value;
  const loading = document.getElementById("loading");
  const output = document.getElementById("output");

  loading.style.display = "block";
  output.textContent = "";

  const response = await fetch("http://127.0.0.1:8000/analyze", {
    method: "POST",
    headers: {"Content-Type": "application/json"},
    body: JSON.stringify({ profile })
  });

  const data = await response.json();

  loading.style.display = "none";
  output.textContent = data.result || data.error;
}
