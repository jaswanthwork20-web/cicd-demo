async function callBackend() {

    const result = document.getElementById("result");

    result.innerText = "Calling backend...";

    try {

        const response = await fetch("/api/hello");

        const data = await response.json();

        result.innerText = data.message;

    } catch (error) {

        result.innerText = "Backend connection failed";

        console.error(error);
    }
}