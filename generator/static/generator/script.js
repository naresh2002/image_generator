document.addEventListener("DOMContentLoaded", function () {
    const formset = document.getElementById("formset");
    const addBtn = document.getElementById("add-btn");
    const generateBtn = document.querySelector(".generate-btn");

    // Add new text input form
    addBtn.addEventListener("click", function () {
        const totalForms = parseInt(document.querySelector('input[name="form-TOTAL_FORMS"]').value);
        const newFormIndex = totalForms;

        const newForm = document.createElement("div");
        newForm.classList.add("text-form");
        newForm.innerHTML = `
            <input type="text" name="form-${newFormIndex}-text_input" maxlength="150" placeholder="Enter text to generate an image" />
            <input type="hidden" name="form-${newFormIndex}-DELETE" value="False" />
            <button type="button" class="delete-btn">Delete</button>
        `;
        formset.appendChild(newForm);

        // Update form index
        document.querySelector('input[name="form-TOTAL_FORMS"]').value = totalForms + 1;

        // Attach delete event to the delete button
        newForm.querySelector(".delete-btn").addEventListener("click", function () {
            newForm.remove();
            document.querySelector('input[name="form-TOTAL_FORMS"]').value = document.querySelectorAll("#formset .text-form").length;
        });
    });

    // Delete existing text input form
    formset.addEventListener("click", function (event) {
        if (event.target.classList.contains("delete-btn")) {
            event.target.parentElement.remove();
            document.querySelector('input[name="form-TOTAL_FORMS"]').value = document.querySelectorAll("#formset .text-form").length;
        }
    });

    // Validation: Disable generate button if all fields are empty or contain only spaces
    function validateGenerateBtn() {
        const textInputs = formset.querySelectorAll("input[type='text']");
        let isAnyFieldFilled = false;

        textInputs.forEach(input => {
            if (input.value.trim() !== "") {
                isAnyFieldFilled = true;
            }
        });

        generateBtn.disabled = !isAnyFieldFilled;
    }

    // Attach validation event to each input field
    formset.addEventListener("input", validateGenerateBtn);

    // Initial validation check
    validateGenerateBtn();
});
