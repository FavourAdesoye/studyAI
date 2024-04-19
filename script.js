const dataContainer = document.getElementById('data-container');
//test
async function fetchData() {
    try {
        const response = await fetch('/api/get-data');  // Replace with your actual route
        const data = await response.json();
        // Process the API data here (e.g., display in the container)
        dataContainer.textContent = JSON.stringify(data, null, 2);
    } catch (error) {
        dataContainer.textContent = `Error: ${error.message}`;
    }
}

fetchData(); //test