document.getElementById('random-verse-btn').addEventListener('click', function() {
    let userInput = document.getElementById('mood-input').value.trim().toLowerCase();
    let url = '/get-random-verse';  // Default to get a random verse
    
    // If user input is not empty, modify the URL to get a specific verse
    if (userInput) {
        url = `/get-verse-for-situation?mood=${userInput}`;
    }
    
    // Fetch verse based on the input
    fetch(url)
        .then(response => response.json())
        .then(data => {
            const verse = data.verse;
            document.getElementById('bible-verse').textContent = verse;
        })
        .catch(error => {
            console.error('Error fetching verse:', error);
        });
});
