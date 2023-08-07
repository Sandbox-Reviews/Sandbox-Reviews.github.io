let params = new URLSearchParams(location.search);
let user = params.get("user");
let database = {"1":"2"}
let realdata = `"schemaVersion": 1, "label": "${user}'s Sandbox Review Points", "message": "${database[user]}", "color": "white"`
document.getElementById("json_data").innerHTML = `",${realdata},"alsojunk":"`
