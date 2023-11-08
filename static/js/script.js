const table = document.getElementById("myTable");
        const checkboxes = document.querySelectorAll(".move-checkbox");

        // Add click event listeners to checkboxes
        checkboxes.forEach(checkbox => {
            checkbox.addEventListener("change", () => {
                if (checkbox.checked) {
                    // Get the row that contains the checked checkbox
                    const row = checkbox.closest("tr");
                    // Move the row to the bottom of the table
                    table.appendChild(row);
                }
            });
        });