async function checkTriangle() {
    const a = document.getElementById("a").value;
    const b = document.getElementById("b").value;
    const c = document.getElementById("c").value;
  
    const response = await fetch("/check", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ a, b, c })
    });
  
    const data = await response.json();
    document.getElementById("result").textContent = data.result;
    if (document.getElementById("result").textContent.includes("These side lengths make a triangle.")) {
        document.getElementById("result").style.color = "green";
    } else {
        document.getElementById("result").style.color = "red";
    }

  }