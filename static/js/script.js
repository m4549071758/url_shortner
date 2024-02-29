const submitButton = document.getElementById("submit");
submitButton.addEventListener("click", () => {
    const url = document.getElementById("url").value;

    try {
        new URL(url);
    } catch (e) {
        alert("Invalid URL");
        return;
    }

    const postData = { url: url };

    axios.post("/", postData)
    .then((response) => {
        console.log(response);
        document.getElementById("result").innerHTML = response.data.url;
        alert(response.data.message)
    })
    .catch((error) => {
        console.error(error);
    });
});